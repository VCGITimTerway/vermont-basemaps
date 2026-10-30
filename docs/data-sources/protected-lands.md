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
  from the same source. Also one of VCGI's Esri Community Maps
  contributions (four separate categories pulled from this one service —
  see below).
- **Known limitations / caveats:** Subtype fields confirmed for 4 of the
  8+ subtypes (see below, via VCGI's Community Maps contribution config)
  — national wildlife refuges, national wilderness areas, municipal
  parks, municipal forests, and the Military Sites filter itself are
  still unconfirmed.
- **Appropriate scale / zoom range:** TODO

### Subtype values (confirmed via Community Maps contribution)

Field names/values VCGI uses to filter this service into four of its
Esri Community Maps layers (see
[`../architecture/foundational-layers.md`](../architecture/foundational-layers.md#esri-community-maps-separate-existing-pipeline)):

| Subtype | Filter |
|---|---|
| National Forest | `PAGENCY1 = '2000032000'` |
| National Park | `PAGENCY1 = '2000031100' AND NAME LIKE '%Park'` |
| State Forest | `DESIGNAT = 'SF'` |
| State Park | `DESIGNAT = 'SP'` |

Label field for all four: `NAME`. The remaining subtypes (national
wildlife refuges, national wilderness areas, municipal parks, municipal
forests) and the Military Sites filter aren't part of the Community Maps
config, so their field values are still unconfirmed.

### Ownership-type filter (confirmed via the Base Topo/Base configuration)

Separate from the four Community Maps subtype filters above, `INT_ORGTYP`
is a confirmed field distinguishing managing-agency type, with coded
values rather than spelled-out text. [Test
02b](../webmap-tests/topographic-test-02b-world-terrain-labels/README.md)
filters this service to `INT_ORGTYP = 'STAT' OR INT_ORGTYP = 'LOC' OR
INT_ORGTYP = 'FED'` to show only publicly stewarded protected land
(State/Municipal/Federal), excluding privately held conservation parcels.
Test 02b's current configuration additionally OR's in several `DESIGNAT`
values (`SF`, `SP`, `ML`, `MF`, `MP`, `SL`) alongside the ownership-type
clause — see [Test 02b's layer
table](../webmap-tests/topographic-test-02b-world-terrain-labels/README.md)
for the exact expression in use there.

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
- **Known fields:** `NAME`, `DESIGNAT`, `PAGENCY1` (subtype filters, above),
  `INT_ORGTYP` (ownership-type filter, above; coded values `STAT`, `LOC`,
  `FED`, not spelled-out text)

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
- **Known gaps / blockers:** Subtype fields known for National/State
  Forest/Park (see above); still need the Military Sites filter and the
  remaining subtypes' fields before a complete filtered style/export can
  be built.

## Related

- Architecture doc row: [`../architecture/foundational-layers.md`](../architecture/foundational-layers.md#vsdi-vermont-spatial-data-infrastructure)
- [`../webmap-tests/README.md#reusable-group-layers`](../webmap-tests/README.md#reusable-group-layers) —
  this layer is part of the shared **Base Topo**/**Base** Group Layer
  composition (not itself a standalone Group Layer item), so it's
  carried into every web map that references either group
