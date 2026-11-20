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
  save-as of Light Roads with water and transportation desaturated, for
  a grayscale/monochromatic basemap variant (the main style in the
  desaturated "Base Desaturated" Group Layer configuration), benchmarked
  throughout against
  [OpenMapTiles' Positron style](https://github.com/openmaptiles/positron-gl-style/blob/master/style.json).
  - **Water** (10 layers: `Water area`/`Water line` at every scale tier,
    `Marine area`): `#d4dadc` (Tim's own further refinement of an earlier
    `#c2c8ca`, which was itself lifted from Positron's `water` fill,
    `rgb(194, 200, 202)`).
  - **Road casings** (19 layers, all road classes — this style doesn't
    tier road colors by class the way the Imagery variant does):
    `#d5d5d5`, matching Positron's `highway_major_casing`/
    `highway_motorway_casing` (`rgb(213, 213, 213)`) almost exactly.
    `Road/Service/1`'s color is a zoom-stop expression rather than a flat
    string and needs to be checked separately from the others when this
    style is next revised.
  - **Trails and pedestrian-road casings** (`Trail or path/1`,
    `Road/Pedestrian/1`): `#eaeaea`, matching Positron's `highway_path`
    (`rgb(234, 234, 234)`) — Positron keeps paths lighter than roads,
    mirrored here.
  - **Railroad**: base line `#dddddd`, matching Positron's `railway`
    color exactly. The cross-tie overlay (`Railroad/ties` — a second
    line layer, same source, width 5 with a tight `[0.2, 2]` dasharray
    drawn under the thin base line, creating the perpendicular tick
    marks) is present here at the same `#dddddd`, matching the base,
    non-desaturated Blue Water style.
  - This style's own `Building` layer (from the same `World_Basemap_v2`
    source, not the dedicated Buildings 2022 layer below) is hidden
    (`"visibility": "none"`) — no visible effect either way.
  - **Road name/shield duplication**: this style carries its own
    `Road/label/Rectangle white black` and `.../(Alt)` layers — full
    road-name-plus-shield-icon symbol layers (text, not just an icon),
    rendered at near-black `#000003`, covering the exact same
    `_label_class` range as the proper shield system in the Labels Desat
    style below. Both are hidden (`"visibility": "none"`) so road names/
    shields render once, from the Labels style only.
- [`human-geography-detail-blue-water-light-roads-desat-imagery`](human-geography-detail-blue-water-light-roads-desat-imagery) —
  save-as of Light Roads Desat for the "Base Desaturated Imagery" group
  (Test 02f), used alongside a muted World Imagery layer at 0.4 opacity.
  Same `#d4dadc` water/casing colors as Light Roads Desat. The four
  water layers with no existing upper zoom cutoff (`Marine area`,
  `Water line/Stream or river`, `Water area/Lake, river or bay`,
  `Water area/Dam or weir`) have `maxzoom: 14.625277` added, matching
  the zoom level where the Base Desaturated Imagery group's Buildings
  2022 layer currently starts rendering (`minScale: 23411.228391` in
  that group, converted from Esri scale to a MapLibre zoom value) — so
  the stylized water fill drops away at the same point buildings start
  showing, letting the aerial imagery itself carry water detail once
  zoomed in that close, mirroring the plain (non-desaturated) Imagery
  style's choice to hide water entirely. The other three water-fill/line
  tiers (`small scale`/`medium scale`/`large scale`) already stop at
  zoom 5/7/11 respectively as part of their normal generalization
  tiering, well before 14.6, so they didn't need a change.
  - **Road/transportation network cutoff**: all 48 road, road tunnel,
    trail, pedestrian-road, railroad, rail ferry, and airport runway
    line/fill layers now have `maxzoom: 15.76` — one zoom level before
    the Base Desaturated Imagery group's Buildings 2022 layer currently
    stops rendering (`maxScale: 5330.99674` in that group, zoom ≈ 16.76)
    — so the road network disappears a level sooner than buildings do,
    per Tim's preference after testing the initial matching cutoff.
    Past that zoom, the vector road network disappears and the aerial
    imagery itself carries the detail. Road name/shield label layers
    and their blockout masks are untouched — they live in the Labels
    style below and keep rendering past this cutoff, just with inverted
    colors (see below).
