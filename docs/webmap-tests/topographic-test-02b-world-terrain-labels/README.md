# Topographic — Test 02b (World Terrain Labels)

Pulled directly from the web map's JSON via the AGOL sharing REST API,
not hand-described — re-pull if this map changes rather than editing
this table by hand.

**Live embed:** <https://vcgitimterway.github.io/vermont-basemaps/webmap-tests/topographic-test-02b-world-terrain-labels/>
**ArcGIS Online item:** <https://vcgi.maps.arcgis.com/apps/mapviewer/index.html?webmap=8d2975f539db4897bd61cfe2f8ced44c>
**AGOL item title:** "VT Basemap 2026 - Base Topo - Test 02b"
**Test extent:** centered roughly -72.35, 43.87 at a statewide view

Save-as copy of an earlier physical-topo-light test webmap, with one
original change (the label layer), since developed further with a
custom label layer stack, surrounding-context boundaries, and layer
grouping.

## Basemap

Same as Test 02: **Human Geography Map** (Esri Living Atlas), own "Human
Geography Base" vector tile sub-layer turned **off**.

## Layer groups

Operational layers are organized into three groups, each independently
toggleable (`visibilityMode: independent` — a sublayer's own `visibility`
still governs whether it draws, same as any ungrouped layer). All three
are now standalone, public **Group layer items** — addable to other web
maps directly, not just ad-hoc groups local to this one (see [Group
layers](../README.md#group-layers) for what that does and doesn't give
you):

| Group | Item ID | Notes |
|---|---|---|
| **Base Topo** | `d5173a686f4844fd8584cfecb37ab940` ("VT Basemap 2026 Base Topo") | Terrain, protected lands, recreation features, roads, buildings, the VT mask, the state boundary line, and surrounding-context boundaries |
| **Boundaries** | `78853d8236e04a1d8d6df5c0f94e7c13` ("VT Basemap 2026 Town Boundaries") | Same item reused from [Test 02c](../topographic-test-02c-admin/README.md#town-boundaries-group); this map restricts its visible range to below 1:897,547 |
| **Labels** | `0ff87dab7daf4141a5e95a2f8be0715e` ("VT Basemap 2026 Labels") | All label layers, described below |

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
| 6 | Human Geography Detail — Blue Water Light Roads | Esri Living Atlas vector tile, VCGI-styled ("Light Roads" style variant) | Off | — | Includes a dashed trail symbol ported from the base Blue Water style — see [style file](../../basemap-styles/human-geography-detail-blue-water-light-roads) |
| 7 | Vermont Significant Wetlands Inventory | [AGOL hosted feature layer](https://services5.arcgis.com/Uzks6LSde6r23wwG/arcgis/rest/services/Vermont_Significant_Wetland_Inventory/FeatureServer/0) | Off | 0.75 | |
| 8 | Buildings 2022 (White) | Vector tile ("White" style variant) | Off | — | Scale range 1:25,617–1:153 when on |
| 9 | VT Data — E911 Alpine Ski Lifts | [AGOL hosted feature layer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Emergency_ALPINELIFTS_line_SP_v1/FeatureServer/0) | Off | — | |
| 10 | VT Mask - GeoJSON Test | [`vermont-mask.geojson`](../../basemap-styles/human-geography-detail-blue-water/vermont-mask.geojson) | On | — | Scale range 1:0–1:794,605. Positioned below both the Boundaries and Labels groups |
| 11 | VT Data - State Boundary | [AGOL hosted FeatureServer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Boundary_BNDHASH_poly_vtbnd_SP_v1/FeatureServer/0) | On | — | Transparent fill, light gray `#e0e0e0` dashed outline |
| 12 | VT Basemap 2026 Context Boundaries | VCGI vector tile layer, item `07f27428b81049d4b250ccdb457be37a` | On *(presumed — no explicit `visibility` key)* | — | Surrounding state/international boundary lines + water, scale range 1:0–1:794,116 (matches the VT Mask's own cutoff) — see [style file](../../basemap-styles/vt-basemap-2026-context-boundaries) |

### Boundaries group (Group layer item)

| # | Layer | Source | On? | Notes |
|---|---|---|---|---|
| 13 | Town Boundaries-Outline | [AGOL hosted FeatureServer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Boundary_BNDHASH_poly_towns_SP_v1/FeatureServer/0) | On | No fill, wide semi-transparent white halo |
| 14 | Town Boundaries | same FeatureServer | On | Light gray dotted outline, `TOWNNAME` labels — see [`boundaries.md`](../../data-sources/boundaries.md) |

### Labels group (Group layer item)

| # | Layer | Source | On? | Notes |
|---|---|---|---|---|
| 15 | World Terrain Reference Labels Light | Esri Living Atlas vector tile (`World_Basemap_v2`), VCGI-styled — same item Test 02c uses (`2345d29f16394e56b5a09500f0c2c3f3`) | On | `minScale` ≈ 1:705,881 — only draws once zoomed in past regional scale |
| 16 | VT Basemap 2026 Town Labels | VCGI vector tile layer, item `c76bdee4d12344fd838bcd7df05de80f` | **Off** | Superseded by row 17; kept in the map but turned off rather than removed |
| 17 | VT Basemap 2026 Town Labels Manual Deconflict | VCGI vector tile layer, item `04faa79cda0446759b7024bb9b46e3ff` — same underlying `Town_Labels` service as row 16, a newer style/data save | On *(presumed — no explicit `visibility` key, but it's the active successor to row 16)* | Vermont municipal names manually deconflicted by hand against World Terrain Reference Labels Light's own content — the live style has no `filter`, so the deconfliction was done upstream in the label data/points, not via styling |
| 18 | VT Basemap 2026 City Points WM - Levels 6 7 8 | VCGI vector tile layer, item `a58653bb5d8947b0909ccbdec1cb463f` | On *(presumed — no explicit `visibility` key)* | Scale range 1:6,735,297–1:602,939; three zoom-filtered tiers (statewide/regional/close-in) — see [style file](../../basemap-styles/vt-basemap-2026-city-points) |

## What's different from Test 02

Building on the original single change (swapping Test 02's four label
layers for one Esri-derived label layer):

1. **The label layer is VCGI's own muted style, not Esri's original.**
   "World Terrain Reference Labels Light" — shared with
   [Test 02c](../topographic-test-02c-admin/README.md).
2. **A custom Town Labels layer fills a content gap**, not just a zoom
   gap: official Vermont municipal names that Esri's Living Atlas content
   doesn't always carry. It's been through two published iterations (an
   attribute-filter approach, then a manually-deconflicted republish —
   row 17 above). Vector tile layers don't share label collision
   detection across separate items in ArcGIS Online — each resolves its
   own symbol placement independently — so manual curation is the
   practical workaround; a single VCGI-controlled label tileset covering
   everything would be the structural fix — see
   [`foundational-layers.md`](../../architecture/foundational-layers.md#gaps--open-questions).
3. **A custom City Points layer fills the statewide/regional zoom gap**
   for the same underlying reason (no Vermont-only attribute exists in
   Esri's Living Atlas tiles), tiered across three zoom levels.
4. **A Context Boundaries layer gives statewide-zoom geographic context**
   without showing non-Vermont roads: the VT Mask hides all Blue Water
   Light Roads content outside Vermont at statewide zoom (to avoid
   showing non-VT road clutter), which previously meant no surrounding
   context at all. This new layer reuses the same `World_Basemap_v2`
   source's boundary-line and water sub-layers (present in the base
   style but disabled by default), restyled to a light, USGS-inspired
   dash convention, and positioned above the mask so it isn't hidden by
   it.
5. **Operational layers are grouped** into Base Topo, Boundaries, and
   Labels — all three are now saved, public Group layer items (see
   above), not ad-hoc groups.

## Related

- [`../topographic-test-02c-admin/README.md`](../topographic-test-02c-admin/README.md) —
  shares both the "World Terrain Reference Labels Light" item and the
  "VT Basemap 2026 Town Boundaries" item
- [`../../basemap-styles/world-terrain-reference-labels-light`](../../basemap-styles/world-terrain-reference-labels-light)
- [`../../basemap-styles/vt-basemap-2026-town-labels`](../../basemap-styles/vt-basemap-2026-town-labels)
- [`../../basemap-styles/vt-basemap-2026-city-points`](../../basemap-styles/vt-basemap-2026-city-points)
- [`../../basemap-styles/vt-basemap-2026-context-boundaries`](../../basemap-styles/vt-basemap-2026-context-boundaries)
- [`../README.md#group-layers`](../README.md#group-layers) — ad-hoc
  groups vs. Group layer items, and the no-propagation caveat
- [`../../data-sources/protected-lands.md`](../../data-sources/protected-lands.md)
- [`../../data-sources/boundaries.md`](../../data-sources/boundaries.md)
- [`../README.md`](../README.md) — index of all webmap tests
