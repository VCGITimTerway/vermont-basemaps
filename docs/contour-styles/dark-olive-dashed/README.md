# 1' Contours — Dark Olive, Dashed

Save-as variant of [Dark Olive](../dark-olive/README.md), for use in the
desaturated basemap configuration (AGOL item "VT Service - Vector Tile
Layer - 1ft Lidar Contours - Dark Olive DASHED", owned by
`Services_VCGI`). Same color (`#504f3d`), widths, and zoom-dependent
interval structure. **Index Major** and **Index Minor** lines
(`_symbol: 0`/`1`) are solid; only **Intermediate Even/Odd** lines
(`_symbol: 2`/`3`) are dashed (`line-dasharray: [2, 1]`) — a landscape
architecture/site planning convention, used here to make the filler
intervals recede relative to the index lines. Intermediate lines only
exist at the finest three interval tiers (5ft, 2ft, 1ft) — nothing is
dashed at coarser tiers. Label `text-size` is `11` (reduced from the
source style's `13.3333`) across all 10 label layers.

## Why dashing follows Major/Minor vs. Intermediate, not labeled vs. unlabeled

The contour **line** features carry only a `_symbol` number, no name or
elevation value at all. Labels live in a completely separate
point-feature layer with its own collision logic (`text-optional:
true`, no filter tying it to which lines are "major"), so which lines
visibly show a label at any moment is a dynamic rendering outcome, not
a fixed attribute on the line — Esri's own "Index Minor" lines
sometimes carry a visible label, sometimes don't, depending on zoom and
collision. There is no way to style a line based on "does it currently
show a label," since the two feature sets aren't linked at all. The
Major+Minor-solid/Intermediate-dashed rule used here is the closest
internally-consistent approximation available, since "Intermediate" is
the one category Esri's own naming marks as pure filler, not index of
any kind.

**Known limitation, not a style question:** at several coarser zoom
tiers, every visible line is classified `Index Major` in the tile
data — there's no `Index Minor` or `Intermediate` line present at all
to dash, no matter how the style is written. Getting dashed
intermediates to appear at those zooms would need the service itself
republished with different index-class assignments there — see
[`../../data-sources/contours-1ft.md`](../../data-sources/contours-1ft.md#use-cases--limitations)
for the confirmed detail.

## Related

- [`../dark-olive/README.md`](../dark-olive/README.md) — the style this
  was saved from, including the low-zoom contour density note (still
  applicable here, unchanged)
- [`../../data-sources/contours-1ft.md`](../../data-sources/contours-1ft.md) —
  source data profile
