# Topographic — Test 02f (Desaturated Imagery)

Pulled directly from the web map's JSON via the AGOL sharing REST API,
not hand-described — re-pull if this map changes rather than editing
this table by hand.

**Live embed:** <https://vcgitimterway.github.io/vermont-basemaps/webmap-tests/topographic-test-02f-desaturated-imagery/>
**ArcGIS Online item:** <https://vcgi.maps.arcgis.com/apps/mapviewer/index.html?webmap=a6cecec78d114e0e924b7e10cafbfd16>
**AGOL item title:** "VT Basemap 2026 - Desaturated Imagery - Test 02f"
**Test extent:** centered roughly -72.81, 43.95 at a statewide view

Reference example for a **Desaturated Imagery** variant of the
Desaturated configuration — adds a muted orthoimagery layer underneath
desaturated vector-tile styles. Work in progress: some layers are
currently toggled off rather than removed, and most styles inside both
new groups still point at the same Desaturated-specific items Test 02e
uses, except for the main Light Roads style, which now has its own
Imagery-specific save-as — see below.

## Basemap

Same as Test 02e: **Human Geography Map** (Esri Living Atlas), own
"Human Geography Base" vector tile sub-layer turned **off**.

## Layer groups

Three groups:

| Group | Item ID | Notes |
|---|---|---|
| Base Desaturated Imagery | `41b654fbf29441e7bb649ae24d09e921` ("VT Basemap 2026 Base Desaturated Imagery") | Save-as of [Base Desaturated](../topographic-test-02e-desaturated/README.md#base-desaturated-group) — adds a World Imagery layer, otherwise the same composition with some layers currently toggled off — see below |
| Boundaries | `78853d8236e04a1d8d6df5c0f94e7c13` ("VT Basemap 2026 Town Boundaries") | Same item reused from every other configuration |
| Labels Desaturated Imagery | `54e31a3ce1a54922896fea2f4b05124b` ("VT Basemap 2026 Labels Desaturated Imagery") | Save-as of [Labels Desaturated](../topographic-test-02e-desaturated/README.md#labels-desaturated-group) — same three sub-layers, same items, no style changes yet |

## Layers shown (top to bottom within each group, as returned by the API)

### Base Desaturated Imagery group

| # | Layer | Source | On? | Opacity | Notes |
|---|---|---|---|---|---|
| 0 | World Imagery | [Esri World Imagery](https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer), item `10df2279f9684e4a9f6a7f08febac2a9` | On | 0.4 | New layer, not present in Test 02e — blended at reduced opacity over the rest of the group to give the desaturated basemap a muted photographic texture, rather than full-color aerial imagery. Minimum scale 1:97,058 — hidden at statewide/regional zoom, only appears once zoomed in past that |
| 1 | Vermont Protected Lands Database | [AGOL hosted FeatureServer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Cadastral_PROTECTEDLND_poly_SP_v2/FeatureServer/0) | On | 0.25 | Filtered to `INT_ORGTYP` = `STAT`/`LOC`/`FED` **or** `DESIGNAT` = `SF`/`SP`/`ML`/`MF`/`MP`/`SL` — see [`protected-lands.md`](../../data-sources/protected-lands.md) |
| 2 | Alpine Trails — VT E911 Other Mapped Features of Interest | [shared FeatureServer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Emergency_FOOTPRINTS_poly_SP_v1/FeatureServer/0) | **Off** | 0.67 | On in Test 02e — toggled off here for now |
| 3 | Golf Courses — VT E911 Other Mapped Features of Interest | same FeatureServer | **Off** | 0.75 | On in Test 02e — toggled off here for now |
| 4 | Quarries — VT E911 Other Mapped Features of Interest | same FeatureServer | **Off** | 0.41 | On in Test 02e — toggled off here for now |
| 5 | 1ft Lidar Contours — Dark Olive DASHED | Vector tile, item `1dc25cb00c084249b3ec5dea89fbb752` | On | 0.2 | Same item as Test 02e — see [style folder](../../contour-styles/dark-olive-dashed/README.md) |
| 6 | VT Data — E911 Driveways | [AGOL hosted FeatureServer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Emergency_DW_line_SP_v1/FeatureServer/0) | Off | — | Same as Test 02e |
| 7 | Human Geography Detail — Blue Water Light Roads Desat | Esri Living Atlas vector tile, item `bb6f7b84a0244a75909cff78f2883e6c` | **Off** | — | Hidden — superseded by row 8, kept in the map rather than removed |
| 8 | Human Geography Detail — Blue Water **Light Roads DESAT IMAGERY** | Esri Living Atlas vector tile, item `8a665305420b4fccafd43059bc5c73c4` | On | — | Save-as of Light Roads Desat, specific to this configuration — see [style file](../../basemap-styles/human-geography-detail-blue-water-light-roads-desat-imagery) |
| 9 | Vermont Significant Wetlands Inventory | [AGOL hosted feature layer](https://services5.arcgis.com/Uzks6LSde6r23wwG/arcgis/rest/services/Vermont_Significant_Wetland_Inventory/FeatureServer/0) | On | 0.75 | Same `#5eabc4` symbol color as Test 02e |
| 10 | Buildings 2022 (White) | Vector tile, item `b9f60490ca3d4a3f8d6af6c80e4b8c96`, Desaturated-specific fork | On | — | Same item as Test 02e, scale range narrowed here to 1:23,411–1:5,331 — see [style file](../../basemap-styles/buildings-2022-white-desat) |
| 11 | VT Data — E911 Alpine Ski Lifts | [AGOL hosted feature layer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Emergency_ALPINELIFTS_line_SP_v1/FeatureServer/0) | On | — | Same as Test 02e |
| 12 | VT Mask - GeoJSON Test | [`vermont-mask.geojson`](../../basemap-styles/human-geography-detail-blue-water/vermont-mask.geojson) | On | — | Same as Test 02e |
| 13 | VT Data - State Boundary | [AGOL hosted FeatureServer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Boundary_BNDHASH_poly_vtbnd_SP_v1/FeatureServer/0) | On | — | Same as Test 02e |
| 14 | VT Basemap 2026 Context Boundaries **Desaturated** | VCGI vector tile layer, item `a6a4272f7f904905b13644e20de6f6ea` | On *(presumed — no explicit `visibility` key)* | — | Same item as Test 02e, water now `#d4dadc` — see [style file](../../basemap-styles/vt-basemap-2026-context-boundaries-desat) |

### Boundaries group (Group layer item)

Identical to every other configuration — see
[Test 02b's writeup](../topographic-test-02b-world-terrain-labels/README.md#boundaries-group-group-layer-item).

### Labels Desaturated Imagery group

| # | Layer | Source | On? | Notes |
|---|---|---|---|---|
| 15 | World Terrain Reference Labels Light **Desaturated** | VCGI vector tile layer, item `8c0999ee861c4c66801b6bcb1bc0ffd6` | On *(presumed)* | Same item as Test 02e — see [style file](../../basemap-styles/world-terrain-reference-labels-light-desat) |
| 16 | VT Basemap 2026 Town Labels Manual Deconflict **DESAT** | VCGI vector tile layer, item `70bdd74a5472484eaa169b583a642237` | On *(presumed)* | Same item as Test 02e |
| 17 | VT Basemap 2026 City Points WM - Levels 6 7 8 **DESAT** | VCGI vector tile layer, item `77b6f532de0b4da091cbc07f1d38a75c` | On *(presumed)* | Same item as Test 02e |

## What's different from Test 02e (Desaturated)

- A **World Imagery** layer is added at the top of the Base group, at
  0.4 opacity (minimum scale 1:97,058), giving the basemap a muted
  aerial-photo texture.
- **Alpine Trails, Golf Courses, and Quarries** are currently toggled
  off (on in Test 02e) — work in progress, may be removed rather than
  re-enabled.
- **Light Roads** has its own Imagery-specific save-as here (item
  `8a665305420b4fccafd43059bc5c73c4`, "...Light Roads DESAT IMAGERY") —
  see [style file](../../basemap-styles/human-geography-detail-blue-water-light-roads-desat-imagery)
  for the water zoom-cutoff change. The original Light Roads Desat item
  is still in the map but hidden.
- **Buildings 2022** keeps the same style item as Test 02e, but its
  scale range is narrower here (1:23,411–1:5,331 vs. Test 02e's
  1:23,411–1:12) — set at the webmap layer level, not in the style. The
  zoomed-out bound (1:23,411, zoom ≈ 14.625) is the one the Light Roads
  DESAT IMAGERY water `maxzoom` above matches — unchanged.
- Everything else is currently identical to Test 02e.

## Related

- [`../topographic-test-02e-desaturated/README.md`](../topographic-test-02e-desaturated/README.md) —
  the Desaturated configuration this one is based on
- [`../README.md#reusable-group-layers`](../README.md#reusable-group-layers) —
  all configurations, with stacking order
- [`../../basemap-styles/README.md`](../../basemap-styles/README.md) —
  index of every style variant
- [`../README.md`](../README.md) — index of all webmap tests