- [`world-terrain-reference-labels-light-desaturated-imagery`](world-terrain-reference-labels-light-desaturated-imagery) —
  save-as of World Terrain Reference Labels Light Desaturated for the
  "Labels Desaturated Imagery" group (Test 02f). Same color scheme as
  the non-imagery Desaturated labels style, except for one zoom-
  dependent change: the 19 road/transportation text-label layers
  (`Road/label/*` and `Road tunnel/label/*` — Major, Highway, Freeway
  Motorway, Local, Minor, Pedestrian, and their alt-name/tunnel
  variants — plus `Railroad/label/Default`, `Trail or path/label/
  Default`, and `Pedestrian/label/Default`) invert their `text-color`/
  `text-halo-color` pair at zoom 15.76, matching the zoom where the
  corresponding road/transportation network disappears in Light Roads
  DESAT IMAGERY above: below that zoom, labels keep their normal dark
  text on a `#fcfcfa` halo; at and above it, the halo color becomes the
  text color and the original text color becomes the halo (e.g. `Road/
  label/Major`: `#758191` text on `#fcfcfa` halo below 15.76, `#fcfcfa`
  text on a `#758191` halo at/above it) — readable against raw imagery
  once the vector road fill is no longer there to read against. Done
  as a two-stop color function (`15.75`→old, `15.76`→swapped) rather
  than a hard step, for compatibility with the same `stops` function
  syntax already used elsewhere in these styles; the 0.01-zoom gap
  reads as instant in practice. Road-name shield icon layers
  (`Road/label/<Shape> <color>`, 64 layers) are untouched — they only
  have `icon-opacity`/`text-color`, no halo, so the same swap doesn't
  apply the same way; `Ferry/label/Ferry` and `Ferry/label/Rail ferry`
  are also untouched, consistent with ferries being treated as a
  separate category from roads/railroads elsewhere in this style.
- [`world-terrain-reference-labels-light`](world-terrain-reference-labels-light) —
  styled copy of Esri's World Terrain Reference Labels item
  (`World_Basemap_v2`), with placename and spot-elevation text muted to
  `#505050`. Used by [Test 02b](../webmap-tests/topographic-test-02b-world-terrain-labels/README.md)
  and [Test 02c](../webmap-tests/topographic-test-02c-admin/README.md).
