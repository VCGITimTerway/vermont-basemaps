# Administrative Boundaries (State / County / Municipal / Village)

## What is this data?

Administrative boundary lines and polygons at four levels: state, county,
municipal (town), and village. Lines for all four levels are published
together in one shared service; polygons are published per-level as
separate services (except municipal, where no dedicated polygon service
has been identified yet — see below).

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
  boundaries alongside state/county/town/village.
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
| Municipal | Polygon | **Not identified yet** — only covered as lines via the shared service above | — |
| Village | Polygon | [AGOL hosted feature layer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Boundary_BNDHASH_poly_villages_SP_v1/FeatureServer/0) | EPSG:32145 (VT State Plane) |

**Format:** AGOL hosted feature layer throughout (uncached, queryable).

## Path to PMTiles / TiTiler output

- **Target format:** PMTiles (vector)
- **Pipeline steps:**
  1. Not yet started. Standard path once the tippecanoe pipeline is ready:
     export each service → FlatGeobuf/GeoJSON → tippecanoe → `.pmtiles`.
     Given these are naturally one thematic family (administrative
     boundaries at multiple levels), consider whether they should be one
     combined PMTiles tileset (multiple layers, one per level) or four
     separate tilesets — affects how basemap styles reference them.
  2. Resolve the missing Municipal polygon source before this layer can be
     included as a polygon fill in any basemap variant (it currently only
     exists as a line).
- **Known gaps / blockers:**
  - Municipal Boundaries polygon service not identified.
  - No PMTiles or parallel Esri Vector Tile Service built yet for any of
    these.

## Related

- Architecture doc row: [`../architecture/foundational-layers.md`](../architecture/foundational-layers.md#vsdi-vermont-spatial-data-infrastructure)
