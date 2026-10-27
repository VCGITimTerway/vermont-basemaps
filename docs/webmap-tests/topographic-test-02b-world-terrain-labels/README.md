# Topographic — Test 02b (World Terrain Labels)

Pulled directly from the web map's JSON via the AGOL sharing REST API,
not hand-described — re-pull if this map changes rather than editing
this table by hand.

**Live embed:** <https://vcgitimterway.github.io/vermont-basemaps/webmap-tests/topographic-test-02b-world-terrain-labels/>
**ArcGIS Online item:** <https://vcgi.maps.arcgis.com/apps/mapviewer/index.html?webmap=8d2975f539db4897bd61cfe2f8ced44c>
**AGOL item title:** "Basemap 2026 - Topographic - Test 02b Physical Topo Light"
**Test extent:** centered -72.353621, 43.894055 at 1:2,311,162 — a
statewide view, consistent with this test's current focus on the
statewide/regional label handoff (see below)

Save-as copy of [Topographic Test 02](../topographic-test-02-physical-topo-light/README.md)
with one original change (the label layer), now further developed with
a new custom label layer and layer grouping.

## Basemap

Same as Test 02: **Human Geography Map** (Esri Living Atlas), own "Human
Geography Base" vector tile sub-layer turned **off**.

## Layer groups

Operational layers are organized into two groups, each independently
toggleable (`visibilityMode: independent` — a sublayer's own `visibility`
still governs whether it draws, same as any ungrouped layer):

- **Base** — terrain, protected lands, recreation features, roads,
  buildings, the VT mask, and the state boundary line
- **Labels** — the two label layers, described below

The Labels group renders above the Base group.

## Layers shown (top to bottom within each group, as returned by the API)

### Base group

