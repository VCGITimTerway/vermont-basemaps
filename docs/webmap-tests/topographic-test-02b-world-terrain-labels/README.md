# Topographic — Test 02b (World Terrain Labels)

Pulled directly from the web map's JSON via the AGOL sharing REST API,
not hand-described — re-pull if this map changes rather than editing
this table by hand.

**Live embed:** <https://vcgitimterway.github.io/vermont-basemaps/webmap-tests/topographic-test-02b-world-terrain-labels/>
**ArcGIS Online item:** <https://vcgi.maps.arcgis.com/apps/mapviewer/index.html?webmap=8d2975f539db4897bd61cfe2f8ced44c>
**AGOL item title:** "Basemap 2026 - Topographic - Test 02b Physical Topo Light"
**Test extent:** centered roughly -72.35, 43.87 at a statewide view

Save-as copy of [Topographic Test 02](../topographic-test-02-physical-topo-light/README.md)
with one original change (the label layer), since developed further with
a custom label layer stack and layer grouping.

## Basemap

Same as Test 02: **Human Geography Map** (Esri Living Atlas), own "Human
Geography Base" vector tile sub-layer turned **off**.

## Layer groups

Operational layers are organized into three groups, each independently
toggleable (`visibilityMode: independent` — a sublayer's own `visibility`
still governs whether it draws, same as any ungrouped layer):

- **Base Topo** — terrain, protected lands, recreation features, roads,
  buildings, the VT mask, and the state boundary line. Currently an
  **ad-hoc group** (no item ID of its own).
