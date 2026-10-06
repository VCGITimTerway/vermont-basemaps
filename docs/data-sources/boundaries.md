# Administrative Boundaries (State / County / Municipal / Village)

## What is this data?

Administrative boundary lines and polygons at four levels: state, county,
municipal (town), and village. Lines for all four levels are published
together in one shared service; polygons are published per-level as
separate services (except municipal, where no dedicated polygon service
has been identified yet — see below).

## Stewardship

- **Maintained by:** TODO
- **Update cadence:** TODO — boundary changes are infrequent (annexation,
  incorporation) but the source should be re-checked periodically rather
  than assumed static
- **Last known update:** TODO

## Derivation

- **Input sources:** TODO
- **Methodology:** TODO — the "BNDHASH" naming convention across all of
  these services suggests a shared hash/versioning scheme tying the line
  and polygon products together; confirm what it actually tracks

## Use cases & limitations

- **Intended use cases:** Reference boundary lines/labels for basemaps at
  multiple zoom levels (state down to village).
- **Known limitations / caveats:** TODO
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
