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
- **Railway symbol**: solid rail line + wide short-dash "ties" layer,
  replacing the dotted look. See "Railway symbol" below. Backed up
  beforehand as [`backups/v2-before-railway.json`](backups/v2-before-railway.json).

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

### Known limitation: label text gets cut off mid-glyph

Placing the mask above *every* layer (including the Human Geography Label
layer) crops text labels the same way it crops polygons/lines — but
cutting a polygon at an edge looks natural, while cutting text mid-word
(e.g. "Plattsburgh" or "Brattleboro" sliced at the mask boundary) reads as
broken, not intentional. There's no attribute to fix this by filtering
(see above — no per-label geographic attribute exists), so the only lever
is **layer order**: placing the mask *below* the label layer instead of
above it. That lets nearby cross-border city labels render in full rather
than getting clipped — normal basemap behavior (most basemaps show some
out-of-state context near borders) — at the cost of no longer hiding
those labels at all. Currently applied as a workaround for testing
purposes; not necessarily the final answer.

This is also a concrete data point for
[`../../architecture/foundational-layers.md` gap #4](../../architecture/foundational-layers.md#gaps--open-questions)
(no open-source equivalent of Living Atlas for transportation/place
names): it's now clear Living Atlas content is awkward even on the
*ArcGIS* side for a hard Vermont-only product, not just absent for
open-source apps. Strengthens the case for eventually sourcing roads and
place names from VCGI's own VSDI data instead (which would carry real
Vermont attribution, enabling genuine per-feature filtering on both
platforms) rather than treating this as an Esri-only workaround problem.

## Railway symbol

**Resolved — went with option 2** (ruled out the Esri Style Editor route:
no built-in railroad/cross-tie symbol available there either). Two
stacked line layers now render the classic no-sprite-needed "hachured
railway" look:

- **`Railroad/ties`** (new, drawn first/underneath): wide (`line-width: 5`)
  dark gray (`#505050`, matching this style's existing road-casing
  color), short-dash (`line-dasharray: [0.2, 2]`) — frequent brief
  segments at the full width.
- **`Railroad`** (existing layer, modified): dasharray removed, now a
  solid `#c8c8c8` line at its original width (1.5), drawn on top.

Because the ties layer is wider than the solid rail-bed line on top, each
short dash segment only shows as a small tick poking out past both edges
of the solid line — reading as cross-ties without needing any sprite
icon. Backed up beforehand as
[`backups/v2-before-railway.json`](backups/v2-before-railway.json).

## Related

- [`../../contour-styles/dark-olive/README.md`](../../contour-styles/dark-olive/README.md) —
  another basemap-layer style in this repo, same bounding-box convention
- [`../../architecture/foundational-layers.md`](../../architecture/foundational-layers.md#esri-community-maps-separate-existing-pipeline) —
  context on this layer's relationship to Esri Community Maps/Living Atlas
