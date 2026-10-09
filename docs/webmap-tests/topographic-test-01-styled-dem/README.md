# Topographic — Test 01 (Styled DEM)

**Status: final state before moving to a new test version.** Documented
here as of 2026-10-09, reflecting layer renames/reordering/additions made
since the first pass. Pulled directly from the web map's JSON via the
AGOL sharing REST API, not hand-described — re-pull if this map changes
again rather than editing this table by hand.

**Live embed:** <https://vcgitimterway.github.io/vermont-basemaps/webmap-tests/topographic-test-01-styled-dem/>
**ArcGIS Online item:** <https://vcgi.maps.arcgis.com/apps/mapviewer/index.html?webmap=c6a5d16848b84f02a67a2e73be6958f9>
**AGOL item title:** "Basemap 2026 - Topographic - Test 01 (TiTiler Styled DEM)"
**Test extent:** roughly Woodstock/Killington area, VT (-72.85 to -72.69° W, 43.59 to 43.65° N)

## Basemap

**Human Geography Map** (Esri Living Atlas), with its own "Human
Geography Base" vector tile sub-layer still turned **off** — as before,
Living Atlas is contributing essentially nothing to the visible ground
surface here; terrain comes from the DEM + hillshade layers.

## Layers shown (current order, top to bottom as returned by the API)

