# Topographic — Test 02c (Physical Topo Light Admin)

Pulled directly from the web map's JSON via the AGOL sharing REST API,
not hand-described — re-pull if this map changes rather than editing
this table by hand.

**Live embed:** <https://vcgitimterway.github.io/vermont-basemaps/webmap-tests/topographic-test-02c-admin/>
**ArcGIS Online item:** <https://vcgi.maps.arcgis.com/apps/mapviewer/index.html?webmap=c204789fd709456aaad6749f8d4188eb>
**AGOL item title:** "Basemap 2026 - Topographic - Test 02c Physical Topo Light Admin"
**Test extent:** centered -72.5728, 44.2647 at 1:9,028 — a closer-in,
town-scale extent than Test 02/02b, consistent with this test's purpose
(showing municipal boundaries and sample thematic data, both of which
only render at this kind of zoom — see the table below)

Save-as copy of [Topographic Test 02b](../topographic-test-02b-world-terrain-labels/README.md)
with two additions: a Town Boundaries layer, and a sample thematic
point/line/polygon layer demonstrating the basemap's intended use as a
muted background for user-added data.

## Basemap

Same as Test 02/02b: **Human Geography Map** (Esri Living Atlas), own
"Human Geography Base" vector tile sub-layer turned **off**.

## Layers shown (top to bottom as returned by the API)

