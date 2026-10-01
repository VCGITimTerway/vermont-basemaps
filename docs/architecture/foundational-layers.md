# Foundational Layers & Delivery Architecture

Context for *why* the basemaps in this repo are built the way they are, not
just *how* — the layer inventory, current vs. target delivery formats, and
the publishing/maintenance workflow changes needed to support reliable,
performant basemaps across both ArcGIS (Map Viewer, Experience Builder) and
open-source (MapLibre/Leaflet/etc.) applications.

## Planned basemaps

Not yet finalized, but the working set is:

- **Light**, **Dark** — colored, general-purpose web basemaps
- **Physical Geography** — the hypsometric/terrain-tint style being
  developed in [`../dem-color-ramps/`](../dem-color-ramps/)
- Possibly separate **monochrome gray/white/black** basemaps (Protomaps-style),
  distinct from Light/Dark rather than a palette swap of them — undecided

Every variant needs to work in both ArcGIS-based apps and open-source
web apps, which is the main constraint shaping the delivery architecture
below: raster and vector data each need a path that works on both sides,
and ideally from one maintained source rather than two drifting copies.

## Delivery architecture (already in production)

Two pieces of shared infrastructure already exist and are live — this
basemap effort is a new *consumer* of both, not something building them
from scratch.

### Raster → TiTiler