| # | Layer | Source | On? | Opacity | Blend/scale notes |
|---|---|---|---|---|---|
| 0 | Lidar DEM Hillshade | ArcGIS cached ImageServer ([`IMG_VCGI_LIDARHILLSHD_WM_CACHE_v1`](https://maps.vcgi.vermont.gov/arcgis/rest/services/EGC_services/IMG_VCGI_LIDARHILLSHD_WM_CACHE_v1/ImageServer)) | On | 0.67 | **New:** now has `minScale` ≈ 1:13.1M — doesn't render at very small/statewide zoom-out (previously unrestricted) |
| 1 | **2023 QL1 DEM COG - TiTiler 11 Zone Elev Style** | TiTiler WebTiledLayer | On | 0.67 | Renamed from "Test Titiler" — more descriptive. `templateUrl` unchanged, still the exact [`titiler-colormap.min.json`](../../dem-color-ramps/11class-feet-aligned/titiler-colormap.min.json). Blend still **soft-light**. **New:** `minScale` ≈ 1:8.4M added |
| 2 | Alpine Trails — VT E911 Other Mapped Features of Interest | [shared FeatureServer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Emergency_FOOTPRINTS_poly_SP_v1/FeatureServer/0) | On | 0.41 | Renamed (title prefix reordered for clarity: theme first, then source) |
| 3 | Golf Courses — VT E911 Other Mapped Features of Interest | same FeatureServer | On | 0.41 | Renamed, same pattern |
| 4 | **Quarries — VT E911 Other Mapped Features of Interest** | same FeatureServer | On | 0.41 | **New layer**, same shared service/pattern as Alpine Trails and Golf Courses |
| 5 | 1ft Lidar Contours — "COPY - Dark Olive" | Vector tile (Esri VT style copy) | Off | — | Unchanged — still a **copy**, not this repo's `style.json` directly; see [dark-olive README](../../contour-styles/dark-olive/README.md) for the confirmed zoom/interval limitation |
| 6 | Human Geography Detail — Blue Water | Esri Living Atlas vector tile | Off | — | **The desaturated variant is gone** — only one Blue Water copy remains now (previously two) |
| 7 | Vermont Significant Wetlands Inventory | [AGOL hosted feature layer](https://services5.arcgis.com/Uzks6LSde6r23wwG/arcgis/rest/services/Vermont_Significant_Wetland_Inventory/FeatureServer/0) | Off | — | Same ANR-hosted VSWI service identified last pass |
| 8 | Buildings 2022 (default style) | Esri Living Atlas vector tile | Off | — | **The recolored `#DCD9D6` copy is gone** — only the default-style version remains now |
| 9 | VT Data — E911 Alpine Ski Lifts | [AGOL hosted feature layer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Emergency_ALPINELIFTS_line_SP_v1/FeatureServer/0) | Off | — | |
| 10 | **VT Mask - GeoJSON Test** | [`vermont-mask.geojson`](../../basemap-styles/human-geography-detail-blue-water/vermont-mask.geojson), hosted via this repo's GitHub Pages | On | — | **New** — the Vermont-crop mask is now applied in this test map. Positioned **below** the label layer (next row), matching the layer-order workaround documented in the [mask README](../../basemap-styles/human-geography-detail-blue-water/README.md#known-limitation-label-text-gets-cut-off-mid-glyph) to avoid cutting labels mid-word |
| 11 | Human Geography Label | Esri Living Atlas vector tile | On | — | Place names — still the one piece of Living Atlas left on |
| 12 | Mountains and Hills — VCGI BASEMAP WM v2 | [ArcGIS MapServer sublayer](https://maps.vcgi.vermont.gov/arcgis/rest/services/VCGI_services/VCGI_BASEMAP_WM_v2/MapServer/4) | Off | — | Same service as last pass, title reordered |
| 13 | **Lake and Pond Labels — VCGI BASEMAP WM CACHE v2** | [ArcGIS MapServer sublayer](https://maps.vcgi.vermont.gov/arcgis/rest/services/VCGI_services/VCGI_BASEMAP_WM_CACHE_v2/MapServer/25) | On | — | **New layer**, and notable: a **VCGI-sourced** place-name label (not Esri Living Atlas) — directly relevant to the architecture gap about needing VCGI's own place-name source instead of Living Atlas, see below |
| 14 | **River and Stream Names — VCGI BASEMAP WM CACHE v2** | [ArcGIS MapServer sublayer](https://maps.vcgi.vermont.gov/arcgis/rest/services/VCGI_services/VCGI_BASEMAP_WM_CACHE_v2/MapServer/30) | On | — | **New layer**, same VCGI-sourced labels pattern as above |

**Removed since the first pass:** VT Protected Lands Database, the
"Blue Water Desaturated" variant, the general-purpose "Human Geography
Detail" layer (roads etc., as distinct from the Label layer), and the
recolored "Buildings 2022 Copy DCD9D6" variant.

## Design decisions (updated)

- **Same core approach as before**: TiTiler-styled DEM + hillshade as the
  actual terrain surface, Esri's basemap imagery switched off except for
  place-name labels.
- **New: VCGI-sourced water-feature labels appear alongside Living Atlas
  labels.** "Lake and Pond Labels" and "River and Stream Names" (both from
  `VCGI_BASEMAP_WM_CACHE_v2`) are a different source than the "Human
  Geography Label" layer — this is a concrete, if partial, step toward
  the VSDI-sourced place-name alternative discussed in
  [`../../architecture/foundational-layers.md` gap #4](../../architecture/foundational-layers.md#gaps--open-questions),
  worth keeping in mind as that gap gets worked on.
- **Vermont-mask now applied**, with the already-documented layer-order
  workaround (mask below labels) in place from the start, rather than
  something to test later.
- **New minScale floors on hillshade and the TiTiler layer** — both now
  stop rendering below roughly 1:8–13M scale. Reason not confirmed with
  you — flagging as observed, not necessarily deliberate performance
  tuning.
- **Several previously-prepared alternates are gone, not just toggled
  off**: the desaturated water variant, Protected Lands, and the
  `#DCD9D6` buildings recolor were removed entirely rather than left
  switched off. Reads like active cleanup ahead of moving to a new test
  version, not just more iteration on this one.
- Quarries joins Alpine Trails and Golf Courses as a third recreation/
  interest theme pulled from the same shared E911 FeatureServer.

## Related

- [`../README.md`](../README.md) — index of all webmap tests
- [`../../dem-color-ramps/11class-feet-aligned/README.md`](../../dem-color-ramps/11class-feet-aligned/README.md)
- [`../../contour-styles/dark-olive/README.md`](../../contour-styles/dark-olive/README.md)
- [`../../basemap-styles/human-geography-detail-blue-water/README.md`](../../basemap-styles/human-geography-detail-blue-water/README.md)
- [`../../data-sources/README.md`](../../data-sources/README.md)
