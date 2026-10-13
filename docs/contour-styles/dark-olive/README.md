# 1' Contours — Dark Olive

MapLibre/Mapbox GL style for the 1' lidar-derived contour layer (see
[`../../data-sources/contours-1ft.md`](../../data-sources/contours-1ft.md)
for the underlying data's stewardship, vintage, and known limitations),
pointed at VCGI's existing Esri Vector Tile Service
(`VECTOR_VCGI_CN1TGEN_WM_v1`). Line/label color `#504f3d`, zoom-dependent
interval (1000 ft down to 1 ft) matching the service's own layer
structure. Line widths: `1.5` (index major at coarser tiers), `1.0`,
`0.8`, `0.7` depending on tier/weight — thinner than the service's
factory-default widths, same hierarchy ratios preserved.

## Low-zoom contour density

The Champlain Valley (mostly low elevation) shows little contour detail
at the zoom levels where contours first appear, since only the 1000ft
interval exists at z7–10 — confirmed by decoding actual tiles directly
from the VectorTileServer. This is a hard server-side/data limitation,
not a style `minzoom`/`maxzoom` choice: the finer-interval data (500ft,
250ft, 100ft...) genuinely doesn't exist in tiles below the zoom it
currently appears at, and these zoom breaks already exactly match Esri's
own factory-default style for this service — no slack to recover by
editing `style.json`. See
[`../../data-sources/contours-1ft.md`](../../data-sources/contours-1ft.md#path-to-pmtiles--titiler-output)
for the underlying pipeline.

Two paths forward if the sparse Champlain Valley contours at low zoom
need addressing:

1. Ask whoever manages the contour service's publishing pipeline whether
   a finer interval (e.g. 500ft) could be exposed starting at a lower
   zoom (e.g. z9–10 instead of z11) in a future republish.
2. Lean on the [Bare Earth Hillshade](../../data-sources/hillshade-bare-earth.md)
   layer instead at this zoom tier — it's a continuous raster with no
   zoom-gating, so it can convey subtle valley relief via shading even
   where contour *lines* structurally can't help yet.

## Related

- [`../../data-sources/contours-1ft.md`](../../data-sources/contours-1ft.md) —
  source data profile (stewardship, vintage mismatch with the 2023 DEM,
  known missing-summit-contours defect)
- [`../../dem-color-ramps/11class-monochrome-canvas/README.md#companion-layers`](../../dem-color-ramps/11class-monochrome-canvas/README.md#companion-layers) —
  a different, lighter contour color (`#95805F`) was recommended there
  for the monochrome canvas basemap specifically, since `#504f3d` read as
  too dark/overwhelming in that context. This dark-olive style is a
  separate variant, not a replacement for that recommendation — which one
  applies depends on which basemap it sits on top of.
