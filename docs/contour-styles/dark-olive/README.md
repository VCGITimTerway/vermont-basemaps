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

Which contour interval shows at which zoom level may need adjustment,
particularly at regional/small-scale zoom levels (the broader
1000/500/250 ft tiers at z7–13) — not changed in this pass, which was
line-width only.

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