| # | Layer | Source | On? | Opacity | Notes |
|---|---|---|---|---|---|
| 0 | Lidar DEM Hillshade | ArcGIS cached ImageServer ([`IMG_VCGI_LIDARHILLSHD_WM_CACHE_v1`](https://maps.vcgi.vermont.gov/arcgis/rest/services/EGC_services/IMG_VCGI_LIDARHILLSHD_WM_CACHE_v1/ImageServer)) | On | 0.4 | No DEM color-ramp layer in this map |
| 1 | Vermont Protected Lands Database | [AGOL hosted FeatureServer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Cadastral_PROTECTEDLND_poly_SP_v2/FeatureServer/0) | On | 0.25 | Filtered to `INT_ORGTYP` = `STAT`/`LOC`/`FED` **or** `DESIGNAT` = `SF`/`SP`/`ML`/`MF`/`MP`/`SL` — see [`protected-lands.md`](../../data-sources/protected-lands.md) |
| 2 | Alpine Trails — VT E911 Other Mapped Features of Interest | [shared FeatureServer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Emergency_FOOTPRINTS_poly_SP_v1/FeatureServer/0) | On | 0.67 | |
| 3 | Golf Courses — VT E911 Other Mapped Features of Interest | same FeatureServer | On | 0.75 | |
| 4 | Quarries — VT E911 Other Mapped Features of Interest | same FeatureServer | On | 0.41 | |
| 5 | 1ft Lidar Contours — "COPY - Dark Olive" | Vector tile (Esri VT style copy) | On | 0.25 | |
| 6 | Human Geography Detail — Blue Water Light Roads | Esri Living Atlas vector tile, VCGI-styled ("Light Roads" style variant) | Off | — | |
| 7 | Vermont Significant Wetlands Inventory | [AGOL hosted feature layer](https://services5.arcgis.com/Uzks6LSde6r23wwG/arcgis/rest/services/Vermont_Significant_Wetland_Inventory/FeatureServer/0) | Off | 0.75 | |
| 8 | Buildings 2022 (White) | Vector tile ("White" style variant) | Off | — | Scale range 1:25,617–1:153 when on |
| 9 | VT Data — E911 Alpine Ski Lifts | [AGOL hosted feature layer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Emergency_ALPINELIFTS_line_SP_v1/FeatureServer/0) | Off | — | |
| 10 | VT Mask - GeoJSON Test | [`vermont-mask.geojson`](../../basemap-styles/human-geography-detail-blue-water/vermont-mask.geojson) | On | — | Positioned below both the state boundary line and the Labels group |
| 11 | **VT Data - State Boundary** | [AGOL hosted FeatureServer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Boundary_BNDHASH_poly_vtbnd_SP_v1/FeatureServer/0) — new to this test | On *(presumed — no explicit `visibility` key, but it carries a deliberate custom symbol: transparent fill, light gray `#e0e0e0` dashed outline at 1.5px, not a default/reference styling)* | — | Same source service the VT Mask's hole geometry is derived from (see [mask README](../../basemap-styles/human-geography-detail-blue-water/README.md)); here drawn as a visible state-outline line, not used for masking |

### Labels group

| # | Layer | Source | On? | Notes |
|---|---|---|---|---|
| 12 | World Terrain Reference Labels Light | Esri Living Atlas vector tile (`World_Basemap_v2`), VCGI-styled — **the same item Test 02c uses** (`2345d29f16394e56b5a09500f0c2c3f3`), not the original unmuted "World Terrain Reference Labels" item Test 01b/02b used previously | On | Layer `minScale` ≈ 1:705,881 — only draws once zoomed in past regional scale |
| 13 | VT Basemap 2026 City Points WM | VCGI-authored vector tile service (AGOL item `e1936ffeaa754bc696043392cf091236`, owner `Publisher_VCGI`) — new custom layer | On *(presumed — no explicit `visibility` key, but the layer's whole purpose per its own description is to fill the statewide/regional gap left by row 12, and its scale range brackets that gap precisely)* | Scale range 1:6,294,116–1:764,705 — covers statewide down to regional zoom, handing off to row 12 just before its 1:705,881 cutoff |

## What's different from Test 02

Three things, building on the original single change (swapping Test 02's
four label layers for one Esri-derived label layer):

1. **The label layer is now VCGI's own muted style, not Esri's original.**
   Test 02b originally reused the same unmuted "World Terrain Reference
   Labels" item as Test 01b. It now uses the "World Terrain Reference
   Labels Light" item — the placename/spot-elevation-muted copy created
   for [Test 02c](../topographic-test-02c-admin/README.md) — shared
   between both tests rather than duplicated.
2. **A new City Points label layer fills the statewide/regional gap.**
   The World Terrain Reference Labels Light layer (and the Esri Living
   Atlas content it derives from) has no attribute distinguishing
   Vermont from non-Vermont places, so at statewide/regional zoom it
   would otherwise show many non-Vermont city labels alongside Vermont
   ones (see [`../../basemap-styles/world-terrain-reference-labels-light`](../../basemap-styles/world-terrain-reference-labels-light)
   for the underlying limitation). The new VCGI-authored City Points
   layer is scale-restricted to exactly that statewide/regional range
   and shows only Vermont cities, handing off to the Esri-derived layer
   once zoomed in far enough that non-Vermont content falls out of view.
3. **Operational layers are now grouped** into "Base" and "Labels" (see
   above), and a new "VT Data - State Boundary" line layer has been added
   to the Base group.

The cross-platform tradeoff discussed in
[Test 01b's writeup](../topographic-test-01b-world-terrain-labels/README.md#whats-different-from-test-01)
still applies to the Esri-derived portion of the label content: licensed
Esri content that isn't exportable as-is, now paired with a VCGI-owned
layer (City Points) that is.

## Related

- [`../topographic-test-02-physical-topo-light/README.md`](../topographic-test-02-physical-topo-light/README.md) —
  the version this was saved from
- [`../topographic-test-02c-admin/README.md`](../topographic-test-02c-admin/README.md) —
  shares the same "World Terrain Reference Labels Light" item
- [`../../basemap-styles/world-terrain-reference-labels-light`](../../basemap-styles/world-terrain-reference-labels-light) —
  the shared muted label style, including the Vermont-only-labels
  limitation that motivated City Points
- [`../../data-sources/protected-lands.md`](../../data-sources/protected-lands.md)
- [`../README.md`](../README.md) — index of all webmap tests
