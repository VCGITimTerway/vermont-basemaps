# Parcels

## What is this data?

Statewide parcel (cadastral) polygons — the property/ownership boundary
layer. Split into **active** and **inactive** parcels within the same
service (inactive presumably meaning superseded/retired parcel records
rather than deleted, but TODO: confirm the actual active/inactive
definition and how a parcel transitions between them).

## Stewardship

- **Maintained by:** TODO — likely assembled from municipal/town-level
  submissions rather than surveyed directly by VCGI; confirm the actual
  aggregation process
- **Update cadence:** TODO
- **Last known update:** TODO

## Derivation

- **Input sources:** TODO — presumably town/municipal grand list or
  cadastral submissions, standardized statewide
- **Methodology:** TODO — standardization/conflation process from
  municipal sources into one statewide schema

## Use cases & limitations

- **Intended use cases:** Parcel boundary reference layer for basemaps;
  attribute lookups (owner, SPAN parcel ID) for property-related
  applications.
- **Known limitations / caveats:** TODO — positional accuracy varies
  significantly by source municipality for cadastral data in general;
  confirm whether that caveat applies here and how it's communicated to
  users
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
