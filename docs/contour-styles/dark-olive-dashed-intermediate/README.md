# 1' Contours — Dark Olive, Dashed Intermediate

Save-as variant of [Dark Olive](../dark-olive/README.md), for use in the
desaturated basemap configuration. Same color (`#504f3d`), widths, and
zoom-dependent interval structure — the only change is a tight
`line-dasharray: [2, 1]` added to the five **intermediate** (non-index)
contour layers:

- `.../Contour Line, Intermediate Odd` (5ft tier)
- `.../Contour Line, Intermediate Even` / `Intermediate Odd` (2ft tier)
- `.../Contour Line, Intermediate Even` / `Intermediate Odd` (1ft tier)

**Index Major**/**Index Minor** layers (the labeled, heavier-weight
contours at every interval tier) are untouched — still solid lines.

This follows a landscape architecture/site planning convention: dashing
the non-index interval lines visually recedes them relative to the
solid index contours, which carry the elevation labels and matter more
for quickly reading the terrain. Only the finest three interval tiers
(5ft, 2ft, 1ft) have intermediate contours at all — coarser tiers
(1000ft down to 20ft) consist solely of Index Major/Minor lines, so
nothing changes at those zoom levels.

## Related

- [`../dark-olive/README.md`](../dark-olive/README.md) — the style this
  was saved from, including the low-zoom contour density note (still
  applicable here, unchanged)
- [`../../data-sources/contours-1ft.md`](../../data-sources/contours-1ft.md) —
  source data profile