- [`world-terrain-reference-labels-light-desat`](world-terrain-reference-labels-light-desat) —
  save-as of the above for the desaturated "Base" configuration, benchmarked
  throughout against
  [OpenMapTiles' Positron style](https://github.com/openmaptiles/positron-gl-style/blob/master/style.json).
  Current label color scheme:
  - **Water-feature labels** (39 layers across `Water line/area/point`,
    `Marine area/waterbody`, `Ocean point/area`, the disputed-waterbody
    label, and ferry route names like "Burlington - Port Kent"): `#9DA9B1`,
    a muted blue-gray lifted from Positron's `water_name` text color
    (`rgb(157,169,177)`) — same source used for Light Roads Desat's water
    fill, for a consistent design lineage. Marine/Ocean label halos are
    the same off-white `#fcfcfa` used everywhere else in this style, not
    the saturated pale blue Esri ships by default. Non-blue water labels
    (islands, playas, dams/weirs — already neutral gray) are unchanged
    from the source style. `Continent` is also `#9DA9B1`, aligning with
    Positron's own country-label tone.
  - **Placenames, landform names, and spot elevations** (38 layers —
    every `City large/small scale`, `Landform/label/*`, and `Spot
    elevation` layer), plus `Neighborhood`, `Building/label/Default`, and
    `Point of interest/General`: `#758191`, Positron's exact `place_*`
    text color — Positron groups all of these under one placename tone,
    mirrored here. (`Neighborhood` previously had no explicit
    `text-color` at all and silently defaulted to black; `Point of
    interest/General`'s color was a zoom-stop expression, now flattened.)
  - **Major road labels** (`Road`/`Road tunnel` label layers for Major,
    Highway, Freeway Motorway, and their alt-name variants — 10 layers):
    `#758191`, matching Positron's `highway_name_motorway`, which uses
    the identical color to its place labels.
  - **Minor/local road labels** (`Road`/`Road tunnel` label layers for
    Local and Minor — 4 layers): `#bbbbbb`, Positron's
    `highway_name_other` — a deliberately much lighter tier than the
    major-road/placename group above. Island labels (`Water area/label/
    Small island`, also naturally lighter) are unrelated to this tier and
    unchanged.
  - **Trail/pedestrian label family** (`Road/label/Pedestrian`, `Road
    tunnel/label/Pedestrian`, `Trail or path/label/Default`,
    `Pedestrian/label/Default`): `#b6bcad`, a hue-preserved lighten of
    the original olive-green `#778069`/`#594c42` — all four now match.
  - **Admin/railroad labels**: `Admin0 point/*` (country-level, all size
    tiers) and `Disputed label point/Admin0`: `#808080`. `Admin1 area/
    label/*` (purple, 6 size tiers): `#ad9cc9`. `Admin2 area/label/*`
    (tan, both tiers): `#bbb3a3`. `Railroad/label/Default`: `#ad9d94`.
    Admin1/Admin2/Railroad are hue-preserved lightens of their original
    purple/tan/brown, rather than flattened to gray, so the distinct
    category color-coding isn't lost. `Ferry/label/Rail ferry` shares
    the original railroad brown (`#6e5d54`) but is intentionally
    unchanged — Tim categorizes railways and ferries separately even
    though they currently share a color.
  - **Road shield icons**: this style's own road-name layers (64
    `Road/label/<Shape> <color>` variants — U-shaped, Rectangle,
    Pentagon, Hexagon, Octagon, Shield, Secondary Hwy, each with a
    `(Alt)` counterpart) render a highway-shield sprite via `icon-image`
    per road system/class. These are baked multi-color sprite graphics,
    not SDF icons, so `icon-color` can't recolor them directly —
    `icon-opacity: 0.75` is set on all 64 instead, to visually mute them
    in line with the lighter road label text. Each shield's internal
    route number is explicitly `#758191` (previously an unset `paint:
    {}`, silently defaulting to black). The Light Roads Desat features
    style hides its own redundant, near-black road-name-plus-shield
    layers that used to cover the same roads, so only this style's
    shields render.
  - **Label/feature zoom alignment**: label `minzoom` values are aligned
    with the matching line layer's `minzoom` in Light Roads Desat, so
    road names don't appear before the road itself is visible:
    `Road/label/Minor` (12), `Road/label/Local` (13), `Road
    tunnel/label/Minor` (12), `Road tunnel/label/Local, service, 4WD`
    (13 — this three-class combined label layer exactly matches `Local`
    and `4WD`'s feature minzoom; `Service` tunnels start one level later
    still, at 14), `Road/label/Pedestrian` (15). Major/Highway/Freeway
    Motorway and Local-ramp classes are already aligned or
    label-after-feature (the safe direction).
- [`buildings-2022-white-desat`](buildings-2022-white-desat) — the
  already-separate, Desaturated-specific "Buildings 2022" item (item
  `b9f60490ca3d4a3f8d6af6c80e4b8c96`, titled "...Buildings 2022 f8f8f8"
  — distinct from the shared item used by Base Topo/Base, so this only
  affects Desaturated). A single flat fill (`#f1f1f1`) + stroke outline
  (`#dbdbda`), rather than the two-layer `fill-translate` drop-shadow
  trick the source style uses elsewhere — on the desaturated basemap,
  with no hillshade/base-color canvas beneath it, that shadow reads as
  the building's actual edge rather than a subtle depth cue.
- [`vt-basemap-2026-town-labels-desat`](vt-basemap-2026-town-labels-desat)
  and [`vt-basemap-2026-city-points-desat`](vt-basemap-2026-city-points-desat) —
  Desaturated-specific Save As copies of **VT Basemap 2026 Town Labels
  Manual Deconflict** (shared item `04faa79cda0446759b7024bb9b46e3ff`,
  used as-is by Base Topo/Base) and **VT Basemap 2026 City Points WM -
  Levels 6 7 8** (shared item `a58653bb5d8947b0909ccbdec1cb463f`),
  now saved as their own items — `VT Basemap 2026 Town Labels Manual
  Deconflict DESAT` (`70bdd74a5472484eaa169b583a642237`) and
  `VT Basemap 2026 City Points WM - Levels 6 7 8 DESAT`
  (`77b6f532de0b4da091cbc07f1d38a75c`) — referenced by the Labels
  Desaturated Group Layer item in place of the shared ones; Base Topo
  and Base's Labels group (`0ff87dab7daf4141a5e95a2f8be0715e`) still
  points at the original shared items. Label text color is `#758191`
  (matching `Neighborhood`'s color) in both — all 3 City Points tiers
  (Default/Regional/Other) and the single Town Labels layer. The City
  Points circle marker's own stroke (`#4E4E4E`) is unchanged from the
  shared item.
- [`vt-basemap-2026-city-points`](vt-basemap-2026-city-points) — VCGI's
  own city-point labels, filling the statewide/regional zoom gap where
  Esri's Living Atlas content has no Vermont-only filter. Tiered across
  three zoom levels: statewide (Burlington, Montpelier, Rutland,
  Bennington — no `minzoom`), regional (Brattleboro, Saint Albans,
  Saint Johnsbury — `minzoom: 7`), close-in (the remaining 9, including
  Barre — `minzoom: 8`, alongside e.g. Middlebury and White River
  Junction). Same tier placement applied to the
  [`vt-basemap-2026-city-points-desat`](vt-basemap-2026-city-points-desat)
  copy below.
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
- [`vt-basemap-2026-context-boundaries-desat`](vt-basemap-2026-context-boundaries-desat) —
  save-as of Context Boundaries with water desaturated to `#d4dadc`
  (all 7 water/marine layers), matching Light Roads Desat's own water
  fill, for use alongside that style in the desaturated "Base"
  configuration. Boundary-line colors (country/state gray,
  `#a8a8a8`/`#c8c8c8`) are unchanged.
- [`world-terrain-reference-labels-dark-imagery`](world-terrain-reference-labels-dark-imagery) —
  styled copy of Esri's World Terrain Reference Labels item, for the
  "Labels Imagery" Group Layer configuration (dark aerial imagery
  background). Text/halo roles flipped from the default light-basemap
  convention (dark text, light halo) to a dark-imagery-appropriate one
  (light text, dark halo matching each category's original text color)
  — 82 layers flipped. Two categories deliberately **excluded** and left
  as-is per explicit instruction: water labels (any layer whose color is
  part of the blue water family — `#1e73c8`/`#0087ff`/`#8499a6`/
  `#73AFBF` — covering `Water line/area/point`, `Marine`, `Ocean`, and
  `Ferry/label/Ferry`, regardless of source-layer name: e.g. gray-colored
  "Water area" labels like islands/dams/playas were still flipped, since
  their *color* was never actually part of the blue water family) and
  open-space labels (`#5a7850`/`#778069` — Cemetery, Golf course, Zoo,
  Park or farming, Trail or path, Pedestrian areas). One layer
  (`Neighborhood`) had no original text-color to flip from — set
  manually to light text (`#fcfcfa`) on a dark neutral halo (`#3c3c3c`)
  to match the rest.
- [`human-geography-detail-blue-water-light-roads-imagery`](human-geography-detail-blue-water-light-roads-imagery) —
  save-as of Light Roads for the in-progress "Base Imagery" Group Layer
  configuration (imagery basemap — [Test 03](../webmap-tests/) once
  documented). Likely to be renamed "Transparent Roads Imagery" to match
  its current design:
  - **Water** (10 layers) set to `"visibility": "none"`, so the vector
    tile's flat water fill/line doesn't cover the real water visible in
    the underlying aerial imagery.
  - **Major and minor/local roads now share the same single-ribbon
    treatment**, after an initial attempt at a two-tone amber-bordered
    white road for major roads proved too harsh against imagery (not the
    clean, translucent look of LINZ's NZ Aerial Imagery basemap). Both
    tiers now hide their white fill layer (`"visibility": "none"`),
    leaving only the colored casing layer, semi-transparent, as the
    entire visible road:
    - **Interstates** (Freeway/Motorway + its ramps — `_symbol` 0, 2)
      and **Major roads** (`_symbol` 3, 4 — arterials, not state-numbered
      highways): muted warm tan `#c9915a` at `line-opacity: 0.55`.
    - **State highways** (Esri's `Highway` class — `_symbol` 1):
      recolored to a more yellow-orange `#e0b030`, at `line-opacity:
      0.4` — lower than interstates, so numbered state routes read as a
      secondary tier rather than competing with/outshining interstates
      for visual prominence. (Esri's taxonomy doesn't have a distinct
      "arterial" tier separate from "Major," so `_symbol` 3/4 were
      grouped with interstates here, not highways — flag if that
      grouping should move instead.)
    - **Minor/local roads** (Minor, Local, Service, Pedestrian, 4WD, and
      their ramp variants — `_symbol` 5–10): gray `#bcbcbc`/`#8c8c8c` at
      `line-opacity: 0.45`.
  - **Trails** (`Trail or path`, a separate source-layer from `Road`):
    width reduced (casing 2.9→1.9, dashed overlay 1.6→2 — the overlay
    ended up wider than the casing after iteration, intentional per
    testing) and both layers given opacity (casing `#8c8c8c` at 0.5,
    white dashed overlay at 0.3) so the "close-to-white" dash reads as
    subtle rather than a bright highlight. Dash pattern itself (`[3,2]`)
    unchanged throughout.
  - **Airport runways** (`Airport/Airport runway`): were solid
    near-white (`#e7e5e5`, fully opaque) — recolored to the same
    `#bcbcbc` at `0.45` opacity as local roads, so they recede the same
    way. `Airport/Airport property` (a separate, already-faint fill) was
    left alone.
  First-pass-and-iterated values (tan/yellow shades, opacities, which
  road classes count as "major") — this style is still being tuned
  against real imagery, re-pull before further edits rather than
  assuming this doc is current.
