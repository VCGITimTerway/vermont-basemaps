# Human Geography Detail — Blue Water

A styled copy of Esri's **Human Geography Detail** vector tile layer
(source: `World_Basemap_v2`), customized for VCGI basemap use. Full
title: "VT Basemap - Vermont Physical Geography Light - Human Geography
Detail - Blue Water". 80 layers total (62 line, 9 fill, 9 symbol — the
symbol layers are all road-shield labels; there's no separate place-name
layer in this style).

## Backups

[`backups/v1-original.json`](backups/v1-original.json) — exact,
untouched copy of the style as provided before any of the changes below,
kept in case of needing to revert. Each future backup should be named
`v<N>-<short-description>.json`.

## Changelog

- **v1 → current:** Added a Vermont-plus-buffer `bounds` array
  (`[-73.5, 42.727, -71.4653, 45.0169]`) to the shared `esri` source.
  This is the same bbox already used for the 1' contour service
  elsewhere in this repo (see
  [`../../contour-styles/dark-olive/style.json`](../../contour-styles/dark-olive/style.json)),
  reused here for consistency.
  - **Why a bounding box and not per-feature filtering:** this style's
    source has no symbol/label layer for named places at all (only road
    labels), and there's no attribute in the other layers (water, roads,
    boundaries, etc.) identifying which state/country a feature belongs
    to — a true "only features touching Vermont" filter isn't expressible
    against this data. A source-level `bounds` is the standard MapLibre
    mechanism for this: it crops which vector tiles are requested/drawn
    to a bounding box, affecting every layer pulling from that source
    uniformly (roads, water, boundaries, airports, buildings, trails,
    ferry, railroad, and road labels all share the one `esri` source).
  - This intentionally keeps features that cross the border (e.g. all of
    Lake Champlain, which extends into New York) rather than clipping at
    the state line exactly, per the original request.

## Pending

**Railway symbol change not yet made.** The `Railroad` layer is currently
a solid gray (`#c8c8c8`) line with a dash pattern (`[2,1,2,1]`) that reads
as dotted. The ask is a solid line with a perpendicular cross-tie mark
(the standard railway cartographic convention), but this style's sprite
sheet has no rail-related icon (confirmed — only 22 icons total, all
road-shield rectangles and a few area-fill patterns), and `line-dasharray`
can't produce perpendicular ties regardless (it only toggles the line
on/off along its own direction). Three options, still waiting on a
choice:

1. **Solid line only, no ties** — just remove the dasharray. No new
   assets needed, doable immediately.
2. **Solid line + contrasting dash overlay** — a second thin, short-dash
   line on top of the solid base; the common no-sprite-needed convention
   several basemaps use to suggest "railway," but not literally
   perpendicular ties.
3. **True cross-ties via Esri's Style Editor** — check whether Esri's
   Vector Tile Style Editor has a built-in railroad/cross-tie line symbol
   in its picker; if so, apply it there (generates the correct sprite
   automatically), then export and hand back the updated style.json.

## Related

- [`../../contour-styles/dark-olive/README.md`](../../contour-styles/dark-olive/README.md) —
  another basemap-layer style in this repo, same bounding-box convention
- [`../../architecture/foundational-layers.md`](../../architecture/foundational-layers.md#esri-community-maps-separate-existing-pipeline) —
  context on this layer's relationship to Esri Community Maps/Living Atlas
