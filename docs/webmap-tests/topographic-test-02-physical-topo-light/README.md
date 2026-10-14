# Topographic — Test 02 (Physical Topo Light)

Pulled directly from the web map's JSON via the AGOL sharing REST API,
not hand-described — re-pull if this map changes rather than editing
this table by hand.

**Live embed:** <https://vcgitimterway.github.io/vermont-basemaps/webmap-tests/topographic-test-02-physical-topo-light/>
**ArcGIS Online item:** <https://vcgi.maps.arcgis.com/apps/mapviewer/index.html?webmap=641315e8dce04177a289c29a5debf7f3>
**AGOL item title:** "Basemap 2026 - Topographic - Test 02 Physical Topo Light"
**Test extent:** centered -72.8647, 44.1355 at 1:36,112 (Mad River Valley area, VT)

## Basemap

Same as Test 01: **Human Geography Map** (Esri Living Atlas), own "Human
Geography Base" vector tile sub-layer turned **off** — Living Atlas
contributes nothing to the visible ground surface here.

## Layers shown (top to bottom as returned by the API)

| # | Layer | Source | On? | Opacity | Notes |
|---|---|---|---|---|---|
| 0 | Lidar DEM Hillshade | ArcGIS cached ImageServer ([`IMG_VCGI_LIDARHILLSHD_WM_CACHE_v1`](https://maps.vcgi.vermont.gov/arcgis/rest/services/EGC_services/IMG_VCGI_LIDARHILLSHD_WM_CACHE_v1/ImageServer)) | On | 0.4 | `minScale` ≈ 1:13.1M. **No DEM color-ramp layer in this map at all** — see [Design notes](#design-notes) |
| 1 | Vermont Protected Lands Database | [AGOL hosted FeatureServer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Cadastral_PROTECTEDLND_poly_SP_v2/FeatureServer/0) | On | 0.25 | New to this test, not present in Test 01. Filtered to `INT_ORGTYP` = State, Municipal, or Federal — i.e. publicly stewarded protected areas only |
| 2 | Alpine Trails — VT E911 Other Mapped Features of Interest | [shared FeatureServer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Emergency_FOOTPRINTS_poly_SP_v1/FeatureServer/0) | On | 0.41 | `FOOTPRINTTYPE` filter on the shared E911 footprints service |
| 3 | Golf Courses — VT E911 Other Mapped Features of Interest | same FeatureServer | On | 0.75 | |
| 4 | Quarries — VT E911 Other Mapped Features of Interest | same FeatureServer | On | 0.41 | |
| 5 | 1ft Lidar Contours — "COPY - Dark Olive" | Vector tile (Esri VT style copy) | Off | 0.25 | See [dark-olive README](../../contour-styles/dark-olive/README.md) |
| 6 | Human Geography Detail — Blue Water **Light Roads** | Esri Living Atlas vector tile, VCGI-styled — **new style variant**, not the same item as Test 01's | Off | — | This is the exact style edited this session (road border color muted from `#505050` to `#999999`) — see [Design notes](#design-notes) |
| 7 | Vermont Significant Wetlands Inventory | [AGOL hosted feature layer](https://services5.arcgis.com/Uzks6LSde6r23wwG/arcgis/rest/services/Vermont_Significant_Wetland_Inventory/FeatureServer/0) | Off | 0.75 | ANR-hosted (ANR GIS staff are VCGI employees) |
| 8 | Buildings 2022 **(White)** | Vector tile — **new style variant**, not the same item as Test 01's "Light" buildings style | Off | — | `minScale`/`maxScale` set |
| 9 | VT Data — E911 Alpine Ski Lifts | [AGOL hosted feature layer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Emergency_ALPINELIFTS_line_SP_v1/FeatureServer/0) | Off | — | |
| 10 | VT Mask - GeoJSON Test | [`vermont-mask.geojson`](../../basemap-styles/human-geography-detail-blue-water/vermont-mask.geojson), served via this repo's GitHub Pages | On | — | Positioned **below** the label layers (same reasoning as Test 01 — see [mask README](../../basemap-styles/human-geography-detail-blue-water/README.md#known-limitation-label-text-gets-cut-off-mid-glyph)) |
| 11 | Mountains and Hills — VCGI BASEMAP WM v2 | [ArcGIS MapServer sublayer](https://maps.vcgi.vermont.gov/arcgis/rest/services/VCGI_services/VCGI_BASEMAP_WM_v2/MapServer/4) | On | — | |
| 12 | Lake and Pond Labels — VCGI BASEMAP WM CACHE v2 | [ArcGIS MapServer sublayer](https://maps.vcgi.vermont.gov/arcgis/rest/services/VCGI_services/VCGI_BASEMAP_WM_CACHE_v2/MapServer/25) | On | — | VCGI-sourced place-name label, not Esri Living Atlas |
| 13 | River and Stream Names — VCGI BASEMAP WM CACHE v2 | [ArcGIS MapServer sublayer](https://maps.vcgi.vermont.gov/arcgis/rest/services/VCGI_services/VCGI_BASEMAP_WM_CACHE_v2/MapServer/30) | On | 1 | Same pattern as Lake and Pond Labels |
| 14 | Human Geography Label | Esri Living Atlas vector tile | On | — | Place names — the one piece of Living Atlas left on |

**A note on the On/Off column:** the web map JSON doesn't always carry an
explicit `visibility` key per layer — several layers that are genuinely
on (e.g. Test 01b's replacement label layer) have no key at all, same as
several that are genuinely off. Where a layer here matches one already
documented for Test 01/01b under the same title, its On/Off state is
carried over by that precedent; Protected Lands Database (new to this
map, no precedent) was confirmed directly with Tim.

## Design notes

- **No DEM color-ramp / hypsometric tint layer in this map at all** —
  unlike Test 01 (which layers a TiTiler-styled 11-class elevation color
  ramp over the hillshade), Test 02 relies on **hillshade alone**, and at
  a lower opacity (0.4 vs. Test 01's 0.67). This is a deliberate,
  structural difference, not an oversight: per Tim, "Physical Topo Light"
  is intended as a **muted basemap meant to sit underneath user-added
  thematic point/line/polygon data** — a colored elevation tint would
  compete with whatever a consuming app layers on top, so it's left out
  entirely rather than just dialed down.
- **Two new vector tile style variants, not shared with Test 01:**
  "Human Geography Detail — Blue Water Light Roads" and "Buildings 2022
  (White)" are each their own distinct AGOL item (different `itemId`s),
  not the same styles Test 01 uses. The "Light Roads" style is the one
  whose road-border color was muted this session (`#505050` → `#999999`)
  — see [the raw style file](../../basemap-styles/human-geography-detail-blue-water-light-roads)
  (committed, but doesn't yet have its own profile folder/README the way
  [`human-geography-detail-blue-water/`](../../basemap-styles/human-geography-detail-blue-water/README.md)
  does — worth doing if this variant becomes the long-term "Light" style).
- **Vermont Protected Lands Database** is new to this test (not part of
  Test 01's layer set), shown filtered to `INT_ORGTYP` = State,
  Municipal, or Federal — publicly stewarded protected land only,
  excluding privately held conservation parcels. See
  [`protected-lands.md`](../../data-sources/protected-lands.md) for what's
  known about the underlying source.
- Quarries, Alpine Trails, and Golf Courses are all filtered views of the
  same shared E911 FeatureServer, not three separate services (same as
  Test 01).

## Related

- [`../topographic-test-01-styled-dem/README.md`](../topographic-test-01-styled-dem/README.md) —
  the prior test this one builds on conceptually (same non-road layer
  set, different terrain treatment and style variants)
- [`../../architecture/cross-platform-publishing.md`](../../architecture/cross-platform-publishing.md) —
  per-layer status on getting every layer in this test map serving
  cleanly on both ArcGIS and open-source apps
- [`../README.md`](../README.md) — index of all webmap tests
- [`../../contour-styles/dark-olive/README.md`](../../contour-styles/dark-olive/README.md)
- [`../../basemap-styles/human-geography-detail-blue-water/README.md`](../../basemap-styles/human-geography-detail-blue-water/README.md)
- [`../../data-sources/protected-lands.md`](../../data-sources/protected-lands.md)
- [`../../data-sources/README.md`](../../data-sources/README.md)
