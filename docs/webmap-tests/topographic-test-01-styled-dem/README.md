# Topographic — Test 01 (Styled DEM)

**Live embed:** <https://vcgitimterway.github.io/vermont-basemaps/webmap-tests/topographic-test-01-styled-dem/>
**ArcGIS Online item:** <https://vcgi.maps.arcgis.com/apps/mapviewer/index.html?webmap=c6a5d16848b84f02a67a2e73be6958f9>
**AGOL item title:** "Basemap 2026 - Topographic - Test 01 (TiTiler Styled DEM)"
**Test extent:** roughly Woodstock/Killington area, VT (-72.85 to -72.69° W, 43.59 to 43.65° N)

Publicly shared as of this writing; pulled directly from the web map's
JSON via the AGOL sharing REST API (`/sharing/rest/content/items/<id>/data`),
not hand-described — it'll go stale if the map changes without this doc
being re-pulled.

## Basemap

**Human Geography Map** (Esri Living Atlas) — but its own "Human
Geography Base" vector tile sub-layer is turned **off** in this test, and
only the **Human Geography Label** sub-layer (place names) is left on, as
a separate operational layer below. So visually, the actual
terrain/ground is coming from the DEM + hillshade layers, not from Esri's
basemap imagery — Living Atlas is only contributing place-name labels
here.

## Layers shown (as saved — on/off reflects this specific test, not a permanent default)

