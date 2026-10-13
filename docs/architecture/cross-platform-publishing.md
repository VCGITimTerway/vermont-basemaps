# Cross-Platform Publishing: Topographic Test 01 Layers

For each layer currently in
[Topographic — Test 01](../webmap-tests/topographic-test-01-styled-dem/README.md),
what it would actually take to get it serving cleanly on **both** ArcGIS
(Map Viewer, Experience Builder) and open-source (MapLibre/Leaflet) apps,
given where it's published today. Companion to
[`foundational-layers.md`](foundational-layers.md), which covers the
architecture generally — this is the concrete, per-layer punch list.

## Correction worth making before the table: the "no popup" limitation isn't a PMTiles thing

You flagged that PMTiles vector tiles seem to offer the same
functionality as Esri vector tiles in Map Viewer — rendering without
popup/attribute access. That's accurate **for how ArcGIS Online's Vector
Tile Layer item type behaves**, whether it's backed by a native Esri
Vector Tile Service or by a PMTiles tileset referenced via a `style.json`
(same pattern as the contour and Human Geography Detail styles in this
repo) — Map Viewer's Vector Tile Layer is built for fast cartographic
background rendering, not feature query, regardless of what's behind it.

It is **not** a limitation of PMTiles or the MVT format itself. A MapLibre
GL JS app (the open-source side) consuming the exact same PMTiles tileset
can absolutely support click-to-popup, via
[`map.queryRenderedFeatures()`](https://maplibre.org/maplibre-gl-js/docs/API/classes/Map/#queryrenderedfeatures) —
MVT tiles carry real per-feature attributes, and MapLibre exposes them.
So the practical implication is:

- **One shared PMTiles tileset genuinely can serve both platforms** for
  layers that don't need popups in Map Viewer either (most basemap
  background layers — contours, hydrography lines, place-name labels,
  building footprints as cartographic context). This is the opportunity
  you're pointing at, and it's real: resolves the "two independent
  pipelines" problem flagged as gap #1 in `foundational-layers.md`,
  not just for contours but for every VCGI-owned background layer.
- **For layers where Esri users specifically need click-for-attributes**
  (the E911 interest layers, Wetlands — anything currently published as
  an AGOL hosted *feature* layer, not a vector *tile* layer, for exactly
  this reason), that requirement doesn't go away just because a PMTiles
  version also exists. Keep the Feature Service for Esri; the PMTiles
  tileset becomes the open-source side's rendering *and* popup source
  (via `queryRenderedFeatures`), rather than needing its own separate
  interactive mechanism.

## Per-layer status

**Legend:** ✅ done/working · 🔧 straightforward, not yet built · 🚧 blocked · — not applicable to this layer

