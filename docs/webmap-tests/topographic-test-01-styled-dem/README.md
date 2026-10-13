# Topographic — Test 01 (Styled DEM)

Pulled directly from the web map's JSON via the AGOL sharing REST API,
not hand-described — re-pull if this map changes rather than editing
this table by hand.

**Live embed:** <https://vcgitimterway.github.io/vermont-basemaps/webmap-tests/topographic-test-01-styled-dem/>
**ArcGIS Online item:** <https://vcgi.maps.arcgis.com/apps/mapviewer/index.html?webmap=c6a5d16848b84f02a67a2e73be6958f9>
**AGOL item title:** "Basemap 2026 - Topographic - Test 01 (TiTiler Styled DEM)"
**Test extent:** centered -72.7178, 43.4065 at 1:18,056 (Plymouth/Ludlow/Okemo area, VT)

## Basemap

**Human Geography Map** (Esri Living Atlas), with its own "Human
Geography Base" vector tile sub-layer turned **off** — Living Atlas
contributes nothing to the visible ground surface here; terrain comes
from the DEM + hillshade layers.

## Layers shown (top to bottom as returned by the API)

| # | Layer | Source | On? | Opacity | Notes |
|---|---|---|---|---|---|
| 0 | Lidar DEM Hillshade | ArcGIS cached ImageServer ([`IMG_VCGI_LIDARHILLSHD_WM_CACHE_v1`](https://maps.vcgi.vermont.gov/arcgis/rest/services/EGC_services/IMG_VCGI_LIDARHILLSHD_WM_CACHE_v1/ImageServer)) | On | 0.67 | `minScale` ≈ 1:13.1M — doesn't render at very small/statewide zoom-out |
| 1 | 2023 QL1 DEM COG - TiTiler 11 Zone Elev Style | TiTiler WebTiledLayer | On | 0.67 | `templateUrl` is [`titiler-colormap.min.json`](../../dem-color-ramps/11class-feet-aligned/titiler-colormap.min.json). Blend mode **soft-light**. `minScale` ≈ 1:8.4M |
| 2 | Alpine Trails — VT E911 Other Mapped Features of Interest | [shared FeatureServer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Emergency_FOOTPRINTS_poly_SP_v1/FeatureServer/0) | On | 0.41 | `FOOTPRINTTYPE` filter on the shared E911 footprints service |
| 3 | Golf Courses — VT E911 Other Mapped Features of Interest | same FeatureServer | On | 0.41 | |
| 4 | Quarries — VT E911 Other Mapped Features of Interest | same FeatureServer | On | 0.41 | |
| 5 | 1ft Lidar Contours — "COPY - Dark Olive" | Vector tile (Esri VT style copy) | Off | — | A **copy**, not this repo's `style.json` directly — see [dark-olive README](../../contour-styles/dark-olive/README.md) |
| 6 | Human Geography Detail — Blue Water | Esri Living Atlas vector tile | Off | — | |
| 7 | Vermont Significant Wetlands Inventory | [AGOL hosted feature layer](https://services5.arcgis.com/Uzks6LSde6r23wwG/arcgis/rest/services/Vermont_Significant_Wetland_Inventory/FeatureServer/0) | Off | — | ANR-hosted (ANR GIS staff are VCGI employees) |
| 8 | Buildings 2022 | Vector tile, sourced from VCGI's 2022 land cover classification | Off | — | See [`cross-platform-publishing.md`](../../architecture/cross-platform-publishing.md) for sourcing detail |
| 9 | VT Data — E911 Alpine Ski Lifts | [AGOL hosted feature layer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Emergency_ALPINELIFTS_line_SP_v1/FeatureServer/0) | Off | — | |
| 10 | VT Mask - GeoJSON Test | [`vermont-mask.geojson`](../../basemap-styles/human-geography-detail-blue-water/vermont-mask.geojson), served via this repo's GitHub Pages | On | — | Positioned **below** the label layer (next row) — see [mask README](../../basemap-styles/human-geography-detail-blue-water/README.md#known-limitation-label-text-gets-cut-off-mid-glyph) for why |
| 11 | Human Geography Label | Esri Living Atlas vector tile | On | — | Place names — the one piece of Living Atlas left on |
| 12 | Mountains and Hills — VCGI BASEMAP WM v2 | [ArcGIS MapServer sublayer](https://maps.vcgi.vermont.gov/arcgis/rest/services/VCGI_services/VCGI_BASEMAP_WM_v2/MapServer/4) | Off | — | |
| 13 | Lake and Pond Labels — VCGI BASEMAP WM CACHE v2 | [ArcGIS MapServer sublayer](https://maps.vcgi.vermont.gov/arcgis/rest/services/VCGI_services/VCGI_BASEMAP_WM_CACHE_v2/MapServer/25) | On | — | VCGI-sourced place-name label, not Esri Living Atlas |
| 14 | River and Stream Names — VCGI BASEMAP WM CACHE v2 | [ArcGIS MapServer sublayer](https://maps.vcgi.vermont.gov/arcgis/rest/services/VCGI_services/VCGI_BASEMAP_WM_CACHE_v2/MapServer/30) | On | — | Same pattern as Lake and Pond Labels |

## Design notes

- TiTiler-styled DEM + hillshade are the actual terrain surface; Esri's
  basemap imagery is switched off except for place-name labels.
- "Lake and Pond Labels" and "River and Stream Names" are VCGI-sourced,
  distinct from the Esri "Human Geography Label" layer — a step toward
  the VSDI-sourced place-name alternative discussed in
  [`foundational-layers.md` gap #4](../../architecture/foundational-layers.md#gaps--open-questions).
- The Vermont mask sits below the label layer specifically to avoid
  cutting labels mid-word (see the mask README for the underlying
  limitation).
- Quarries, Alpine Trails, and Golf Courses are all filtered views of the
  same shared E911 FeatureServer, not three separate services.

## Related

- [`../../architecture/cross-platform-publishing.md`](../../architecture/cross-platform-publishing.md) —
  per-layer status on getting every layer in this test map serving
  cleanly on both ArcGIS and open-source apps
- [`../README.md`](../README.md) — index of all webmap tests
- [`../../dem-color-ramps/11class-feet-aligned/README.md`](../../dem-color-ramps/11class-feet-aligned/README.md)
- [`../../contour-styles/dark-olive/README.md`](../../contour-styles/dark-olive/README.md)
- [`../../basemap-styles/human-geography-detail-blue-water/README.md`](../../basemap-styles/human-geography-detail-blue-water/README.md)
- [`../../data-sources/README.md`](../../data-sources/README.md)