| Layer | Source | On? | Opacity | Blend mode | Notes |
|---|---|---|---|---|---|
| Lidar DEM Hillshade | ArcGIS cached ImageServer ([`IMG_VCGI_LIDARHILLSHD_WM_CACHE_v1`](https://maps.vcgi.vermont.gov/arcgis/rest/services/EGC_services/IMG_VCGI_LIDARHILLSHD_WM_CACHE_v1/ImageServer)) | On | 0.66 | normal | The [Bare Earth Hillshade](../../data-sources/hillshade-bare-earth.md) |
| **Test Titiler** | TiTiler WebTiledLayer | On | default | **soft-light** | The actual subject of this test — confirmed byte-for-byte match to [`titiler-colormap.min.json`](../../dem-color-ramps/11class-feet-aligned/titiler-colormap.min.json) applied to the [Bare Earth DEM](../../data-sources/dem-bare-earth.md). Blended with **soft-light**, not the Multiply/Overlay suggested in the ramp's ArcGIS Pro instructions — worth reconciling which actually looks better |
| Human Geography Base | Esri Living Atlas vector tile | **Off** | — | — | Basemap's own base layer, deliberately turned off (see above) |
| VT E911 — Alpine Trails | [AGOL hosted feature layer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Emergency_FOOTPRINTS_poly_SP_v1/FeatureServer/0) | On | 0.41 | normal | Same service as Golf Courses below, different filter/definition query presumably |
| VT E911 — Golf Courses | same FeatureServer as above | On | 0.41 | normal | |
| Human Geography Detail — Blue Water Desaturated | Esri Living Atlas vector tile | **Off** | — | — | A desaturated water variant exists but isn't the one in use |
| Human Geography Detail — Blue Water | Esri Living Atlas vector tile | On | — | — | The non-desaturated water variant is the one actually shown |
| VT Protected Lands Database | [AGOL hosted feature layer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Cadastral_PROTECTEDLND_poly_SP_v2/FeatureServer/0) | **Off** | 0.34 | normal | Same service as our [Protected Lands profile](../../data-sources/protected-lands.md); present but toggled off in this saved view |
| 1ft Lidar Contours — "COPY - Dark Olive" | Vector tile (Esri VT style, duplicated from the base CN1TGEN service) | On | — | — | `minScale` ≈ 1:178,627 — only draws at large/zoomed-in scales, not statewide. This is a **copy** of our [dark-olive contour style](../../contour-styles/dark-olive/README.md) made via Esri's Vector Tile Style Editor, not literally this repo's `style.json` — the two could drift apart; worth checking they still match |
| Vermont Significant Wetlands Inventory | [AGOL hosted feature layer](https://services5.arcgis.com/Uzks6LSde6r23wwG/arcgis/rest/services/Vermont_Significant_Wetland_Inventory/FeatureServer/0) | On | — | — | **New find:** hosted under a different org (`Uzks6LSde6r23wwG`, not VCGI's usual `BkFxaEFNwHqX3tAw`) — likely ANR, not VCGI. This is the actual regulatory VSWI, confirming it's a genuinely different dataset from the `LandLandcov_Wetlands` metadata records flagged as a possible-but-unconfirmed match in [`../../data-sources/README.md`](../../data-sources/README.md) |
| Buildings 2022 (default style) | Esri Living Atlas vector tile | On | — | — | `minScale`/`maxScale` set — large-scale only, as expected for building footprints |
| Human Geography Detail | Esri Living Atlas vector tile | **Off** | 0.5 | normal | The general detail layer (roads etc.) is off — consistent with VCGI preferring its own data for most themes, per [`../../architecture/foundational-layers.md`](../../architecture/foundational-layers.md#esri-community-maps-separate-existing-pipeline) |
| VT E911 — Alpine Ski Lifts | [AGOL hosted feature layer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Emergency_ALPINELIFTS_line_SP_v1/FeatureServer/0) | On | — | — | |
| Human Geography Label | Esri Living Atlas vector tile | On | — | — | Place names — the one piece of Living Atlas actually left on |
| Buildings 2022 — "Copy DCD9D6" | Vector tile (recolored copy) | **Off** | — | — | A prepared, recolored buildings style using **exactly** the `#DCD9D6` building color recommended in [`11class-monochrome-canvas`](../../dem-color-ramps/11class-monochrome-canvas/README.md#companion-layers) — present but not the one currently shown; the default-style Buildings 2022 above is active instead |
| Mountains and Hills | [ArcGIS MapServer sublayer](https://maps.vcgi.vermont.gov/arcgis/rest/services/VCGI_services/VCGI_BASEMAP_WM_v2/MapServer/4) | On | — | — | **New service reference** for this layer in our inventory — a classic MapServer sublayer, not an AGOL hosted feature layer like most other VSDI layers |

## Design decisions (as observed, not all explicitly confirmed with you yet)

- **TiTiler DEM as the actual terrain surface**, with Esri's own basemap
  imagery switched off entirely except for place-name labels — this test
  is specifically evaluating the custom color ramp + hillshade
  combination on its own, not blended with or compared against Esri's
  stock terrain rendering.
- **`soft-light` blend mode** was used for the TiTiler layer in practice,
  rather than Multiply/Overlay as suggested in the ramp's own ArcGIS Pro
  instructions — this might be a MapViewer-specific choice (Pro and
  Online don't necessarily offer identical blend mode options) or a
  deliberate preference; worth a note back in the ramp's docs if
  `soft-light` turns out to be the better choice generally.
- **Several prepared alternates exist but are switched off**: the
  desaturated water variant, the Protected Lands overlay, and critically
  the `#DCD9D6`-recolored Buildings layer — suggesting iterative
  testing is already underway (styles prepared ahead of deciding whether
  to use them), not just the single happy-path described here.
- **Recreation-themed E911 layers are on** (alpine trails, ski lifts, golf
  courses) alongside Protected Lands (off) and Wetlands (on) — reads like
  this test is oriented toward outdoor recreation use cases specifically,
  not a general-purpose basemap evaluation.
- The **1ft contours only draw at large scale** (`minScale` ≈ 1:178,627),
  consistent with the "to revisit... regional scale zoom levels" note
  already in the [dark-olive contour style doc](../../contour-styles/dark-olive/README.md#to-revisit).

## Related

- [`../README.md`](../README.md) — index of all webmap tests
- [`../../dem-color-ramps/11class-feet-aligned/README.md`](../../dem-color-ramps/11class-feet-aligned/README.md)
- [`../../contour-styles/dark-olive/README.md`](../../contour-styles/dark-olive/README.md)
- [`../../data-sources/README.md`](../../data-sources/README.md)
