# Surface Waters (Waterbodies, Waterlines)

## What is this data?

Vermont's cartographic hydrography — waterbody polygons (lakes, ponds)
and waterlines (rivers, streams, canals/ditches) — published from the
Vermont Hydrography Dataset, Cartographic variant (VHDCARTO). Feeds
Esri's Community Maps program directly (see below), and is the open-source
sourcing answer for the "Human Geography Detail — Blue Water" and "World
Terrain Reference Labels" layers used in this repo's webmap tests (both
of which are Esri Living Atlas content, not VCGI's own — see
[`../architecture/foundational-layers.md`](../architecture/foundational-layers.md#esri-community-maps-separate-existing-pipeline)).

## Stewardship

- **Maintained by:** TODO
- **Update cadence:** TODO (VCGI's Community Maps contribution pulls it
  every 6 months, but that's a consumption cadence, not necessarily this
  dataset's own update cadence)
- **Last known update:** TODO

## Derivation

- **Input sources:** TODO — presumably built from/aligned to the National
  Hydrography Dataset (NHD) given the `GNIS_NAME` field (NHD's standard
  name attribute) and "VHD" naming convention, but not confirmed
- **Methodology:** TODO

## Use cases & limitations

- **Intended use cases:** Cartographic water-feature rendering and
  labeling for basemaps; feeds Esri Community Maps' Waterbody/Waterline
  layers.
- **Known limitations / caveats:** TODO
- **Appropriate scale / zoom range:** TODO

## Current source

| | Waterbody | Waterline |
|---|---|---|
| **Service** | [`FS_VCGI_OPENDATA_Water_VHDCARTO_poly_SP_v1`](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/ArcGIS/rest/services/FS_VCGI_OPENDATA_Water_VHDCARTO_poly_SP_v1/FeatureServer/0) | [`FS_VCGI_OPENDATA_Water_VHDCARTO_line_SP_v1`](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/ArcGIS/rest/services/FS_VCGI_OPENDATA_Water_VHDCARTO_line_SP_v1/FeatureServer/0) |
| **Format** | AGOL hosted feature layer, `capabilities: Query,Extract` | Same |
| **Projection (EPSG)** | EPSG:32145 (VT State Plane), confirmed | Same |
| **Geometry type** | Polygon | Line |

## Esri Community Maps contribution

Both services feed Esri's Community Maps program directly:

| Community Maps layer | Source | Filter | Label field |
|---|---|---|---|
| Waterbody | Waterbody service above | `FTYPE = 'LakePond'` (LakePond) / `FTYPE = 'StreamRiver'` (RiverStream) | `GNIS_NAME` |
| Waterline | Waterline service above | `FCODE = 33600` (CanalDitch) / `FTYPE = 'StreamRiver' AND (FCODE = 46006 OR FCODE = 46000)` (RiverStream) / `FTYPE = 'StreamRiver' AND FCODE = 46003` (RiverStreamIntermit) | `GNIS_NAME` |

Part of VCGI's broader Community Maps contribution — see
[`../architecture/foundational-layers.md`](../architecture/foundational-layers.md#esri-community-maps-separate-existing-pipeline)
for the full list of layers VCGI contributes and the shared 6-month pull
cadence.

## Path to PMTiles / TiTiler output

- **Target format:** PMTiles (vector)
- **Pipeline steps:**
  1. Not yet started. Standard path: export each service → FlatGeobuf/
     GeoJSON → tippecanoe → `.pmtiles`. The `FTYPE`/`FCODE` categories
     used for the Community Maps filters above are a reasonable starting
     point for styling (e.g. distinguishing lakes/ponds from rivers, or
     canals from natural streams) if useful for an open-source basemap
     too.
- **Known gaps / blockers:** No PMTiles or parallel Esri Vector Tile
  Service built yet.

## Related

- [`../architecture/foundational-layers.md`](../architecture/foundational-layers.md#esri-community-maps-separate-existing-pipeline)
- [`../architecture/cross-platform-publishing.md`](../architecture/cross-platform-publishing.md) —
  Human Geography Detail — Blue Water / World Terrain Reference Labels
  rows reference this as their open-source sourcing path
