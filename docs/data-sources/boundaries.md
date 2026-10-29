# Administrative Boundaries (State / County / Municipal / Village)

## What is this data?

Administrative boundary lines and polygons at four levels: state, county,
municipal (town), and village. Lines for all four levels are published
together in one shared service; polygons are published per-level as
separate services. Municipal Boundaries is also one of VCGI's Esri
Community Maps contributions (as "Admin3") — see below.

## Stewardship

- **Maintained by:** VCGI (process credited to Steve Sharp and others,
  per the metadata's lineage steps), reviewing records from the **VT
  State Archives, Secretary of State's Office**, with corrections welcomed
  from VGIS users.
- **Update cadence:** **Annual**, per the published metadata. Versioned
  (e.g. `2026A`) — a `UPDACT` field tracks what changed since the prior
  version and is reset each release.
- **Last known update:** 2026A (content date 2026-07-31).
- **Source:** [published FGDC metadata, `BoundaryOther_BNDHASH`](https://maps.vcgi.vermont.gov/gisdata/metadata/BoundaryOther_BNDHASH.htm)

## Derivation

- **Input sources:** "Best available" boundaries from multiple sources
  (tracked per-feature via `ARC_SRC`/`SRC_NOTES` attributes), integrated
  from the predecessor layer **TBHASH** (the master town boundary layer
  prior to BNDHASH).
- **Methodology:** Maintained as a single ESRI geodatabase feature dataset
  with shared topology rules across all levels, so village/town/county
  boundaries stay vertically integrated (a village boundary can't drift
  from its parent town boundary, etc.). "BNDHASH" itself isn't a
  processing method — it's the dataset name; the actual feature classes
  inside it are `BNDHASH_POLY_VILLAGES`, `BNDHASH_POLY_TOWNS`,
  `BNDHASH_POLY_COUNTIES`, `BNDHASH_POLY_RPCS` (**Regional Planning
  Commissions — a boundary level not in our original inventory, worth
  adding**), `BNDHASH_POLY_VTBND` (state), and `BNDHASH_LINE` (the shared
  line geometry all polygons are built from — this is the "All Lines"
  service in our inventory).

## Use cases & limitations

- **Intended use cases:** Reference boundary lines/labels for basemaps at
  multiple zoom levels (state down to village). Explicitly includes RPC
  boundaries alongside state/county/town/village. Confirmed in production
  use in both the **Base Topo** and **Base** Group Layer configurations
  (see [Related](#related) below): the State polygon service supplies a
  visible dashed-line state outline (not just the VT Mask's hole
  geometry — see [`human-geography-detail-blue-water/README.md`](../basemap-styles/human-geography-detail-blue-water/README.md)
  for that separate, mask-specific use), and the Municipal polygon
  service backs the reusable "Boundaries" Group Layer item (Town
  Boundaries, styled as a two-layer halo).
- **Known limitations / caveats:**
  - **Not a legally definitive boundary layer** — stated directly in the
    metadata: *"VCGI has NOT attempted to create a legally definitive
    boundary layer... BNDHASH should be used for general mapping purposes
    only."* Ultimate authority rests with the Secretary of State's Office
    and the VT Legislature.
  - Based on municipality/county/village lists from a 2000 Secretary of
    State publication, with endorsed legislative changes (e.g. village
    mergers) folded in since — not a live feed from that source.
- **Appropriate scale / zoom range:** Varies by level — state boundary
  relevant at statewide zoom, village boundaries only at large scale.

## Current source

All services below confirmed via direct query of each `FeatureServer`'s
`spatialReference` (not inferred from the `_SP_` naming alone, though it
matches).

| Level | Geometry | Service | Projection |
|---|---|---|---|
| All levels (shared) | Line | [AGOL hosted feature layer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Boundary_BNDHASH_line_SP_v1/FeatureServer/0) ("VT Data – Boundaries, All Lines") | EPSG:32145 (VT State Plane) |
| State | Polygon | [AGOL hosted feature layer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/ArcGIS/rest/services/FS_VCGI_OPENDATA_Boundary_BNDHASH_poly_vtbnd_SP_v1/FeatureServer/0) | EPSG:32145 (VT State Plane) |
| County | Polygon | [AGOL hosted feature layer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Boundary_BNDHASH_poly_counties_SP_v1/FeatureServer/0) | EPSG:32145 (VT State Plane) |
| Municipal | Polygon | [AGOL hosted feature layer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/ArcGIS/rest/services/FS_VCGI_OPENDATA_Boundary_BNDHASH_poly_towns_SP_v1/FeatureServer/0), label field `TOWNNAMEMC` | EPSG:32145 (VT State Plane) |
| Village | Polygon | [AGOL hosted feature layer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Boundary_BNDHASH_poly_villages_SP_v1/FeatureServer/0) | EPSG:32145 (VT State Plane) |

**Format:** AGOL hosted feature layer throughout (uncached, queryable).

### Esri Community Maps contribution (Admin3)

Municipal Boundaries feeds Esri's Community Maps program as "Admin3":
all features from the Municipal service above submitted, no filter,
labeled via `TOWNNAMEMC`. Part of VCGI's broader Community Maps
contribution — see
[`../architecture/foundational-layers.md`](../architecture/foundational-layers.md#esri-community-maps-separate-existing-pipeline)
for the full list of layers VCGI contributes and the shared 6-month pull
cadence.

## Path to PMTiles / TiTiler output

- **Target format:** PMTiles (vector)
- **Pipeline steps:**
  1. Not yet started. Standard path once the tippecanoe pipeline is ready:
     export each service → FlatGeobuf/GeoJSON → tippecanoe → `.pmtiles`.
     Given these are naturally one thematic family (administrative
     boundaries at multiple levels), consider whether they should be one
     combined PMTiles tileset (multiple layers, one per level) or four
     separate tilesets — affects how basemap styles reference them.
- **Known gaps / blockers:** No PMTiles or parallel Esri Vector Tile
  Service built yet for any of these.

## Related

- Architecture doc row: [`../architecture/foundational-layers.md`](../architecture/foundational-layers.md#vsdi-vermont-spatial-data-infrastructure)
- [`../webmap-tests/README.md#reusable-group-layers`](../webmap-tests/README.md#reusable-group-layers) —
  Municipal boundaries are packaged as the reusable **Boundaries** Group
  Layer item (dotted-line + white-halo pair with scale-dependent width),
  shared across the Base Topo and Base configurations ([Test 02b](../webmap-tests/topographic-test-02b-world-terrain-labels/README.md),
  [Test 02c](../webmap-tests/topographic-test-02c-admin/README.md),
  [Test 02d](../webmap-tests/topographic-test-02d-base/README.md)) —
  Test 02c was the first to use it, before it was saved as a standalone
  item
- State Boundary's dashed-line use in Base Topo/Base: see each test's
  "Base Topo group" / "Base group" layer table (e.g.
  [Test 02b](../webmap-tests/topographic-test-02b-world-terrain-labels/README.md#base-topo-group))
