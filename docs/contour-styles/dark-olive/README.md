# 1' Contours — Dark Olive

MapLibre/Mapbox GL style for the 1' lidar-derived contour layer (see
[`../../data-sources/contours-1ft.md`](../../data-sources/contours-1ft.md)
for the underlying data's stewardship, vintage, and known limitations),
pointed at VCGI's existing Esri Vector Tile Service
(`VECTOR_VCGI_CN1TGEN_WM_v1`). Line/label color `#504f3d`, zoom-dependent
interval (1000 ft down to 1 ft) matching the service's own layer
structure.

## Changelog

- **Line widths thinned ~25%** (uniform scale, ratios between
  index/intermediate weights preserved): `2 → 1.5`, `1.33333 → 1.0`,
  `1.06667 → 0.8`, `0.933333 → 0.7`. No other properties changed — color,
  zoom breaks, labels, and layout are untouched from the original. Two
  layers (`50ft`/`50ft` Index Major/Minor, z14–15) had no explicit
  `line-width` to begin with (MapLibre default of 1) and were left as-is.

## To revisit

~~Which contour interval shows at which zoom level may need
adjustment...~~ **Investigated — not fixable via style changes.**
Decoded actual tiles directly from the VectorTileServer at z7–13: the
finer-interval data (500ft, 250ft, 100ft...) genuinely doesn't exist in
the tiles below the zoom it currently appears at (z7–10 tiles contain
*only* the 1000ft interval, full stop) — this is a hard server-side/data
limitation, not a style `minzoom`/`maxzoom` choice. Our zoom breaks
already exactly match Esri's own factory-default style for this service;
there's no slack to recover by editing the style.json. See
[`../../data-sources/contours-1ft.md`](../../data-sources/contours-1ft.md#path-to-pmtiles--titiler-output)
for the underlying pipeline gaps this ties into.

Two real paths forward if the sparse Champlain Valley contours at low
zoom still need addressing:

1. Ask whoever manages the contour VectorTileServer's publishing pipeline
   whether a finer interval (e.g. 500ft) could be exposed starting at a
   lower zoom (e.g. z9–10 instead of z11) in a future republish.
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