- **Boundaries** — Town Boundaries-Outline + Town Boundaries. This group
  already carries an item ID (`78853d8236e04a1d8d6df5c0f94e7c13`) — the
  same **Group layer item** (`Group Layer - Town Boundaries`) used in
  [Test 02c](../topographic-test-02c-admin/README.md#town-boundaries-group),
  reused here rather than rebuilt.
- **Labels** — all label layers, described below. Currently an **ad-hoc
  group** (no item ID of its own).

Rendering order (bottom to top): Base Topo, then Boundaries, then Labels.

## Layers shown (top to bottom within each group, as returned by the API)

### Base Topo group

| # | Layer | Source | On? | Opacity | Notes |
|---|---|---|---|---|---|
| 0 | Lidar DEM Hillshade | ArcGIS cached ImageServer ([`IMG_VCGI_LIDARHILLSHD_WM_CACHE_v1`](https://maps.vcgi.vermont.gov/arcgis/rest/services/EGC_services/IMG_VCGI_LIDARHILLSHD_WM_CACHE_v1/ImageServer)) | On | 0.4 | No DEM color-ramp layer in this map |
| 1 | Vermont Protected Lands Database | [AGOL hosted FeatureServer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Cadastral_PROTECTEDLND_poly_SP_v2/FeatureServer/0) | On | 0.25 | Filtered to `INT_ORGTYP` = `STAT`/`LOC`/`FED` **or** `DESIGNAT` = `SF`/`SP`/`ML`/`MF`/`MP`/`SL` — see [`protected-lands.md`](../../data-sources/protected-lands.md) |
| 2 | Alpine Trails — VT E911 Other Mapped Features of Interest | [shared FeatureServer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Emergency_FOOTPRINTS_poly_SP_v1/FeatureServer/0) | On | 0.67 | |
| 3 | Golf Courses — VT E911 Other Mapped Features of Interest | same FeatureServer | On | 0.75 | |
| 4 | Quarries — VT E911 Other Mapped Features of Interest | same FeatureServer | On | 0.41 | |
| 5 | 1ft Lidar Contours — "COPY - Dark Olive" | Vector tile (Esri VT style copy) | On | 0.25 | |
| 6 | Human Geography Detail — Blue Water Light Roads | Esri Living Atlas vector tile, VCGI-styled ("Light Roads" style variant) | Off | — | Now includes a dashed trail symbol ported from the base Blue Water style — see [style file](../../basemap-styles/human-geography-detail-blue-water-light-roads) |
| 7 | Vermont Significant Wetlands Inventory | [AGOL hosted feature layer](https://services5.arcgis.com/Uzks6LSde6r23wwG/arcgis/rest/services/Vermont_Significant_Wetland_Inventory/FeatureServer/0) | Off | 0.75 | |
| 8 | Buildings 2022 (White) | Vector tile ("White" style variant) | Off | — | Scale range 1:25,617–1:153 when on |
| 9 | VT Data — E911 Alpine Ski Lifts | [AGOL hosted feature layer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Emergency_ALPINELIFTS_line_SP_v1/FeatureServer/0) | Off | — | |
| 10 | VT Mask - GeoJSON Test | [`vermont-mask.geojson`](../../basemap-styles/human-geography-detail-blue-water/vermont-mask.geojson) | On | — | Positioned below both the Boundaries and Labels groups |
| 11 | VT Data - State Boundary | [AGOL hosted FeatureServer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Boundary_BNDHASH_poly_vtbnd_SP_v1/FeatureServer/0) | On | — | Transparent fill, light gray `#e0e0e0` dashed outline |

### Boundaries group (Group layer item)

| # | Layer | Source | On? | Notes |
|---|---|---|---|---|
| 12 | Town Boundaries-Outline | [AGOL hosted FeatureServer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Boundary_BNDHASH_poly_towns_SP_v1/FeatureServer/0) | On | No fill, wide semi-transparent white halo |
| 13 | Town Boundaries | same FeatureServer | On | Light gray dotted outline, `TOWNNAME` labels — see [`boundaries.md`](../../data-sources/boundaries.md) |

### Labels group

| # | Layer | Source | On? | Notes |
|---|---|---|---|---|
| 14 | World Terrain Reference Labels Light | Esri Living Atlas vector tile (`World_Basemap_v2`), VCGI-styled — same item Test 02c uses (`2345d29f16394e56b5a09500f0c2c3f3`) | On | `minScale` ≈ 1:705,881 — only draws once zoomed in past regional scale |
| 15 | VT Basemap 2026 Town Labels | VCGI vector tile layer, item `c76bdee4d12344fd838bcd7df05de80f` | **Off** | Superseded by row 16; kept in the map but turned off rather than removed |
| 16 | VT Basemap 2026 Town Labels Manual Deconflict | VCGI vector tile layer, item `04faa79cda0446759b7024bb9b46e3ff` — same underlying `Town_Labels` service as row 15, a newer style/data save | On *(presumed — no explicit `visibility` key, but it's the active successor to row 15 per its name and row 15 being explicitly off)* | Vermont municipal names not well-covered by Esri's Living Atlas content, manually deconflicted by hand (many more towns hand-tuned than the earlier attribute-filter approach) rather than via a style `filter` — the current live style has no `filter` at all, so the deconfliction was done upstream of styling (label point selection/placement in the source data) |
| 17 | VT Basemap 2026 City Points WM - Levels 6 7 8 | VCGI vector tile layer, item `a58653bb5d8947b0909ccbdec1cb463f` | On *(presumed — no explicit `visibility` key)* | Scale range 1:6,735,297–1:602,939; three zoom-filtered tiers (statewide/regional/close-in) — see [style file](../../basemap-styles/vt-basemap-2026-city-points) |

## What's different from Test 02

Building on the original single change (swapping Test 02's four label
layers for one Esri-derived label layer):

1. **The label layer is VCGI's own muted style, not Esri's original.**
   "World Terrain Reference Labels Light" — the placename/spot-elevation-muted
   copy also used by [Test 02c](../topographic-test-02c-admin/README.md) —
   shared between both tests rather than duplicated.
2. **A custom Town Labels layer fills a content gap**, not just a zoom
   gap: official Vermont municipal names that Esri's Living Atlas content
   doesn't always carry. It's been through two iterations (an
   attribute-filter approach, then a manually-deconflicted republish —
   row 16 above) as the overlap with World Terrain Reference Labels
   Light's own place content got hand-tuned down. Vector tile layers
   don't share label collision detection across separate items in
   ArcGIS Online — each Vector Tile Layer resolves its own symbol
   placement independently, so two separate vector tile label layers
   will never auto-deconflict with each other the way layers *within*
   one style do. Manual curation (dropping/repositioning overlapping
   names) is the practical workaround; a single VCGI-controlled label
   tileset covering everything would be the structural fix — see
   [`foundational-layers.md`](../../architecture/foundational-layers.md#gaps--open-questions).
3. **A custom City Points layer fills the statewide/regional zoom gap**
   for the same reason (no Vermont-only attribute exists in Esri's
   Living Atlas tiles), tiered across three zoom levels — see
   [`vt-basemap-2026-city-points`](../../basemap-styles/vt-basemap-2026-city-points).
4. **Operational layers are grouped** into Base Topo, Boundaries, and
   Labels (see above). Boundaries reuses the same Group layer item as
   Test 02c; Base Topo and Labels are still ad-hoc groups as of this
   writing.

## Related

- [`../topographic-test-02-physical-topo-light/README.md`](../topographic-test-02-physical-topo-light/README.md) —
  the version this was saved from
- [`../topographic-test-02c-admin/README.md`](../topographic-test-02c-admin/README.md) —
  shares both the "World Terrain Reference Labels Light" item and the
  "Group Layer - Town Boundaries" item
- [`../../basemap-styles/world-terrain-reference-labels-light`](../../basemap-styles/world-terrain-reference-labels-light)
- [`../../basemap-styles/vt-basemap-2026-town-labels`](../../basemap-styles/vt-basemap-2026-town-labels)
- [`../../basemap-styles/vt-basemap-2026-city-points`](../../basemap-styles/vt-basemap-2026-city-points)
- [`../README.md#group-layers`](../README.md#group-layers) — ad-hoc
  groups vs. Group layer items, and the no-propagation caveat
- [`../../data-sources/protected-lands.md`](../../data-sources/protected-lands.md)
- [`../../data-sources/boundaries.md`](../../data-sources/boundaries.md)
- [`../README.md`](../README.md) — index of all webmap tests
