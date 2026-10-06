# Parcels

## What is this data?

Statewide parcel (cadastral) polygons — the property/ownership boundary
layer. Split into **active** and **inactive** parcels within the same
service (inactive presumably meaning superseded/retired parcel records
rather than deleted, but TODO: confirm the actual active/inactive
definition and how a parcel transitions between them).

## Stewardship

- **Maintained by:** VCGI, compiling/standardizing data sourced from
  Vermont municipalities, Vermont licensed land surveyors, and the
  Vermont Department of Taxes (Grand List).
- **Update cadence:** **Weekly** (statewide), per the published metadata
  — "Vermont GIS Parcel Data is generally updated weekly." Note the
  *content* currency still varies by municipality (some towns' underlying
  parcel geometry/attribution is much more current than others — the
  weekly cadence is about republishing, not about how recently each town
  resurveyed).
- **Last known update:** Ongoing (weekly); program began 2018-01-24
  (first statewide load), Grand List join automation added 2018-10-02.
- **Source:** [published metadata, `CadastralParcels_VTPARCELS`](https://maps.vcgi.vermont.gov/gisdata/metadata/CadastralParcels_VTPARCELS.htm)
  (an ISO/ArcGIS-item-style metadata record, not the older FGDC format
  used for the lidar products above)

## Derivation

- **Input sources:** Individual municipality-submitted parcel datasets
  (via the Statewide Property Parcel Mapping Program), joined to Grand
  List records from the VT Department of Taxes by SPAN (Span Parcel
  Account Number).
- **Methodology:**
  1. Municipalities submit parcel geometry conforming to the **Vermont
     GIS Parcel Data Standard 2.3**.
  2. VCGI standardizes/loads these into one statewide feature class
     (`Cadastral_VTPARCELS_poly_standardized_parcels` for active,
     `..._standardized_inactive` for inactive).
  3. Grand List data (ownership, SPAN, assessment info) is joined via an
     intersection/reconciliation table matching active SPAN numbers.
  4. The published **Active** layer is a *value-added join product* — it
     includes not just land parcels but unlanded buildings, public
     rights-of-way, trail rights-of-way (from VTrans Town Highway Maps),
     and surface water areas that serve as property boundaries.

## Use cases & limitations

- **Intended use cases:** Parcel boundary reference layer for basemaps;
  attribute lookups (owner, SPAN parcel ID) for property-related
  applications. Explicitly **not** a survey product (see below).
- **Known limitations / caveats:**
  - **"This data layer is not a legal survey. It is not a legal
    conveyance or description of property and is intended for planning
    purposes only."** — stated directly in the metadata; don't let this
    caveat get lost if parcels are surfaced as an authoritative-looking
    basemap layer.
  - **Stacked-polygon effect:** where a one-to-many relationship exists
    between land and Grand List records (e.g., a parcel with 15 mobile
    homes as separate taxable records), the layer includes one polygon
    *per Grand List record*, all with identical geometry stacked on top
    of each other. An identify/click on such a parcel returns many
    overlapping identical-shaped features, not one — matters for any
    click/hover interaction built against this layer, and for rendering
    performance if fills are even slightly transparent (stacked
    translucent fills darken).
  - Positional accuracy inherently varies by source municipality (not
    independently quantified statewide in the metadata reviewed here).
- **Appropriate scale / zoom range:** Large-scale/high-zoom only — parcel
  boundaries are not meaningful at statewide zoom levels.

## Current source

- **Service (active):** [AGOL hosted feature layer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/ArcGIS/rest/services/FS_VCGI_VTPARCELS_WM_NOCACHE_v2/FeatureServer/1)
- **Service (inactive):** [AGOL hosted feature layer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/ArcGIS/rest/services/FS_VCGI_VTPARCELS_WM_NOCACHE_v2/FeatureServer/0)
  (same service, different layer ID)
- **Format:** AGOL hosted feature layer (uncached, queryable)
- **Projection (EPSG):** EPSG:3857 (Web Mercator), confirmed
- **Geometry type:** Polygon
- **Known fields** (from an earlier PMTiles prototype, `parcels.pmtiles`):
  `OBJECTID`, `OWNER1`, `OWNER2`, `SPAN` (parcel ID), `id` — confirm this
  field list is still current against the live service, not just the
  prototype tileset.

## Path to PMTiles / TiTiler output

- **Target format:** PMTiles (vector)
- **Pipeline steps:**
  1. A proof-of-concept already exists:
     `vtopendata-dev/_SANDBOX/vt-parcels-wgs84-fixed.pmtiles` and a second
     prototype at `_Other/pmtile-test/parcels.pmtiles` (per
     [`VCGI/pmtiles`](https://github.com/VCGI/pmtiles)'s README example).
     Treat these as **prototypes, not the production pipeline** — confirm
     whether they were built from the FeatureServer above and whether
     they include both active and inactive parcels or just one.
  2. Production path once the AWS-hosted tippecanoe pipeline (in
     development, see
     [`../architecture/foundational-layers.md`](../architecture/foundational-layers.md#vector--pmtiles--parallel-esri-vector-tiles))
     is ready: export both layer IDs (1 = active, 0 = inactive) →
     FlatGeobuf/GeoJSON → tippecanoe → `.pmtiles`.
- **Known gaps / blockers:**
  - No confirmed single source-of-truth export process yet (architecture
    doc gap #2) — the existing prototypes may or may not reflect what the
    eventual production pipeline will do.
  - Parallel Esri Vector Tile Service (for ArcGIS-centric apps) not yet
    built for parcels — only the PMTiles side has a prototype so far.
  - Style for parcels (fill/outline per active vs. inactive) not yet
    authored in either MapLibre or Esri Vector Tile Style Editor form.

## Related

- Architecture doc row: [`../architecture/foundational-layers.md`](../architecture/foundational-layers.md#vsdi-vermont-spatial-data-infrastructure)
- [`VCGI/pmtiles`](https://github.com/VCGI/pmtiles) README documents the
  existing parcels PMTiles prototype and the ArcGIS Online vector tile
  layer consumption pattern in detail.