[`VCGI/titiler-deployment`](https://github.com/VCGI/titiler-deployment) — a
TiTiler instance (AWS Lambda + CloudFront) at `https://titiler.geo.vermont.gov`,
reading COGs directly from the `vtopendata-prd`/`vtopendata-dev` S3 buckets
and returning dynamically styled tiles (colormap, rescale, band math, etc.
via query params) in standard XYZ/TileJSON form. No format change needed —
the COGs already in S3 work as-is.

The repo's `titiler-endpoint-generator` tool builds correctly-templated tile
URLs for ArcGIS, XYZ, WMTS, and TileJSON consumers from the same underlying
endpoint — including handling ArcGIS's swapped `{z}/{y}/{x}` token order
(vs. XYZ's `{z}/{x}/{y}`). This is the piece that makes one styled raster
endpoint usable from both an open-source MapLibre map and an ArcGIS Online
web map.

### Vector → PMTiles (+ parallel Esri Vector Tiles)

[`VCGI/pmtiles`](https://github.com/VCGI/pmtiles) — a PMTiles CDN
(CloudFront + Lambda, reading `.pmtiles` files via HTTP byte-range
requests) at `https://pmtiles.geo.vermont.gov`, serving both vector
(`.mvt`) and raster (`.webp`/`.png`) tilesets out of the same two S3
buckets.

- **Generation pipeline (in development):** AGOL hosted feature layer →
  intermediate export (FlatGeobuf/GeoJSON) → `tippecanoe` (via Docker,
  since it's not natively a Windows tool) → `.pmtiles`. Plan is to host
  this in AWS so it's a no-install, "drag and drop" job rather than
  something requiring local tooling.
- **ArcGIS Online consumption already worked out:** vector tilesets need a
  hosted Mapbox-Style-Spec `style.json` pointing at the tile URL (added via
  *Add Layer from URL* → Vector Tile Layer, or published as a reusable
  hosted item via ArcGIS Pro → *Share As Web Layer*); raster tilesets are
  plain XYZ (same `{z}/{y}/{x}` token-order gotcha as TiTiler above).
- **Existing tooling:** `inspect-pmtiles.mjs` (reads a tileset's schema/zoom
  range/bounds via range requests, no full download) and
  `arcgis-webmap.mjs` (pulls an AGOL web map's renderer/labeling/popup JSON
  for conversion into a MapLibre `style.json`) — the data-gathering half of
  the `arcgis-to-maplibre` Claude Code skill. This tooling runs **one
  direction**: AGOL symbology → MapLibre style. There's no equivalent tool
  yet for the reverse (MapLibre style → Esri Vector Tile Style Editor
  input), which matters below.
- **Important limitation:** the existing elevation PMTiles tileset
  (`STATEWIDE_2023_35cm_DEMHF_TERRARIUM.pmtiles`) uses Mapzen/Terrarium
  RGB-encoded elevation values, not a styled image. ArcGIS Online's generic
  tile layer doesn't decode Terrarium encoding automatically — so this
  tileset is usable for open-source/MapLibre client-side elevation work
  (hillshading, analysis) but **not** as a drop-in visual layer in ArcGIS.
  For a styled, cross-platform DEM/hillshade visual (which is what the
  basemaps need), TiTiler-COG is the right path, not PMTiles-Terrarium —
  these two raster paths serve different purposes from the same source COG.

### Esri Community Maps (separate, existing pipeline)

VCGI contributes foundational layers to Esri's Community Maps program on a
~6-month cadence, which populates the Living Atlas Human Geography
light/dark **detail** and **label** layers. At least transportation and
place names are, today, typically consumed in Esri-centric apps as a styled
Esri vector tile layer *from Living Atlas*, not from VCGI's own VSDI
publishing path. That's a real asymmetry: there's no open-source equivalent
of Living Atlas, so those two themes need their own VSDI → PMTiles path for
non-Esri apps — see [Gaps](#gaps--open-questions) below.

## Foundational layer inventory

Default assumption for everything below unless noted otherwise: **VSDI**
vector layers are currently hosted feature layers in ArcGIS Online; raster
products are COGs in the `vtopendata-prd`/`vtopendata-dev` S3 buckets.

### VSDI (Vermont Spatial Data Infrastructure)

| Layer | Current format/source | Notes |
|---|---|---|
| State Boundary | AGOL hosted feature layer | |
| County Boundaries | AGOL hosted feature layer | |
| Municipal Boundaries | AGOL hosted feature layer | |
| Village Boundaries | AGOL hosted feature layer | |
| Parcels | AGOL hosted feature layer | Already has a PMTiles proof-of-concept (`parcels.pmtiles`, sandbox prefix) |
| Protected Lands | AGOL hosted feature layer(s) | Subtypes: state parks, state forests, national parks, national forests, national wildlife refuges, national wilderness areas, municipal parks, municipal forests |
| Military Sites | AGOL hosted feature layer | |
| 1' Contours (QL2 lidar) | **Not a hosted feature layer** — published via ArcGIS Server ([cached WM MapServer](https://maps.vcgi.vermont.gov/arcgis/rest/services/EGC_services/MAP_VCGI_LIDARCONTOURS_WM_CACHE_v1/MapServer)) and independently as an [Esri Vector Tile Service](https://tiles.arcgis.com/tiles/BkFxaEFNwHqX3tAw/arcgis/rest/services/VECTOR_VCGI_CN1TGEN_WM_v1/VectorTileServer) | **Two existing pipelines already, not derived from a shared export** — see [Gaps](#gaps--open-questions). No PMTiles equivalent exists yet. Styling currently done per-basemap in Esri's Vector Tile Style Editor (see the contour color work in [`../dem-color-ramps/11class-monochrome-canvas/`](../dem-color-ramps/11class-monochrome-canvas/README.md)) |
| Surface Waters | AGOL hosted feature layer | Waterbodies, waterlines |
| Base Land Cover | AGOL hosted feature layer | |
| Land Cover — Impervious Surfaces | AGOL hosted feature layer | |
| Land Cover — Tree Canopy | AGOL hosted feature layer | |
| Mountains and Hills | AGOL hosted feature layer | |
| Tree Centroids | *Available next year* | |
| Tree Canopy (next-gen) | *Available next year* | Presumably supersedes/complements Land Cover — Tree Canopy above; relationship between the two not yet clarified |
| Wetlands (VSWI) | AGOL hosted feature layer | Vermont Significant Wetland Inventory |

### E911 Board layers

| Layer | Current format/source |
|---|---|
| Private Driveways | AGOL hosted feature layer |
| Building Footprints | AGOL hosted feature layer |
| Cemeteries | AGOL hosted feature layer |
| Golf Course | AGOL hosted feature layer |
| Quarries / Mines | AGOL hosted feature layer |
| Trails | AGOL hosted feature layer |

### VCGI-maintained raster products

| Product | Current format/source | Notes |
|---|---|---|
| Bare Earth DEM | COG, S3 (`vtopendata-prd`) | QL1 lidar, hydro-flattened — the DEM this repo's color ramps are built for |
| Bare Earth Hillshade | COG, S3 | |
| DSM Hillshade | COG, S3 | Surface model (includes buildings/canopy), distinct from bare-earth hillshade |
| Best of Color Imagery | COG, S3 | |
| Time in Daylight | COG, S3 | |

## Gaps / open questions

Concrete follow-ups raised by comparing this inventory against the two
delivery pipelines above:

1. **Contours already have two independent pipelines** (ArcGIS Server
   cached MapServer + a separately-generated Esri Vector Tile Service),
   neither derived from a shared export, and no PMTiles version exists for
   open-source apps yet. This is the clearest live example of the
   single-source-of-truth problem the rest of VSDI will hit as the PMTiles
   pipeline comes online — worth deciding the contour pipeline first as a
   template for the rest.
2. **No single source-of-truth export defined yet** for the general case:
   as the PMTiles pipeline matures, each VSDI/E911 layer needs one
   canonical export (e.g., AGOL hosted feature layer → FlatGeobuf) that
   *both* the PMTiles build and any Esri Vector Tile Service/Package
   publishing step consume, rather than two pipelines independently
   reading from (and potentially drifting from) the source.
3. **Style authoring is one-directional.** Tooling exists to convert AGOL
   renderer JSON → MapLibre `style.json` (`arcgis-webmap.mjs`, the
   `arcgis-to-maplibre` skill), but not the reverse. If a basemap's visual
   design gets authored MapLibre-first (as the color ramp work in this
   repo effectively is), there's no automated path to an Esri Vector Tile
   Style Editor equivalent — that's being done by hand per-layer right
   now (e.g., the contour color work here).
4. **Transportation and place names have no open-source path.** The
   Esri-side answer is Living Atlas Human Geography (via the 6-month
   Community Maps contribution), which doesn't help a MapLibre-based
   basemap. These likely need their own VSDI → PMTiles pipeline,
   independent of the Community Maps cadence.
5. **Per-variant raster styling presets aren't defined yet.** TiTiler can
   serve arbitrary colormap/rescale per basemap variant (Light/Dark/
   Physical Geography) from the same COGs, but those presets need to be
   decided and captured (via `titiler-endpoint-generator`) so ArcGIS and
   open-source apps reference the same parameterized endpoint rather than
   independently-tuned copies.
6. **DEM delivery is intentionally split, document it as such:**
   TiTiler-COG (styled visual raster, cross-platform, used for the basemap
   itself) vs. the existing PMTiles-Terrarium tileset (encoded elevation
   values, open-source/MapLibre client-side use only — not usable in
   ArcGIS Online without custom decoding). Don't conflate these when
   deciding how a given basemap layer should be served.
