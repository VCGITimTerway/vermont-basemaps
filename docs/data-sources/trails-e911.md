# Trails (E911)

## What is this data?

General-purpose trail lines (hiking, multi-use, etc.) from E911's
emergency-response mapping data. **Distinct from "Alpine Trails"** used
elsewhere in this repo's webmap tests — that one is a polygon subtype
(`FOOTPRINTTYPE` codes T1–T6) within the shared E911 FOOTPRINTS service,
specifically alpine/ski trails and glades. This is a separate, dedicated
line service covering trails more broadly. Don't conflate the two.

## Stewardship

- **Maintained by:** TODO (E911 board, per the service's naming
  convention — same board referenced for the FOOTPRINTS/ALPINELIFTS
  services elsewhere in this repo)
- **Update cadence:** TODO
- **Last known update:** TODO

## Derivation

- **Input sources:** TODO
- **Methodology:** TODO

## Use cases & limitations

- **Intended use cases:** Trail reference layer for basemaps; feeds Esri
  Community Maps' Trail layer (see below).
- **Known limitations / caveats:** `VISIBLE` field suggests some trails
  are flagged not-for-public-display (confirm meaning/values before
  assuming all records should render); `TRAILTYPE` T7/T8 are explicitly
  excluded from the Community Maps contribution (meaning unconfirmed).
- **Appropriate scale / zoom range:** TODO

## Current source

- **Service:** [`FS_VCGI_OPENDATA_Emergency_TRAILS_line_SP_v1`](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/ArcGIS/rest/services/FS_VCGI_OPENDATA_Emergency_TRAILS_line_SP_v1/FeatureServer/0)
- **Format:** AGOL hosted feature layer, `capabilities: Query,Extract`
- **Projection (EPSG):** EPSG:32145 (VT State Plane), confirmed
- **Geometry type:** Line
- **Fields:** `TRAILNAME`, `TRAILTYPE`, `SOURCE`, `TOWNNAME`, `COUNTY`,
  `STATE`, `TRAILMANAGEMENT`, `TRAILRATING`, `SURFACE`, `TRAILSYSTEM`,
  `VISIBLE`, `ACTUALMILES`, `ARCMILES`, `TechnicalRescue`

## Esri Community Maps contribution

Feeds Esri's Community Maps program as "Trail": all features except
`TRAILTYPE` T7/T8, labeled via `TRAILNAME`. Part of VCGI's broader
Community Maps contribution — see
[`../architecture/foundational-layers.md`](../architecture/foundational-layers.md#esri-community-maps-separate-existing-pipeline)
for the full list of layers VCGI contributes and the shared 6-month pull
cadence.

## Path to PMTiles / TiTiler output

- **Target format:** PMTiles (vector)
- **Pipeline steps:**
  1. Not yet started. Standard path: export → FlatGeobuf/GeoJSON →
     tippecanoe → `.pmtiles`.
- **Known gaps / blockers:** No PMTiles or parallel Esri Vector Tile
  Service built yet.

## Related

- [`../architecture/foundational-layers.md`](../architecture/foundational-layers.md#esri-community-maps-separate-existing-pipeline)
