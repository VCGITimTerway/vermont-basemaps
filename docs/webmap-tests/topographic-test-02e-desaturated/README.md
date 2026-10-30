# Topographic — Test 02e (Desaturated)

Pulled directly from the web map's JSON via the AGOL sharing REST API,
not hand-described — re-pull if this map changes rather than editing
this table by hand.

**Live embed:** <https://vcgitimterway.github.io/vermont-basemaps/webmap-tests/topographic-test-02e-desaturated/>
**ArcGIS Online item:** <https://vcgi.maps.arcgis.com/apps/mapviewer/index.html?webmap=fcda751408f64e42a8371b797524f769>
**AGOL item title:** "Basemap 2026 Test 02e Desaturated"
**Test extent:** centered roughly -72.51, 43.88 at a statewide view

Reference example for the **Desaturated** Group Layer configuration — a
grayscale/monochromatic take on the basemap (MapTiler Positron is the
visual reference), alongside Base Topo and Base. Same operational
structure as those two, but with desaturated copies of the vector-tile
styles substituted in.

## Basemap

Same as Test 02/02b/02d: **Human Geography Map** (Esri Living Atlas),
own "Human Geography Base" vector tile sub-layer turned **off**.

## Layer groups

Three groups:

| Group | Item ID | Notes |
|---|---|---|
| Base Desaturated | `024fe4874e67434d8987e580300b228c` ("VT Basemap 2026 Base Desaturated") | Same composition as [Base](../topographic-test-02d-base/README.md#base-group), with desaturated vector-tile styles substituted in — see below |
| Boundaries | `78853d8236e04a1d8d6df5c0f94e7c13` ("VT Basemap 2026 Town Boundaries") | **Same, non-desaturated item** reused from Test 02b/02c/02d — its existing light-gray/white palette was already close enough to the desaturated target that no separate copy was made |
| Labels Desaturated | `ceaef1a3a4744f8e99f05f9f3148443e` ("VT Basemap 2026 Labels Desaturated") | Desaturated World Terrain Reference Labels Light, plus the same Town Labels and City Points items reused from the Labels group — see below |

## Layers shown (top to bottom within each group, as returned by the API)

### Base Desaturated group

| # | Layer | Source | On? | Opacity | Notes |
|---|---|---|---|---|---|
| 0 | Vermont Protected Lands Database | [AGOL hosted FeatureServer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Cadastral_PROTECTEDLND_poly_SP_v2/FeatureServer/0) | On | 0.25 | Filtered to `INT_ORGTYP` = `STAT`/`LOC`/`FED` **or** `DESIGNAT` = `SF`/`SP`/`ML`/`MF`/`MP`/`SL` — see [`protected-lands.md`](../../data-sources/protected-lands.md) |
| 1 | Alpine Trails — VT E911 Other Mapped Features of Interest | [shared FeatureServer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Emergency_FOOTPRINTS_poly_SP_v1/FeatureServer/0) | On | 0.67 | |
| 2 | Golf Courses — VT E911 Other Mapped Features of Interest | same FeatureServer | On | 0.75 | |
| 3 | Quarries — VT E911 Other Mapped Features of Interest | same FeatureServer | On | 0.41 | |
| 4 | 1ft Lidar Contours — "COPY - Dark Olive" | Vector tile (Esri VT style copy, not a desaturated variant) | On | 0.25 | |
| 5 | Human Geography Detail — Blue Water **Light Roads Desat** | Esri Living Atlas vector tile, VCGI-styled | On | — | Water fill/line desaturated to `#c2c8ca` (Positron-derived) — see [style file](../../basemap-styles/human-geography-detail-blue-water-light-roads-desat) |
| 6 | Vermont Significant Wetlands Inventory | [AGOL hosted feature layer](https://services5.arcgis.com/Uzks6LSde6r23wwG/arcgis/rest/services/Vermont_Significant_Wetland_Inventory/FeatureServer/0) | Off | 0.75 | Symbol color set to `#5eabc4` (hue preserved from the original `#00AEEF`, saturation roughly halved) — a deliberate exception to the otherwise near-monochrome palette, since wetlands are a regulatory/thematic feature where losing the color cue would reduce usability |
| 7 | Buildings 2022 (White) | Vector tile ("White" style variant, not a desaturated variant) | Off | — | Scale range 1:25,617–1:153 when on |
| 8 | VT Data — E911 Alpine Ski Lifts | [AGOL hosted feature layer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Emergency_ALPINELIFTS_line_SP_v1/FeatureServer/0) | Off | — | |
| 9 | VT Mask - GeoJSON Test | [`vermont-mask.geojson`](../../basemap-styles/human-geography-detail-blue-water/vermont-mask.geojson) | On | — | Scale range 1:0–1:794,605 |
| 10 | VT Data - State Boundary | [AGOL hosted FeatureServer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Boundary_BNDHASH_poly_vtbnd_SP_v1/FeatureServer/0) | On | — | Transparent fill, light gray `#e0e0e0` dashed outline — already neutral, not re-styled |
| 11 | VT Basemap 2026 Context Boundaries **Desaturated** | VCGI vector tile layer, item `a6a4272f7f904905b13644e20de6f6ea` | On *(presumed — no explicit `visibility` key)* | — | Water desaturated to the same `#c2c8ca`; boundary-line grays unchanged — see [style file](../../basemap-styles/vt-basemap-2026-context-boundaries-desat). Scale range extends to 1:867,647 here (vs. 1:794,117 in the non-desaturated version) |

### Boundaries group (Group layer item)

Identical to Base Topo/Base — see
[Test 02b's writeup](../topographic-test-02b-world-terrain-labels/README.md#boundaries-group-group-layer-item).
Not re-styled for this configuration.

### Labels Desaturated group

| # | Layer | Source | On? | Notes |
|---|---|---|---|---|
| 12 | World Terrain Reference Labels Light **Desaturated** | VCGI vector tile layer, item `8c0999ee861c4c66801b6bcb1bc0ffd6` | On *(presumed — no explicit `visibility` key)* | All water-feature label text (lakes, rivers, bays, marine/ocean, ferry route names) desaturated to `#9DA9B1`; marine label halos normalized to the standard `#fcfcfa` — see [style file](../../basemap-styles/world-terrain-reference-labels-light-desat). `minScale` ≈ 1:691,175 |
| 13 | VT Basemap 2026 Town Labels Manual Deconflict | VCGI vector tile layer, item `04faa79cda0446759b7024bb9b46e3ff` — **same item reused**, not a desaturated copy | On *(presumed)* | Town labels are already a neutral `#505050`, so no separate desaturated version was needed. Unlike Base Topo/Base's Labels group, the superseded (Off) earlier Town Labels item isn't carried along here |
| 14 | VT Basemap 2026 City Points WM - Levels 6 7 8 | VCGI vector tile layer, item `a58653bb5d8947b0909ccbdec1cb463f` — **same item reused** | On *(presumed)* | Already neutral `#505050`; no desaturated copy needed |

## What's different from Base Topo / Base

Every vector-tile style with a saturated color (water fills/lines,
water-feature labels, ferry-route labels) has a desaturated sibling
substituted in; everything already neutral (Town Boundaries, Town
Labels, City Points, State Boundary) is reused as-is rather than
duplicated. The one deliberate exception is the Wetlands Inventory
symbol, kept at a reduced-but-still-visible saturation (`#5eabc4`) so
the regulatory/ecological meaning of the symbol isn't lost — see the
layer table above for the reasoning.

## Related

- [`../topographic-test-02b-world-terrain-labels/README.md`](../topographic-test-02b-world-terrain-labels/README.md) —
  the Base Topo configuration
- [`../topographic-test-02d-base/README.md`](../topographic-test-02d-base/README.md) —
  the Base configuration this one's structure most directly parallels
- [`../README.md#reusable-group-layers`](../README.md#reusable-group-layers) —
  all three configurations (Desaturated, Base, Base Topo), with stacking
  order
- [`../../basemap-styles/README.md`](../../basemap-styles/README.md) —
  index of every desaturated style variant and its exact color changes
- [`../README.md`](../README.md) — index of all webmap tests
