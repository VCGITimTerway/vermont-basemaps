# 1' Contours — Dark Olive, Dashed

Save-as variant of [Dark Olive](../dark-olive/README.md), for use in the
desaturated basemap configuration (AGOL item "VT Service - Vector Tile
Layer - 1ft Lidar Contours - Dark Olive DASHED", owned by
`Services_VCGI`). Same color (`#504f3d`), widths, and zoom-dependent
interval structure. Current rule: **Index Major** and **Index Minor**
lines (`_symbol: 0`/`1`) are solid; only **Intermediate Even/Odd** lines
(`_symbol: 2`/`3`) are dashed (`line-dasharray: [2, 1]`). Intermediate
lines only exist at the finest three interval tiers (5ft, 2ft, 1ft) —
nothing is dashed at coarser tiers. Label text size reduced from the
original `13.3333` to `11` across all 10 label layers.

## Why not dash by "is this line labeled"

The first two attempts (dash intermediate-only, then dash everything)
didn't match what a labeled-vs-unlabeled distinction should look like,
so a third attempt tried solid-Index-Major / dashed-everything-else —
also wrong, confirmed by testing: at several tiers, Esri's own "Index
Minor" lines (`_symbol: 1`) **do** carry visible elevation labels (e.g.
1250/1750 between 1000/1500/2000), so treating them as the "unlabeled"
category dashed them incorrectly.

Investigated further by decoding live tiles directly rather than
guessing from layer names: the contour **line** features carry only a
`_symbol` number, no name or elevation value at all. Labels live in a
completely separate point-feature layer with its own collision logic
(`text-optional: true`, no filter tying it to which lines are "major"),
so which lines visibly show a label at any moment is a dynamic
rendering outcome, not a fixed attribute on the line. There's no way to
style a line based on "does it currently show a label" — the two
feature sets aren't linked. A perfect labeled/unlabeled split isn't
achievable with this data; the current rule (Major + Minor solid,
Intermediate dashed) is the closest internally-consistent approximation
available, since "Intermediate" is the one category Esri's own naming
marks as pure filler, not index of any kind.

If this still doesn't read right, the next option is varying the dash
by zoom tier directly (e.g. which interval tiers get dashed treatment
at all, independent of symbol category) rather than continuing to key
off `_symbol`.

## Related

- [`../dark-olive/README.md`](../dark-olive/README.md) — the style this
  was saved from, including the low-zoom contour density note (still
  applicable here, unchanged)
- [`../../data-sources/contours-1ft.md`](../../data-sources/contours-1ft.md) —
  source data profile
