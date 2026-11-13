# Contour Styles

MapLibre/Mapbox GL style.json variants for the 1' lidar-derived contour
layer, each pointed at VCGI's Esri Vector Tile Service
(`VECTOR_VCGI_CN1TGEN_WM_v1`). See
[`../data-sources/contours-1ft.md`](../data-sources/contours-1ft.md) for
the underlying data itself (stewardship, vintage, known limitations).

## Variants

- [`dark-olive/`](dark-olive/README.md) — dark olive-green lines/labels
  (`#504f3d`), thinned line widths.
- [`dark-olive-dashed/`](dark-olive-dashed/README.md) — save-as of Dark
  Olive for the desaturated basemap, with a tight dash (`[2, 1]`) on
  every contour line — a common landscape architecture/site planning
  convention. Index contours are differentiated from intermediate ones
  by line weight alone (both are now dashed, not solid-vs-dashed).