| Layer | Currently published as | ArcGIS | Open-source (PMTiles/TiTiler) | Notes |
|---|---|---|---|---|
| Lidar DEM Hillshade | ArcGIS cached ImageServer ([`IMG_VCGI_LIDARHILLSHD_WM_CACHE_v1`](../data-sources/hillshade-bare-earth.md)) | ✅ | ✅ (TiTiler, same COG) | Raster — TiTiler is already *the* shared single pipeline here, same role PMTiles would play for vector. No work needed on either side |
| 2023 QL1 DEM — TiTiler styled | Same COG via TiTiler | ✅ | ✅ (TiTiler) | Already the proof-of-concept for "one raster pipeline, two consumers" — cite this as the working precedent |
| Alpine Trails (E911) | [AGOL hosted FeatureServer](../data-sources/README.md), shared `FOOTPRINTTYPE`-coded service | ✅ | 🔧 | `capabilities: Query,Extract` confirmed — standard export → tippecanoe → PMTiles pipeline is unblocked. Keep the Feature Service for Esri popups; PMTiles + `queryRenderedFeatures` gives open-source equivalent popups from the same export |
| Golf Courses (E911) | Same shared FOOTPRINTS service, `FOOTPRINTTYPE = G1` | ✅ | 🔧 | Same export as Alpine Trails covers this — one tippecanoe run against the whole service, filtered client-side by `FOOTPRINTTYPE`, not three separate exports |
| Quarries (E911) | Same shared FOOTPRINTS service, `FOOTPRINTTYPE = Q1` | ✅ | 🔧 | Same as above |
| 1ft Lidar Contours (Dark Olive) | Esri Vector Tile Service (`VECTOR_VCGI_CN1TGEN_WM_v1`) | ✅ | 🚧 **blocked** | Confirmed no queryable feature-service backing exists for this data (see [`contours-1ft.md`](../data-sources/contours-1ft.md#current-source)) — can't export what isn't queryable. **This is the one to raise with your colleague**: either expose a queryable source behind the existing tile service, or confirm the original feature class used to generate it and export from there directly |
| Human Geography Detail — Blue Water | Esri Living Atlas (`World_Basemap_v2`), customized copy in [`basemap-styles/`](../basemap-styles/human-geography-detail-blue-water/README.md) | ✅ | 🚧 **not VCGI's data** | Can't "convert" licensed Esri content to PMTiles. Open-source equivalent requires sourcing VCGI's *own* hydrography (Surface Waters/VHDCARTO) via a new pipeline — the "tricky" layer you said you'd follow up on separately in [`data-sources/README.md`](../data-sources/README.md) |
| Vermont Significant Wetlands Inventory | [ANR-hosted FeatureServer](https://services5.arcgis.com/Uzks6LSde6r23wwG/arcgis/rest/services/Vermont_Significant_Wetland_Inventory/FeatureServer/0), different org than VCGI's | ✅ | 🔧, pending a confirmation | Technically exportable (standard FeatureServer), but it's ANR's service, not VCGI's — confirm data-sharing/redistribution terms with ANR before building a PMTiles export, not just a technical question |
| Buildings 2022 | Esri Living Atlas vector tile | ✅ | 🚧 **not VCGI's data, source unclear** | Same licensing issue as Blue Water. Candidate VCGI sources: `LandLandcov_Buildings2016`/`2022` (metadata records exist, not yet opened — see [`data-sources/README.md`](../data-sources/README.md)) — **not** the shared E911 FOOTPRINTS service as I'd guessed; that service's schema defines a `Building`/`B1` `FOOTPRINTTYPE` code, but a quick scan of live data didn't surface any `B1` records, so that connection is unconfirmed, not disproven |
| E911 Alpine Ski Lifts | [AGOL hosted FeatureServer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Emergency_ALPINELIFTS_line_SP_v1/FeatureServer/0) | ✅ | 🔧 | `capabilities: Query,Extract` confirmed — standard pipeline |
| VT Mask (GeoJSON) | [This repo](../basemap-styles/human-geography-detail-blue-water/vermont-mask.geojson), served via GitHub Pages | ✅ | ✅ | Already cross-platform — added via "Add Layer from URL" in Map Viewer, and directly fetchable by any open-source map. No further work |
| Human Geography Label | Esri Living Atlas vector tile | ✅ | 🚧 **not VCGI's data** | Same issue as Blue Water/Buildings. Candidate VCGI source for place names generally: `BasemapLandmarks_GEONAME` (metadata record identified, not yet opened) |
| Mountains and Hills | [ArcGIS MapServer sublayer](https://maps.vcgi.vermont.gov/arcgis/rest/services/VCGI_services/VCGI_BASEMAP_WM_v2/MapServer/4) | ✅ | 🔧 | `capabilities: Map,Query,Data` confirmed — exportable despite being a classic MapServer sublayer rather than a modern hosted feature layer |
| Lake and Pond Labels | [ArcGIS MapServer sublayer](https://maps.vcgi.vermont.gov/arcgis/rest/services/VCGI_services/VCGI_BASEMAP_WM_CACHE_v2/MapServer/25) | ✅ | 🔧 | Despite "CACHE" in the service name (the rendered map image is pre-cached — `singleFusedMapCache: true`), the sublayer itself still reports `capabilities: Map,Query,Data` — confirmed queryable, export is unblocked. This is a real, VCGI-sourced alternative to Esri's place-name labels — directly useful for the gap #4 open-source labels problem |
| River and Stream Names | [ArcGIS MapServer sublayer](https://maps.vcgi.vermont.gov/arcgis/rest/services/VCGI_services/VCGI_BASEMAP_WM_CACHE_v2/MapServer/30) | ✅ | 🔧 | Same service family and same confirmed queryability as Lake and Pond Labels |

## What this changes about the existing gaps

- **Gap #1 (contours' two independent pipelines)** stays blocked on the
  same thing as before — a queryable source — but the fix is now clearer:
  once your colleague identifies or exposes one, the *same* export feeds
  both an Esri-side refresh and a new PMTiles tileset, rather than
  maintaining two authored-separately pipelines going forward.
- **Gap #2 (no confirmed source-of-truth export pattern)** has a working
  answer for every layer marked 🔧 above: AGOL/ArcGIS Server feature
  query → FlatGeobuf/GeoJSON → tippecanoe → PMTiles, with the *same*
  export also usable to keep an Esri Vector Tile Service in sync if one's
  wanted, instead of hand-authoring two.
- **Gap #4 (no open-source equivalent for transportation/place names)**
  now has concrete, identified VCGI-sourced candidates instead of being
  purely theoretical: Lake/Pond Labels and River/Stream Names are
  confirmed queryable today; `BasemapLandmarks_GEONAME` is an identified
  but unopened candidate for general place names.

## Suggested next steps, roughly in order

1. Raise the contour source-of-truth question with your colleague — the
   one genuinely blocked item, and worth settling first since it'll
   likely inform how the others get built (shared tooling/conventions).
2. Confirm ANR's data-sharing terms for VSWI before building anything
   against it, even though it's technically exportable.
3. Open `LandLandcov_Buildings2016`/`2022` and `BasemapLandmarks_GEONAME`
   metadata to confirm they're the right VCGI sources for buildings and
   place names, respectively (same approach used for the DEM/hillshade/
   contours/parcels/boundaries profiles already done in
   [`data-sources/`](../data-sources/README.md)).
4. Pick one 🔧 layer (Alpine Ski Lifts or Mountains and Hills are
   simplest — single-purpose services, no shared-service filtering
   needed) to build as the first real export → tippecanoe → PMTiles run,
   proving out the pipeline end-to-end before doing the rest.
