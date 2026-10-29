# Topographic — Test 02d (Physical Topo Light Base)

Pulled directly from the web map's JSON via the AGOL sharing REST API,
not hand-described — re-pull if this map changes rather than editing
this table by hand.

**Live embed:** <https://vcgitimterway.github.io/vermont-basemaps/webmap-tests/topographic-test-02d-base/>
**ArcGIS Online item:** <https://vcgi.maps.arcgis.com/apps/mapviewer/index.html?webmap=5e5d8a7a2bb54ca791271c7050f6e29d>
**AGOL item title:** "Basemap 2026 - Topographic - Test 02d Physical Topo Light Base"
**Test extent:** centered roughly -72.44, 43.90 at a statewide view

Reference example for the **Base** Group Layer configuration — the
counterpart to [Test 02b](../topographic-test-02b-world-terrain-labels/README.md),
which references **Base Topo**. The only difference between the two
configurations: Base Topo includes the Lidar DEM Hillshade layer, Base
does not.

## Basemap

Same as Test 02/02b: **Human Geography Map** (Esri Living Atlas), own
"Human Geography Base" vector tile sub-layer turned **off**.

## Layer groups

Three groups, all saved, public **Group layer items**:

| Group | Item ID | Notes |
|---|---|---|
| Base | `1a119fb231ac4e8985346ddcc438692f` ("VT Basemap 2026 Base") | Same composition as [Base Topo](../topographic-test-02b-world-terrain-labels/README.md#base-topo-group) minus the Lidar DEM Hillshade layer — see below |
| Boundaries | `78853d8236e04a1d8d6df5c0f94e7c13` ("Group Layer - Town Boundaries") | Same item reused from Test 02b/02c |
| Labels | `0ff87dab7daf4141a5e95a2f8be0715e` ("VT Basemap 2026 Labels") | Same item reused from Test 02b |

## Layers shown (top to bottom within each group, as returned by the API)

### Base group

| # | Layer | Source | On? | Opacity | Notes |
|---|---|---|---|---|---|
| 0 | Vermont Protected Lands Database | [AGOL hosted FeatureServer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Cadastral_PROTECTEDLND_poly_SP_v2/FeatureServer/0) | On | 0.25 | Filtered to `INT_ORGTYP` = `STAT`/`LOC`/`FED` **or** `DESIGNAT` = `SF`/`SP`/`ML`/`MF`/`MP`/`SL` — see [`protected-lands.md`](../../data-sources/protected-lands.md) |
| 1 | Alpine Trails — VT E911 Other Mapped Features of Interest | [shared FeatureServer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Emergency_FOOTPRINTS_poly_SP_v1/FeatureServer/0) | On | 0.67 | |
| 2 | Golf Courses — VT E911 Other Mapped Features of Interest | same FeatureServer | On | 0.75 | |
| 3 | Quarries — VT E911 Other Mapped Features of Interest | same FeatureServer | On | 0.41 | |
| 4 | 1ft Lidar Contours — "COPY - Dark Olive" | Vector tile (Esri VT style copy) | On | 0.25 | |
| 5 | Human Geography Detail — Blue Water Light Roads | Esri Living Atlas vector tile, VCGI-styled ("Light Roads" style variant) | Off | — | |
| 6 | Vermont Significant Wetlands Inventory | [AGOL hosted feature layer](https://services5.arcgis.com/Uzks6LSde6r23wwG/arcgis/rest/services/Vermont_Significant_Wetland_Inventory/FeatureServer/0) | Off | 0.75 | |
| 7 | Buildings 2022 (White) | Vector tile ("White" style variant) | Off | — | Scale range 1:25,617–1:153 when on |
| 8 | VT Data — E911 Alpine Ski Lifts | [AGOL hosted feature layer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Emergency_ALPINELIFTS_line_SP_v1/FeatureServer/0) | Off | — | |
| 9 | VT Mask - GeoJSON Test | [`vermont-mask.geojson`](../../basemap-styles/human-geography-detail-blue-water/vermont-mask.geojson) | On | — | Scale range 1:0–1:794,605 |
| 10 | VT Data - State Boundary | [AGOL hosted FeatureServer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Boundary_BNDHASH_poly_vtbnd_SP_v1/FeatureServer/0) | On | — | Transparent fill, light gray `#e0e0e0` dashed outline |
| 11 | VT Basemap 2026 Context Boundaries | VCGI vector tile layer, item `07f27428b81049d4b250ccdb457be37a` | On *(presumed — no explicit `visibility` key)* | — | Surrounding state/international boundary lines + water, scale range 1:0–1:794,117 (matches the VT Mask's own cutoff) |

**No Lidar DEM Hillshade layer** — this is the one structural difference
from Base Topo; every other sublayer matches.

### Boundaries group (Group layer item)

Same two sublayers (Town Boundaries-Outline + Town Boundaries), both On
— see [Test 02b's writeup](../topographic-test-02b-world-terrain-labels/README.md#boundaries-group-group-layer-item).

### Labels group (Group layer item)

Same four sublayers (World Terrain Reference Labels Light On; VT
Basemap 2026 Town Labels Off, superseded by Town Labels Manual
Deconflict; City Points presumed On) — see [Test 02b's writeup](../topographic-test-02b-world-terrain-labels/README.md#labels-group-group-layer-item).

## What's different from Test 02b

Only the bottom group: **Base** instead of **Base Topo** — the Lidar DEM
Hillshade layer is absent entirely (not just toggled off). Boundaries
and Labels are the exact same Group layer items, unchanged.

## Related

- [`../topographic-test-02b-world-terrain-labels/README.md`](../topographic-test-02b-world-terrain-labels/README.md) —
  the Base Topo counterpart this is paired with
- [`../README.md#reusable-group-layers`](../README.md#reusable-group-layers) —
  both the Base Topo and Base configurations, with stacking order
- [`../README.md`](../README.md) — index of all webmap tests
