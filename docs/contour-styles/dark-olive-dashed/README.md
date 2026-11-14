# 1' Contours — Dark Olive, Dashed

Save-as variant of [Dark Olive](../dark-olive/README.md), for use in the
desaturated basemap configuration (AGOL item "VT Service - Vector Tile
Layer - 1ft Lidar Contours - Dark Olive DASHED", owned by
`Services_VCGI`). Same color (`#504f3d`), widths, and zoom-dependent
interval structure. Current rule: **Index Major** lines (`_symbol: 0`)
are solid at every tier; **Index Minor** (`_symbol: 1`) and
**Intermediate Even/Odd** (`_symbol: 2`/`3`) lines are dashed
(`line-dasharray: [2, 1]`) at every tier where they exist.

This landed after a few iterations: dashing only the Intermediate layers
first (5 layers, only present at the finest three tiers) read fine but
left the index lines at coarser tiers looking relatively strong; dashing
every line (including Index Major) was tested next and came back as too
much dashing overall. The fix wasn't a bespoke per-zoom lookup — it's
that `_symbol: 0` ("Index Major," the labeled line) vs. everything else
is **already the same distinction at every tier**, confirmed by decoding
live tiles directly rather than assuming from layer names alone: at
tiers where a source-layer has more than one symbol value present
(e.g. `250ft` at z12–13, `50ft`/`10ft` at z16–17, `1ft`/`2ft` at
z18–19+), symbol 0 always lines up with the labeled contours and the
higher symbol numbers are always the finer, unlabeled lines between
them — regardless of what actual foot-interval that tier represents.
So "solid Index Major, dashed everything else" applied uniformly across
all 29 contour line layers reproduces the tier-by-tier behavior
described (e.g. "1000/2000/3000 solid with 250ft dashed in between,"
then "1000/1500/2000 solid with 100ft dashed in between" one zoom in)
without needing to special-case each interval tier individually. Some
coarser tiers (1000ft down to 20ft, depending on exact zoom) only have
Index Major defined in the style at all — nothing to dash there yet.

## Related

- [`../dark-olive/README.md`](../dark-olive/README.md) — the style this
  was saved from, including the low-zoom contour density note (still
  applicable here, unchanged)
- [`../../data-sources/contours-1ft.md`](../../data-sources/contours-1ft.md) —
  source data profile
