# Topographic — Test 02c (Base + Thematic Features)

Pulled directly from the web map's JSON via the AGOL sharing REST API,
not hand-described — re-pull if this map changes rather than editing
this table by hand.

**Live embed:** <https://vcgitimterway.github.io/vermont-basemaps/webmap-tests/topographic-test-02c-admin/>
**ArcGIS Online item:** <https://vcgi.maps.arcgis.com/apps/mapviewer/index.html?webmap=c204789fd709456aaad6749f8d4188eb>
**AGOL item title:** "VT Basemap 2026 - Base - Thematic Features - Test 02c"
**Test extent:** centered -72.5722, 44.2650 at a town-scale zoom,
consistent with this test's purpose (showing municipal boundaries and
sample thematic data, both of which only render at this kind of zoom —
see the table below)

Built on the **Base** Group Layer configuration (same as
[Test 02d](../topographic-test-02d-base/README.md)) plus two additions:
the Town Boundaries Group Layer, and a sample thematic point/line/polygon
layer demonstrating the basemap's intended use as a muted background for
user-added data.

## Basemap

Same as Test 02b/02d: **Human Geography Map** (Esri Living Atlas), own
"Human Geography Base" vector tile sub-layer turned **off**.

## Layer groups

| Group (in-map label) | Item ID | Notes |
|---|---|---|
| Base | `1a119fb231ac4e8985346ddcc438692f` ("VT Basemap 2026 Base") | Same item reused from [Test 02d](../topographic-test-02d-base/README.md) — no Lidar DEM Hillshade |
| Town Boundaries | `78853d8236e04a1d8d6df5c0f94e7c13` ("VT Basemap 2026 Town Boundaries") | Same item reused from Test 02b/02d/02e (there shown with the in-map label "Boundaries" — this map happens to label it "Town Boundaries" instead); scale range restricted to below 1:1,412,738 in this map |
| Labels | `0ff87dab7daf4141a5e95a2f8be0715e` ("VT Basemap 2026 Labels") | Same item reused from Test 02b/02d |

Plus one ad-hoc, non-grouped layer: **Thematic Features Example**.

## Layers shown (top to bottom as returned by the API)

### Base group

Same composition as [Test 02d's Base group](../topographic-test-02d-base/README.md#base-group):
Protected Lands Database, Alpine Trails/Golf Courses/Quarries, 1ft Lidar
Contours, Blue Water Light Roads, Wetlands Inventory, Buildings 2022,
Alpine Ski Lifts, VT Mask, State Boundary, and Context Boundaries —
unchanged here except Alpine Trails' opacity, raised from 0.41 to 0.67
in this test.

### Town Boundaries group (Group layer item)

Both sublayers point at the same VCGI municipal polygon service profiled
in [`boundaries.md`](../../data-sources/boundaries.md)
(`FS_VCGI_OPENDATA_Boundary_BNDHASH_poly_towns_SP_v1`), styled as two
layers stacked for a halo effect — both explicitly On
(`visibility: true` on each, independent of the group):

- **Town Boundaries-Outline** — no fill, wide (4.5px) semi-transparent
  white outline, no labels, popups disabled. Purely a soft halo behind
  the line below.
- **Town Boundaries** — no fill, light gray (`#C4C4C4`) dotted outline
  whose width scales down with zoom (1.5px at 1:256,849 down to 0px by
  1:6,421,213), labeled with `TOWNNAME` in muted gray (`#8C8C8C`) bold
  text with a light halo.

### Labels group (Group layer item)

Same three sublayers as [Test 02b/02d's Labels
group](../topographic-test-02b-world-terrain-labels/README.md#labels-group-group-layer-item):
World Terrain Reference Labels Light (On), Town Labels Manual Deconflict
(presumed On), City Points (presumed On).

### Thematic Features Example (ad-hoc layer, not grouped)

Inline ArcGIS Online "Map Notes" sketch layer (not a hosted service — no
`itemId`/`url`, defined directly in the web map JSON). On *(presumed —
this is the layer the test exists to demonstrate; no explicit
`visibility` key was found to confirm it directly)*. 15 polygons, 4
polylines, 12 points, 5 text annotations; all hidden when zoomed out
past 1:26,029.

## Design notes

- **The Thematic Features Example layer is the point of this test:** it
  demonstrates the muted basemap's intended role as a background for
  user-added point/line/polygon data.
- **Town Boundaries' two-layer halo styling** (solid white backing +
  dotted gray line + gray labels) is a reasonable reference point if a
  similar treatment is wanted for other boundary levels (county,
  village) in future tests.
- This test now shares all three of its Group Layers (Base, Town
  Boundaries, Labels) with Test 02b/02d rather than carrying its own
  copies — the only things unique to this map are the Alpine Trails
  opacity bump and the Thematic Features Example layer itself.

## Related

- [`../topographic-test-02d-base/README.md`](../topographic-test-02d-base/README.md) —
  the Base configuration this one builds on
- [`../topographic-test-02b-world-terrain-labels/README.md`](../topographic-test-02b-world-terrain-labels/README.md) —
  shares the same Labels and Town Boundaries Group Layer items
- [`../../data-sources/boundaries.md`](../../data-sources/boundaries.md) —
  the Town Boundaries source
- [`../../data-sources/protected-lands.md`](../../data-sources/protected-lands.md)
- [`../README.md`](../README.md) — index of all webmap tests