| # | Layer | Source | On? | Opacity | Notes |
|---|---|---|---|---|---|
| 0 | Lidar DEM Hillshade | ArcGIS cached ImageServer ([`IMG_VCGI_LIDARHILLSHD_WM_CACHE_v1`](https://maps.vcgi.vermont.gov/arcgis/rest/services/EGC_services/IMG_VCGI_LIDARHILLSHD_WM_CACHE_v1/ImageServer)) | On | 0.4 | Same as Test 02/02b — no DEM color-ramp layer in this map either |
| 1 | Vermont Protected Lands Database | [AGOL hosted FeatureServer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Cadastral_PROTECTEDLND_poly_SP_v2/FeatureServer/0) | On | 0.25 | Filtered to `INT_ORGTYP` = State, Municipal, or Federal — same as Test 02/02b (see [`protected-lands.md`](../../data-sources/protected-lands.md)) |
| 2 | Alpine Trails — VT E911 Other Mapped Features of Interest | [shared FeatureServer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Emergency_FOOTPRINTS_poly_SP_v1/FeatureServer/0) | On | 0.67 | Opacity raised from 0.41 (Test 02/02b) to 0.67 in this test |
| 3 | Golf Courses — VT E911 Other Mapped Features of Interest | same FeatureServer | On | 0.75 | |
| 4 | Quarries — VT E911 Other Mapped Features of Interest | same FeatureServer | On | 0.41 | |
| 5 | 1ft Lidar Contours — "COPY - Dark Olive" | Vector tile (Esri VT style copy) | Off | 0.25 | |
| 6 | Human Geography Detail — Blue Water Light Roads | Esri Living Atlas vector tile, VCGI-styled (same "Light Roads" style variant as Test 02/02b) | Off | — | |
| 7 | Vermont Significant Wetlands Inventory | [AGOL hosted feature layer](https://services5.arcgis.com/Uzks6LSde6r23wwG/arcgis/rest/services/Vermont_Significant_Wetland_Inventory/FeatureServer/0) | Off | 0.75 | |
| 8 | Buildings 2022 (White) | Vector tile (same "White" style variant as Test 02/02b) | Off | — | |
| 9 | VT Data — E911 Alpine Ski Lifts | [AGOL hosted feature layer](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Emergency_ALPINELIFTS_line_SP_v1/FeatureServer/0) | Off | — | |
| 10 | VT Mask - GeoJSON Test | [`vermont-mask.geojson`](../../basemap-styles/human-geography-detail-blue-water/vermont-mask.geojson) | On | — | Positioned below both the Town Boundaries and label layers (same label-clipping reasoning as prior tests) |
| 11 | **Town Boundaries Group** | [Group layer item](#town-boundaries-group) wrapping two views of the same VCGI municipal boundary service | On | — | Saved as a standalone, reusable **Group layer item** (`Group Layer - Town Boundaries`, item `78853d8236e04a1d8d6df5c0f94e7c13`, public) — addable to other web maps directly, not just an ad-hoc group local to this map (see [Group layers](../README.md#group-layers)). Group has no `minScale` restriction of its own beyond 1:196,470 (hidden when zoomed out further than that); see below |
| 12 | **World Terrain Reference Labels Light** | Esri Living Atlas vector tile (`World_Basemap_v2`), VCGI-styled — **a different, newer item than Test 01b/02b's label layer**, not a reused copy | On | — | This is the muted-text label style edited earlier this session (placename and spot-elevation colors lightened to `#505050`) — see [`../../basemap-styles/`](../../basemap-styles/world-terrain-reference-labels-light). Layer-level `minScale` ≈ 1:1,676,470 (hidden when zoomed out past regional scale) |
| 13 | **Thematic Features Example** | Inline ArcGIS Online "Map Notes" sketch layer (not a hosted service — no `itemId`/`url`, defined directly in the web map JSON) | On *(presumed — this is the layer the test exists to demonstrate; no explicit `visibility` key was found to confirm it directly, unlike the Town Boundaries group below)* | — | 15 polygons, 4 polylines, 12 points, 5 text annotations; all hidden when zoomed out past 1:26,029 |

### Town Boundaries Group

Saved as a standalone **Group layer item** — `Group Layer - Town
Boundaries` (item `78853d8236e04a1d8d6df5c0f94e7c13`, owner
`Publisher_VCGI`, public) — rather than staying an ad-hoc group local to
this one web map. Per the propagation caveat documented in [Group
layers](../README.md#group-layers), any future styling/structure edits
made to this item won't automatically reach this web map (or any other
map it's added to) without re-adding it; only edits to the underlying
boundary data itself update live.

Both sublayers point at the same VCGI municipal polygon service already
profiled in [`boundaries.md`](../../data-sources/boundaries.md)
(`FS_VCGI_OPENDATA_Boundary_BNDHASH_poly_towns_SP_v1`), styled as two
layers stacked for a halo effect — confirmed **both explicitly On**
(`visibility: true` on each, independent of the group):

- **Town Boundaries-Outline** — no fill, wide (4.5px) semi-transparent
  white outline, no labels, popups disabled. Purely a soft halo behind
  the line below.
- **Town Boundaries** — no fill, light gray (`#C4C4C4`) dotted outline
  whose width scales down with zoom (1.5px at 1:256,849 down to 0px by
  1:6,421,213), labeled with `TOWNNAME` in muted gray (`#8C8C8C`) bold
  text with a light halo.

## Design notes

- **New label style, not just new content layers:** the label layer in
  this test ("World Terrain Reference Labels Light") is a different AGOL
  item from the one Test 01b/02b use, not the same style reused. It's the
  copy whose placename and spot-elevation text colors were muted to
  `#505050` earlier this session — Test 02c is the first webmap test
  using it.
- **Town Boundaries' two-layer halo styling** (solid white backing +
  dotted gray line + gray labels) is a reasonable reference point if a
  similar treatment is wanted for other boundary levels (county, village)
  in future tests.
- **The Thematic Features Example layer is the point of this test:** it
  demonstrates the muted basemap's intended role as a background for
  user-added point/line/polygon data, per Tim's own description of this
  test's purpose.
- Everything else (base layers 0–10) is unchanged from
  [Test 02b](../topographic-test-02b-world-terrain-labels/README.md)
  except the Alpine Trails opacity bump noted above.

## Related

- [`../topographic-test-02b-world-terrain-labels/README.md`](../topographic-test-02b-world-terrain-labels/README.md) —
  the version this was saved from
- [`../../basemap-styles/world-terrain-reference-labels-light`](../../basemap-styles/world-terrain-reference-labels-light) —
  the new muted label style used here
- [`../../data-sources/boundaries.md`](../../data-sources/boundaries.md) —
  the Town Boundaries source
- [`../../data-sources/protected-lands.md`](../../data-sources/protected-lands.md)
- [`../README.md`](../README.md) — index of all webmap tests
