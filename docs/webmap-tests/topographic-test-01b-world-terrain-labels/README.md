# Topographic — Test 01b (World Terrain Labels)

Pulled directly from the web map's JSON via the AGOL sharing REST API,
not hand-described — re-pull if this map changes rather than editing
this table by hand.

**Live embed:** <https://vcgitimterway.github.io/vermont-basemaps/webmap-tests/topographic-test-01b-world-terrain-labels/>
**ArcGIS Online item:** <https://vcgi.maps.arcgis.com/apps/mapviewer/index.html?webmap=bbab5ff34b7543df8a06cee07a6f30ec>
**AGOL item title:** "VT Basemap 2026 - Topographic - Test 01b"
**Test extent:** centered -72.7166, 43.4048 at 1:18,056

Save-as copy of an earlier styled-DEM test webmap, with one change: the
label layer.

## Basemap

Same as Test 01: **Human Geography Map** (Esri Living Atlas), own "Human
Geography Base" vector tile sub-layer turned **off** — terrain comes from
the DEM + hillshade layers, not Esri's basemap imagery.

## Layers shown (top to bottom as returned by the API)

| # | Layer | Source | On? | Opacity | Notes |
|---|---|---|---|---|---|
| 0 | Lidar DEM Hillshade | ArcGIS cached ImageServer ([`IMG_VCGI_LIDARHILLSHD_WM_CACHE_v1`](https://maps.vcgi.vermont.gov/arcgis/rest/services/EGC_services/IMG_VCGI_LIDARHILLSHD_WM_CACHE_v1/ImageServer)) | On | 0.67 | `minScale` ≈ 1:13.1M |
| 1 | 2023 QL1 DEM COG - TiTiler 11 Zone Elev Style | TiTiler WebTiledLayer | On | 0.67 | [`titiler-colormap.min.json`](../../dem-color-ramps/11class-feet-aligned/titiler-colormap.min.json), blend **soft-light**, `minScale` ≈ 1:8.4M |
| 2 | Alpine Trails — VT E911 Other Mapped Features of Interest | [shared FeatureServer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Emergency_FOOTPRINTS_poly_SP_v1/FeatureServer/0) | On | 0.41 | |
| 3 | Golf Courses — VT E911 Other Mapped Features of Interest | same FeatureServer | On | 0.41 | |
| 4 | Quarries — VT E911 Other Mapped Features of Interest | same FeatureServer | On | 0.41 | |
| 5 | 1ft Lidar Contours — "COPY - Dark Olive" | Vector tile (Esri VT style copy) | Off | 0.67 | See [dark-olive README](../../contour-styles/dark-olive/README.md) |
| 6 | Human Geography Detail — Blue Water | Esri Living Atlas vector tile, [customized copy](../../basemap-styles/human-geography-detail-blue-water/README.md) | Off | — | |
| 7 | Vermont Significant Wetlands Inventory | [AGOL hosted feature layer](https://services5.arcgis.com/Uzks6LSde6r23wwG/arcgis/rest/services/Vermont_Significant_Wetland_Inventory/FeatureServer/0) | Off | — | |
| 8 | Buildings 2022 | Vector tile, sourced from VCGI's 2022 land cover classification | Off | — | |
| 9 | VT Data — E911 Alpine Ski Lifts | [AGOL hosted feature layer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Emergency_ALPINELIFTS_line_SP_v1/FeatureServer/0) | Off | — | |
| 10 | VT Mask - GeoJSON Test | [`vermont-mask.geojson`](../../basemap-styles/human-geography-detail-blue-water/vermont-mask.geojson), served via this repo's GitHub Pages | On | — | |
| 11 | **World Terrain Reference Labels** | Esri Living Atlas vector tile (`World_Basemap_v2`), VCGI-styled copy referencing Esri's "World Terrain Reference Label" cartography | On | — | Combines place names, water-feature names, and mountain/peak labels in one layer |

## What's different from Test 01

The only change is the label layer. Test 01 used four separate layers for
labels: Esri's Human Geography Label, plus three VCGI-sourced layers
(Lake and Pond Labels, River and Stream Names, Mountains and Hills). This
version replaces all four with one Esri Living Atlas vector tile layer —
"World Terrain Reference Labels" — styled by VCGI from the same
`World_Basemap_v2` source as the Blue Water hydrography layer.

**Cartographically**, this is a strong, cohesive result: one well-designed
layer instead of four, built on a mature Esri reference style intended
for exactly this (topographic terrain labeling).

**For cross-platform purposes, this is a step backward from Test 01**,
not forward. Test 01's Lake/Pond Labels and River/Stream Names were
confirmed `Query`-capable VCGI sources — real, queryable, exportable
VCGI-sourced labels (see
[`cross-platform-publishing.md`](../../architecture/cross-platform-publishing.md)).
This version has no VCGI-sourced label content at all; all of it is
licensed Esri content, in the same "not exportable as-is" category as the
Blue Water layer, now also covering water-feature and mountain names in
addition to place names. An open-source equivalent would need to combine
VCGI's own hydrography labels, mountain/hill labels, and general place
names (`BasemapLandmarks_GEONAME`, still unopened) into one comparably
cohesive style — more sourcing work than Test 01 implied, not less.

## Related

- [`../../architecture/cross-platform-publishing.md`](../../architecture/cross-platform-publishing.md) —
  per-layer status on getting every layer serving cleanly on both ArcGIS
  and open-source apps
- [`../README.md`](../README.md) — index of all webmap tests
