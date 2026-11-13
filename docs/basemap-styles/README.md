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
    `Marine area`): lightened in stages, currently `#d4dadc` (Tim's own
    further refinement of an earlier `#c2c8ca`, which was itself lifted
    from Positron's `water` fill, `rgb(194, 200, 202)`).
  - **Road casings** (19 layers, all road classes — this style doesn't
    tier road colors by class the way the Imagery variant does):
    lightened from `#505050` to `#d5d5d5`, matching Positron's
    `highway_major_casing`/`highway_motorway_casing`
    (`rgb(213, 213, 213)`) almost exactly. One layer (`Road/Service/1`)
    initially missed this pass since its color was a zoom-stop
    expression (`#999999`→`#505050`), not a flat string — caught and
    flattened to `#d5d5d5` in a follow-up fix.
  - **Trails and pedestrian-road casings** (`Trail or path/1`,
    `Road/Pedestrian/1`): lightened from `#8c8c8c` to `#eaeaea`,
    matching Positron's `highway_path` (`rgb(234, 234, 234)`) — Positron
    keeps paths lighter than roads, mirrored here.
  - **Railroad**: base line lightened from `#c8c8c8` to `#dddddd`,
    matching Positron's `railway` color exactly. The cross-tie overlay
    (`Railroad/ties` — a second line layer, same source, width 5 with a
    tight `[0.2, 2]` dasharray drawn under the thin base line, creating
    the perpendicular tick marks) was missing entirely from this item
    (present in the base, non-desaturated Blue Water style) — re-added
    at the same lightened `#dddddd`.
  - Buildings and the plain `Boundary line`/`Airport property` layers in
    this style are hidden (`"visibility": "none"`) and weren't touched —
    no visible effect either way.
  - **Road name/shield duplication**: this style carries its own
    `Road/label/Rectangle white black` and `.../(Alt)` layers — full
    road-name-plus-shield-icon symbol layers (text, not just an icon),
    rendered at near-black `#000003`, covering the exact same
    `_label_class` range as the proper shield system in the Labels Desat
    style below. Both hidden (`"visibility": "none"`) so road names/
    shields render once, from the Labels style only, not twice at
    conflicting darkness.
- [`world-terrain-reference-labels-light`](world-terrain-reference-labels-light) —
  styled copy of Esri's World Terrain Reference Labels item
  (`World_Basemap_v2`), with placename and spot-elevation text muted to
  `#505050`. Used by [Test 02b](../webmap-tests/topographic-test-02b-world-terrain-labels/README.md)
  and [Test 02c](../webmap-tests/topographic-test-02c-admin/README.md).
- [`world-terrain-reference-labels-light-desat`](world-terrain-reference-labels-light-desat) —
  save-as of the above for the desaturated "Base" configuration. All
  water-feature label text (lakes, rivers, bays, marine/ocean names — 39
  layers across `Water line/area/point`, `Marine area/waterbody`,
  `Ocean point/area`, the disputed-waterbody label, and ferry route names
  like "Burlington - Port Kent") changed from saturated blue (`#1e73c8`,
  plus `#0087ff` on the ferry-label layer specifically — a different,
  even more saturated blue that the first pass missed since it doesn't
  share the other layers' hex value) to `#9DA9B1`, a muted blue-gray
  lifted from
  [OpenMapTiles' Positron style](https://github.com/openmaptiles/positron-gl-style/blob/master/style.json)'s
  own `water_name` text color (`rgb(157,169,177)`) — same source used for
  Light Roads Desat's water fill, for a consistent design lineage. Also
  normalized the Marine/Ocean label halos (previously pale blue,
  `#e0f4ff`/`#e5f6ff`) to the same off-white `#fcfcfa` halo used
  everywhere else in this style, since a blue-tinted halo would have
  undercut the desaturation. Non-blue water labels (islands, playas,
  dams/weirs — already neutral gray) were left unchanged.
  - **Road/placename contrast and hierarchy** (second pass, benchmarked
    against Positron's `highway_name_motorway`/`place_*`/
    `highway_name_other` layers): Positron keeps overall label contrast
    lower than ours and gives major roads and placenames the same
    darker tone, with minor/local road labels notably lighter — not
    something we had before (major vs. minor road labels only differed
    by `#4e4e4e` vs. `#595959`, an 11-point gap, both quite dark).
    - **Placenames, landform names, and spot elevations** (38 layers —
      every `City large/small scale`, `Landform/label/*`, and `Spot
      elevation` layer): `#505050` → `#758191`, Positron's exact
      `place_*` text color.
    - **Major road labels** (`Road`/`Road tunnel` label layers for
      Major, Highway, Freeway Motorway, and their alt-name variants —
      10 layers): `#4e4e4e` → `#758191`, matching Positron's
      `highway_name_motorway` — which uses the identical color to its
      place labels, mirrored here.
    - **Minor/local road labels** (`Road`/`Road tunnel` label layers for
      Local and Minor — 4 layers): `#595959` → `#bbbbbb`, Positron's
      `highway_name_other` — a much lighter tier, giving a real gap
      (~70 points) from the major-road/placename tier instead of 11.
    - Left untouched in this pass: island labels (also `#595959`, but
      not roads — e.g. `Water area/label/Small island`).
  - **Third pass — admin, building, neighborhood, railroad labels**
    (water, ferry, and open-space labels confirmed good as-is and left
    alone):
    - `Neighborhood` had **no explicit text-color at all** (silently
      defaulting to black) — set to `#758191`, the same tone as
      placenames, matching Positron's `place_other` layer (which groups
      neighbourhoods with every other place-name tier under one color).
    - `Building/label/Default` and `Point of interest/General`
      (building/POI name labels — the latter's color was a zoom-stop
      `#787878`→`#343434`, flattened in the process): both set to
      `#758191` as well, for the same visual weight as placenames/
      neighborhoods.
    - `Admin0 point/*` (country-level labels, all size tiers + the
      zoom-stop `2x large` variant, flattened) and
      `Disputed label point/Admin0`: neutral `#3c3c3c` → `#808080` (no
      Positron admin-point equivalent to benchmark against directly, so
      lightened by the same ~25-point-lightness magnitude used
      elsewhere rather than picked arbitrarily).
    - `Admin1 area/label/*` (purple, all 6 size tiers) and
      `Admin2 area/label/*` (tan, both tiers): hue preserved, lightness
      raised by the same ~25 points — `#785ba6`→`#ad9cc9`,
      `#80755f`→`#bbb3a3` — rather than flattened to gray, so the
      distinct admin-level color-coding isn't lost.
    - `Railroad/label/Default`: same hue-preserving lighten,
      `#6e5d54`→`#ad9d94`. `Ferry/label/Rail ferry` shares the original
      brown but was **not** touched, since Tim categorized railways and
      ferries separately (railways need updating, ferries don't) even
      though they currently share a color — they'll diverge after this.
    - `Continent`: `#7d8287` → `#9DA9B1`, aligning with Positron's own
      country-label tone (the same value already used for water-feature
      label text, reused here rather than inventing a new one).
  - **Fourth pass**: `Trail or path/label/Default` (`#778069`) stood out
    once everything around it had been lightened, even though it wasn't
    touched by the earlier open-space exclusion decision — hue-preserved
    lighten to `#b6bcad`. `Pedestrian/label/Default` currently shares the
    original `#778069` but was left alone since only trails were flagged.
  - **Fifth pass — road shield icons**: this style's own road-name
    layers (64 `Road/label/<Shape> <color>` variants — U-shaped,
    Rectangle, Pentagon, Hexagon, Octagon, Shield, Secondary Hwy, each
    with a `(Alt)` counterpart) render a highway-shield sprite via
    `icon-image` per road system/class, with no paint overrides of their
    own (`paint: {}`). These are baked multi-color sprite graphics, not
    SDF icons, so `icon-color` can't recolor them directly — `icon-opacity:
    0.75` added to all 64 instead, to visually mute them in line with the
    now-lighter major road label text. The shield's internal route
    number (also previously an unset `paint: {}`, silently defaulting to
    black — same gap pattern as `Neighborhood` earlier) now explicitly
    set to `#758191` as well, matching the major road label color. This
    was also why shields
    looked doubled/conflicting in testing: see the matching note under
    Light Roads Desat above — the features style had its own redundant,
    near-black road-name-plus-shield layers covering the same roads,
    now hidden there so only this style's shields render.
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
- [`vt-basemap-2026-context-boundaries-desat`](vt-basemap-2026-context-boundaries-desat) —
  save-as of Context Boundaries with water desaturated to the same
  `#c2c8ca` used in Light Roads Desat (all 7 water/marine layers), for
  use alongside that style in the desaturated "Base" configuration.
  Boundary-line colors (country/state gray) are unchanged — only water
  was in scope for this pass.
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
