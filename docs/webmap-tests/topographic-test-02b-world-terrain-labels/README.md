# Topographic — Test 02b (World Terrain Labels)

Pulled directly from the web map's JSON via the AGOL sharing REST API,
not hand-described — re-pull if this map changes rather than editing
this table by hand.

**Live embed:** <https://vcgitimterway.github.io/vermont-basemaps/webmap-tests/topographic-test-02b-world-terrain-labels/>
**ArcGIS Online item:** <https://vcgi.maps.arcgis.com/apps/mapviewer/index.html?webmap=8d2975f539db4897bd61cfe2f8ced44c>
**AGOL item title:** "Basemap 2026 - Topographic - Test 02b Physical Topo Light"
**Test extent:** centered -72.8647, 44.1355 at 1:36,112 (same area as Test 02)

Save-as copy of [Topographic Test 02](../topographic-test-02-physical-topo-light/README.md)
with one change: the label layer.

## Basemap

Same as Test 02: **Human Geography Map** (Esri Living Atlas), own "Human
Geography Base" vector tile sub-layer turned **off**.

## Layers shown (top to bottom as returned by the API)

| # | Layer | Source | On? | Opacity | Notes |
|---|---|---|---|---|---|
| 0 | Lidar DEM Hillshade | ArcGIS cached ImageServer ([`IMG_VCGI_LIDARHILLSHD_WM_CACHE_v1`](https://maps.vcgi.vermont.gov/arcgis/rest/services/EGC_services/IMG_VCGI_LIDARHILLSHD_WM_CACHE_v1/ImageServer)) | On | 0.4 | Same as Test 02 — no DEM color-ramp layer in this map either |
| 1 | Vermont Protected Lands Database | [AGOL hosted FeatureServer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Cadastral_PROTECTEDLND_poly_SP_v2/FeatureServer/0) | *unconfirmed* | 0.25 | Same unresolved on/off question as in Test 02 |
| 2 | Alpine Trails — VT E911 Other Mapped Features of Interest | [shared FeatureServer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Emergency_FOOTPRINTS_poly_SP_v1/FeatureServer/0) | On | 0.41 | |
| 3 | Golf Courses — VT E911 Other Mapped Features of Interest | same FeatureServer | On | 0.75 | |
| 4 | Quarries — VT E911 Other Mapped Features of Interest | same FeatureServer | On | 0.41 | |
| 5 | 1ft Lidar Contours — "COPY - Dark Olive" | Vector tile (Esri VT style copy) | Off | 0.25 | |
| 6 | Human Geography Detail — Blue Water Light Roads | Esri Living Atlas vector tile, VCGI-styled (same new "Light Roads" style variant as Test 02) | Off | — | |
| 7 | Vermont Significant Wetlands Inventory | [AGOL hosted feature layer](https://services5.arcgis.com/Uzks6LSde6r23wwG/arcgis/rest/services/Vermont_Significant_Wetland_Inventory/FeatureServer/0) | Off | 0.75 | |
| 8 | Buildings 2022 (White) | Vector tile (same new "White" style variant as Test 02) | Off | — | |
| 9 | VT Data — E911 Alpine Ski Lifts | [AGOL hosted feature layer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Emergency_ALPINELIFTS_line_SP_v1/FeatureServer/0) | Off | — | |
| 10 | VT Mask - GeoJSON Test | [`vermont-mask.geojson`](../../basemap-styles/human-geography-detail-blue-water/vermont-mask.geojson) | On | — | Positioned below the label layer, same reasoning as Test 01/02 |
| 11 | **World Terrain Reference Labels** | Esri Living Atlas vector tile (`World_Basemap_v2`), VCGI-styled copy referencing Esri's "World Terrain Reference Label" cartography | On | — | **The exact same AGOL item** Test 01b uses (`d3ca482e8f044b6283961db9b06350de`) — reused, not duplicated |

## What's different from Test 02

Only the label layer. Test 02 used four separate layers for labels:
Esri's Human Geography Label, plus three VCGI-sourced layers (Lake and
Pond Labels, River and Stream Names, Mountains and Hills). This version
replaces all four with one Esri Living Atlas vector tile layer — "World
Terrain Reference Labels" — the same layer already used in
[Test 01b](../topographic-test-01b-world-terrain-labels/README.md), not
a newly built copy.

The cross-platform tradeoff discussed in
[Test 01b's writeup](../topographic-test-01b-world-terrain-labels/README.md#whats-different-from-test-01)
applies identically here: cartographically cohesive, but gives up Test
02's VCGI-sourced, `Query`-capable label content (Lake/Pond, River/Stream)
in favor of licensed Esri content that isn't exportable as-is.

## Related

- [`../topographic-test-02-physical-topo-light/README.md`](../topographic-test-02-physical-topo-light/README.md) —
  the version this was saved from
- [`../topographic-test-01b-world-terrain-labels/README.md`](../topographic-test-01b-world-terrain-labels/README.md) —
  the other test using this same label layer
- [`../../architecture/cross-platform-publishing.md`](../../architecture/cross-platform-publishing.md)
- [`../README.md`](../README.md) — index of all webmap tests
