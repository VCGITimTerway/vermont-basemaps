# Cross-Platform Publishing: Topographic Test 01 Layers

For each layer currently in
[Topographic — Test 01](../webmap-tests/topographic-test-01-styled-dem/README.md),
what it takes to get it serving cleanly on **both** ArcGIS (Map Viewer,
Experience Builder) and open-source (MapLibre/Leaflet) apps, given where
it's published today. Companion to [`foundational-layers.md`](foundational-layers.md),
which covers the architecture generally — this is the concrete, per-layer
punch list.

## Recommendation: one PMTiles tileset per background/cartographic layer, not two separate publishing paths

For layers that are purely cartographic background (contours, hydrography
lines, place-name labels, building footprints shown as context — anything
that doesn't need click-for-attributes in Map Viewer), publish **one**
PMTiles tileset and reference it from both platforms: directly in
open-source apps, and from ArcGIS Online via a `style.json`-based Vector
Tile Layer item (same pattern already used for the contour and Human
Geography Detail styles in this repo). There's no need to *also* maintain
a separate native Esri Vector Tile Service for these — Map Viewer's
Vector Tile Layer doesn't support click popups regardless of whether it's
backed by a native Esri service or a PMTiles tileset, so nothing is lost
by consolidating to one pipeline, and a MapLibre app on the open-source
side can still get full click-popup behavior from that same tileset via
[`map.queryRenderedFeatures()`](https://maplibre.org/maplibre-gl-js/docs/API/classes/Map/#queryrenderedfeatures) —
MVT tiles carry real per-feature attributes even though Map Viewer
doesn't expose them.

Layers where Esri users specifically need click-for-attributes (the E911
interest layers, Wetlands, etc.) keep their Feature Service as-is — that
requirement doesn't go away. A PMTiles tileset can still be built from the
same source for the open-source side's rendering and popups.

## Per-layer status

**Legend:** ✅ done/working · 🔧 straightforward, not yet built

| Layer | Currently published as | ArcGIS | Open-source (PMTiles/TiTiler) | Notes |
|---|---|---|---|---|
| Lidar DEM Hillshade | ArcGIS cached ImageServer ([`IMG_VCGI_LIDARHILLSHD_WM_CACHE_v1`](../data-sources/hillshade-bare-earth.md)) | ✅ | ✅ (TiTiler, same COG) | Raster — TiTiler is the shared single pipeline here, same role PMTiles plays for vector |
| 2023 QL1 DEM — TiTiler styled | Same COG via TiTiler | ✅ | ✅ (TiTiler) | Working precedent for "one raster pipeline, two consumers" |
| Alpine Trails (E911) | [AGOL hosted FeatureServer](../data-sources/README.md), shared `FOOTPRINTTYPE`-coded service, `capabilities: Query,Extract` | ✅ | 🔧 | Export → tippecanoe → PMTiles; keep the Feature Service for Esri popups, PMTiles + `queryRenderedFeatures` covers open-source popups |
| Golf Courses (E911) | Same shared FOOTPRINTS service, `FOOTPRINTTYPE = G1` | ✅ | 🔧 | One tippecanoe run against the whole service covers this and Alpine Trails/Quarries together, filtered client-side by `FOOTPRINTTYPE` |
| Quarries (E911) | Same shared FOOTPRINTS service, `FOOTPRINTTYPE = Q1` | ✅ | 🔧 | Same export as above |
| 1ft Lidar Contours (Dark Olive) | Esri Vector Tile Service (`VECTOR_VCGI_CN1TGEN_WM_v1`) **and** an [ArcGIS Server MapServer](https://maps.vcgi.vermont.gov/arcgis/rest/services/EGC_services/MAP_VCGI_LIDARCONTOURS_WM_CACHE_v1/MapServer), `capabilities: Query,Map,Data` | ✅ | 🔧 | The MapServer exposes every generalization tier (1ft through 1000ft, including the `_Major` variants) as its own queryable sublayer (27 total) — a full tippecanoe export is achievable directly from this service |
| Human Geography Detail — Blue Water | Esri Living Atlas (`World_Basemap_v2`), customized copy in [`basemap-styles/`](../basemap-styles/human-geography-detail-blue-water/README.md) | ✅ | 🔧 | Licensed Esri content, not exportable as-is. Open-source equivalent: VCGI's own `FS_VCGI_OPENDATA_Water_VHDCARTO_poly_SP_v1` / `..._line_SP_v1` services — confirmed `Query`-capable, EPSG:32145 — see [`foundational-layers.md`](foundational-layers.md#esri-community-maps-separate-existing-pipeline) |
| Vermont Significant Wetlands Inventory | [AGOL hosted FeatureServer](https://services5.arcgis.com/Uzks6LSde6r23wwG/arcgis/rest/services/Vermont_Significant_Wetland_Inventory/FeatureServer/0) (ANR, who are VCGI staff — no cross-org data-sharing question here) | ✅ | 🔧 | Standard export |
| Buildings 2022 | Vector tile, sourced from VCGI's own 2022 high-resolution land cover classification (Buildings class within the [Base Land Cover COG](https://s3.us-east-2.amazonaws.com/vtopendata-prd/Landcover/STATEWIDE_2022_50cm_LANDCOVER_Base.tif)) | ✅ | 🔧 | VCGI's own data. Two possible vector sources, not yet reconciled: the `LandLandcov_Buildings2022` metadata record, or [`ESRICMP_BuildingFootprintsVT_v1`](https://maps.vcgi.vermont.gov/arcgis/rest/services/VCGI_services/ESRICMP_BuildingFootprintsVT_v1/MapServer/2) (a service built specifically for Esri Community Maps, with its own `Carto`-coded categories — see [`foundational-layers.md`](foundational-layers.md#esri-community-maps-separate-existing-pipeline)) — confirm which (if either) matches this layer before building an export |
| E911 Alpine Ski Lifts | [AGOL hosted FeatureServer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Emergency_ALPINELIFTS_line_SP_v1/FeatureServer/0), `capabilities: Query,Extract` | ✅ | ✅ (proof of concept) | See [`../pmtiles-pipeline/alpine-ski-lifts/`](../pmtiles-pipeline/alpine-ski-lifts/README.md) — a working PMTiles file exists; production build should use tippecanoe once Docker is available (not installed in this environment) |
| VT Mask (GeoJSON) | [This repo](../basemap-styles/human-geography-detail-blue-water/vermont-mask.geojson), served via GitHub Pages | ✅ | ✅ | Already cross-platform as-is |
| Human Geography Label | Esri Living Atlas vector tile | ✅ | 🔧, needs its own source | Licensed Esri content. Candidate VCGI source for place names generally: `BasemapLandmarks_GEONAME` (metadata record identified, not yet opened) |
| World Terrain Reference Labels (used in [Test 01b](../webmap-tests/topographic-test-01b-world-terrain-labels/README.md) in place of the four rows above) | Esri Living Atlas (`World_Basemap_v2`), VCGI-styled copy referencing Esri's "World Terrain Reference Label" cartography | ✅ | 🔧 | Same licensing situation as Blue Water. Combines place names, water-feature names, and mountain/peak labels in one layer — cartographically strong, but an open-source equivalent needs to combine Lake/Pond Labels, River/Stream Names, Mountains and Hills, and VHDCARTO water-feature names into one comparably cohesive style, not just source one dataset |
| Mountains and Hills | [ArcGIS MapServer sublayer](https://maps.vcgi.vermont.gov/arcgis/rest/services/VCGI_services/VCGI_BASEMAP_WM_v2/MapServer/4), `capabilities: Map,Query,Data` | ✅ | 🔧 | Standard export |
| Lake and Pond Labels | [ArcGIS MapServer sublayer](https://maps.vcgi.vermont.gov/arcgis/rest/services/VCGI_services/VCGI_BASEMAP_WM_CACHE_v2/MapServer/25), `capabilities: Map,Query,Data` | ✅ | 🔧 | VCGI-sourced place-name labels — a real alternative to Esri's Human Geography Label layer |
| River and Stream Names | [ArcGIS MapServer sublayer](https://maps.vcgi.vermont.gov/arcgis/rest/services/VCGI_services/VCGI_BASEMAP_WM_CACHE_v2/MapServer/30), `capabilities: Map,Query,Data` | ✅ | 🔧 | Same as Lake and Pond Labels |

## Suggested next steps, roughly in order

1. Run the Alpine Ski Lifts proof of concept through real tippecanoe
   (once Docker is available) and compare against the hand-rolled
   version in [`pmtiles-pipeline/alpine-ski-lifts/`](../pmtiles-pipeline/alpine-ski-lifts/README.md).
2. Reconcile the two Buildings 2022 candidate sources
   (`LandLandcov_Buildings2022` vs. `ESRICMP_BuildingFootprintsVT_v1`),
   and open `BasemapLandmarks_GEONAME` to confirm it's the right VCGI
   source for general place names (same approach used for the
   DEM/hillshade/contours/parcels/boundaries profiles already done in
   [`data-sources/`](../data-sources/README.md)).
3. Build the contour export from the MapServer's per-tier sublayers,
   replacing the current Esri-only Vector Tile Service with the shared
   PMTiles pipeline described above.
4. Build the export from VCGI's VHDCARTO waterbody/waterline services as
   the open-source equivalent for Human Geography Detail — Blue Water.
