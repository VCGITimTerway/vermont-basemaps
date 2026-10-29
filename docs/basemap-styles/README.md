# Basemap Styles

Styled copies of Esri basemap vector tile layers (Human Geography,
World Basemap, etc.), customized for VCGI basemap use. Distinct from
[`../contour-styles/`](../contour-styles/README.md), which is specifically
the 1' contour layer.

## Variants

- [`human-geography-detail-blue-water/`](human-geography-detail-blue-water/README.md) —
  styled copy of Esri's Human Geography Detail layer ("VT Basemap -
  Vermont Physical Geography Light - Human Geography Detail - Blue
  Water"). Vermont-cropped via source bounds; railway symbol change
  pending a decision.
- [`human-geography-detail-blue-water-light-roads`](human-geography-detail-blue-water-light-roads) —
  save-as of the above with lighter road border colors (for use as a
  muted background under thematic data) and a dashed trail symbol
  ported from the base style.
- [`human-geography-detail-blue-water-light-roads-desat`](human-geography-detail-blue-water-light-roads-desat) —
  save-as of Light Roads with water desaturated, for a grayscale/
  monochromatic basemap variant (first piece of a desaturated "Base"
  configuration). All 10 water-related layers (`Water area`/`Water
  line` at every scale tier, `Marine area`) changed from the saturated
  `#ddeff4` to `#c2c8ca` — a cool neutral gray lifted directly from
  [OpenMapTiles' Positron style](https://github.com/openmaptiles/positron-gl-style/blob/master/style.json)
  (`rgb(194, 200, 202)`), the reference MapTiler Positron look this
  variant is aiming for.
- [`world-terrain-reference-labels-light`](world-terrain-reference-labels-light) —
  styled copy of Esri's World Terrain Reference Labels item
  (`World_Basemap_v2`), with placename and spot-elevation text muted to
  `#505050`. Used by [Test 02b](../webmap-tests/topographic-test-02b-world-terrain-labels/README.md)
  and [Test 02c](../webmap-tests/topographic-test-02c-admin/README.md).
- [`vt-basemap-2026-city-points`](vt-basemap-2026-city-points) — VCGI's
  own city-point labels, filling the statewide/regional zoom gap where
  Esri's Living Atlas content has no Vermont-only filter. Tiered across
  three zoom levels (statewide/regional/close-in).
- [`vt-basemap-2026-town-labels`](vt-basemap-2026-town-labels) — VCGI's
  own Vermont municipal-name labels, filling a content gap (official
  town names not always present in Living Atlas content), not just a
  zoom gap. Manually deconflicted against World Terrain Reference
  Labels Light's own place content (vector tile layers don't share
  label collision detection across separate items — see
  [Test 02b](../webmap-tests/topographic-test-02b-world-terrain-labels/README.md#whats-different-from-test-02)).
- [`vt-basemap-2026-context-boundaries`](vt-basemap-2026-context-boundaries) —
  surrounding state/international boundary lines and water, derived from
  the same `World_Basemap_v2` source as the base Blue Water style
  (its boundary-line sub-layers exist there but are disabled by
  default). Positioned above the VT mask so neighboring-state context
  still shows at statewide zoom while non-Vermont roads stay masked.
