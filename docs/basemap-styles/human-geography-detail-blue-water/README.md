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
  **Confirmed NOT to achieve cropping in ArcGIS Online** — see
  "Vermont-only cropping" below. Left in `style.json` anyway since it's
  spec-correct per the MapLibre style spec and harmless where unsupported
  — it may actually work if this style is ever loaded in a non-Esri
  MapLibre/Mapbox GL context later, consistent with this project's
  dual-platform (ArcGIS + open-source) goal. Just don't rely on it for
  ArcGIS Online specifically.
- **Added [`vermont-mask.geojson`](vermont-mask.geojson)** — the actual
  working fix for cropping in ArcGIS Online, see below.

## Vermont-only cropping

**`bounds` does not work in ArcGIS Online.** Confirmed by screenshot after
applying it — roads, water polygons, and place labels from NH/NY/MA/the
wider region still rendered unchanged. ArcGIS's vector tile renderer
appears to silently ignore the MapLibre style spec's `bounds` property
on a source entirely (not a partial/edge-tile issue — the crop had zero
effect).

**Per-feature attribute filtering isn't possible either.** Decoded an
actual tile directly from the live service
(`World_Basemap_v2/VectorTileServer/tile/8/93/76.pbf`) and inspected
every layer's real attribute schema. None of the relevant layers (`Road`,
`Water area`, `Water line`, `Boundary line`, `Railroad`, etc.) carry any
country/state/admin attribute — just things like `Viz`, `DisputeID`,
`_symbol`, and per-language label fields. There's nothing to write a
`filter` expression against; this is a data limitation, not a style
authoring gap.

**Working fix: an opaque mask overlay.** [`vermont-mask.geojson`](vermont-mask.geojson)
is a single polygon covering the whole world *except* Vermont — the real
geometric difference (world rectangle minus Vermont), computed from
Vermont's actual boundary (pulled live from the
[`FS_VCGI_OPENDATA_Boundary_BNDHASH_poly_vtbnd_SP_v1`](../../architecture/foundational-layers.md#vsdi-vermont-spatial-data-infrastructure)
service already documented in this repo), simplified to ~30m tolerance
(invisible at any basemap scale) to keep the file a practical 68 KB
instead of 500 KB.

To use it in ArcGIS Online Map Viewer:

1. **Add → Add Layer from URL**, paste the raw file's GitHub Pages URL:
   `https://vcgitimterway.github.io/vermont-basemaps/basemap-styles/human-geography-detail-blue-water/vermont-mask.geojson`,
   layer type **GeoJSON**.
2. Style its fill as a **solid color matching the basemap's background**
   (e.g. white/light canvas for a Light basemap, dark gray/near-black for
   a Dark basemap) with no outline.
3. Place this mask layer **above every world-wide Esri Living Atlas vector
   tile layer** (Human Geography Base, this Detail layer, Human Geography
   Label, and any other "Blue Water" variants) — one mask layer covers all
   of them at once, since it's a geometric overlay that doesn't care what
   renders beneath it. Keep it *below* any Vermont-specific overlays (DEM,
   contours, parcels, etc.) so those still show normally within the state.
4. The fill color needs to be re-set per basemap variant (Light vs. Dark
   vs. monochrome) — the mask geometry itself is reusable, but its style
   isn't "one size fits all" across variants with different background
   colors.

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
