# 1' Contours — Dark Olive, Dashed

Save-as variant of [Dark Olive](../dark-olive/README.md), for use in the
desaturated basemap configuration (AGOL item "VT Service - Vector Tile
Layer - 1ft Lidar Contours - Dark Olive DASHED", owned by
`Services_VCGI`). Same color (`#504f3d`), widths, and zoom-dependent
interval structure — every contour line, both **Index Major**/**Index
Minor** and the five **Intermediate** (non-index) layers, now carries a
tight `line-dasharray: [2, 1]`.

This went through two passes: dashing just the intermediate lines first
(to visually recede them relative to solid index contours), then
extending the same dash to the index lines too once those still read as
too strong on their own — the index contours' heavier line weight is
relied on to convey their index status instead of a solid-vs-dashed
distinction. Only the finest three interval tiers (5ft, 2ft, 1ft) have
intermediate contours at all — coarser tiers (1000ft down to 20ft)
consist solely of Index Major/Minor lines.

## Related

- [`../dark-olive/README.md`](../dark-olive/README.md) — the style this
  was saved from, including the low-zoom contour density note (still
  applicable here, unchanged)
- [`../../data-sources/contours-1ft.md`](../../data-sources/contours-1ft.md) —
  source data profile
