# Protected Lands / Military Sites

## What is this data?

Polygons for publicly/conservation-protected land across Vermont, spanning
multiple subtypes: state parks, state forests, national parks, national
forests, national wildlife refuges, national wilderness areas, municipal
parks, and municipal forests. **Military Sites** is not a separate
dataset — it's a filtered view of this same service (presumably by a
category/subtype attribute), so it shares every field below except its own
filter definition.

## Stewardship

- **Maintained by:** TODO
- **Update cadence:** TODO
- **Last known update:** TODO

## Derivation

- **Input sources:** TODO — likely aggregated from multiple managing
  agencies (state, federal, municipal) given the subtype list; confirm
  how conflicts/overlaps between agency sources are resolved
- **Methodology:** TODO

## Use cases & limitations

- **Intended use cases:** Protected-lands context layer for basemaps;
  Military Sites as a specific point of interest/caution layer, filtered
  from the same source.
- **Known limitations / caveats:** TODO — confirm the exact attribute
  field and values used to distinguish subtypes (including Military
  Sites), since that's what any derived PMTiles/Esri style would need to
  filter on
- **Appropriate scale / zoom range:** TODO

## Current source

- **Service:** [AGOL hosted feature layer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Cadastral_PROTECTEDLND_poly_SP_v2/FeatureServer/0)
  (same service/URL for both Protected Lands and the Military Sites
  filtered subset)
- **Format:** AGOL hosted feature layer (uncached, queryable)
- **Projection (EPSG):** EPSG:32145 (VT State Plane), confirmed
- **Geometry type:** Polygon
- **Subtypes represented:** state parks, state forests, national parks,
  national forests, national wildlife refuges, national wilderness areas,
  municipal parks, municipal forests (field name/values for these subtypes
  and for the Military Sites filter: TODO)

## Path to PMTiles / TiTiler output

- **Target format:** PMTiles (vector)
- **Pipeline steps:**
  1. Not yet started. Standard path: export → FlatGeobuf/GeoJSON →
     tippecanoe → `.pmtiles`.
  2. Decide whether Military Sites ships as its own PMTiles layer (derived
     via an attribute filter during export) or whether basemap styles
     just filter the combined Protected Lands tileset client-side by the
     same attribute — avoids maintaining two parallel exports of what's
     really one dataset.
- **Known gaps / blockers:** Need the subtype/category field name and its
  values (including whatever distinguishes Military Sites) before a
  filtered style or a filtered export can be built correctly.

## Related

- Architecture doc row: [`../architecture/foundational-layers.md`](../architecture/foundational-layers.md#vsdi-vermont-spatial-data-infrastructure)
