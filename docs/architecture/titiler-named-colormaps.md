# TiTiler Named Colormaps (proposed, not yet live-tested)

**Status: mechanism confirmed via source inspection only.** The approach
below was worked out by installing `rio-tiler`/`titiler.core` locally and
reading their actual source (not from memory/documentation), but an
end-to-end test against a real tile request was started and then
cancelled before it completed (it was fetching the full statewide DEM COG
over the network and was taking a long time; cancelled to avoid an
unnecessary large download, not because it failed). **Nothing here has
been deployed or confirmed working against a live server.** Revisit and
actually test before relying on it.

## Why

See the ArcGIS Online gotcha documented in
[`foundational-layers.md`](foundational-layers.md#raster--titiler) and in
[`../dem-color-ramps/11class-feet-aligned/README.md`](../dem-color-ramps/11class-feet-aligned/README.md#applying-in-titiler):
embedding a custom classified colormap as inline JSON in a TiTiler tile
URL's `colormap` query param worked everywhere except ArcGIS Online Map
Viewer, where it silently failed to render until the JSON was minified.
Minifying fixed it for this one ramp, but it's fragile — registering each
ramp as a **named colormap** server-side would let ArcGIS (and everything
else) reference it via `colormap_name=<short-plain-name>`, a query value
with zero special characters, immune to whatever URL
decode/re-encode handling caused the original problem.

## Versions used for this investigation

Installed locally (not necessarily what's pinned in
`VCGI/titiler-deployment`'s vendored copy — check that before assuming
this applies unmodified):

- `rio-tiler` 9.4.10
- `titiler.core` 2.4.0

## The mechanism (confirmed via source, not yet via a live request)

Three pieces, read directly from installed source:

1. **`rio_tiler.colormap.ColorMaps.register()`** — the default colormap
   registry (`rio_tiler.colormap.cmap`, ~211 built-in names) is an
   immutable `ColorMaps` object with a `.register(dict, overwrite=False)`
   method that returns a *new* `ColorMaps` instance with additional
   entries merged in. The dict values can be an inline colormap, **or a
   path to a `.json` file** — `ColorMaps.get()` auto-detects whether that
   JSON is a discrete dict (`{"0": [r,g,b,a], ...}`) or an interval list
   (`[[[min,max],[r,g,b,a]], ...]`, our format) based on its structure, so
   [`titiler-colormap.json`](../dem-color-ramps/11class-feet-aligned/titiler-colormap.json)
   could be registered directly, no reformatting needed:

   ```python
   from rio_tiler.colormap import cmap as default_cmap

   custom_cmap = default_cmap.register({
       "vt-dem-11class-feet-aligned": "path/to/titiler-colormap.json",
   })
   ```

2. **`titiler.core.dependencies.create_colormap_dependency(cmap)`** — a
   factory that builds a FastAPI dependency function whose
   `colormap_name` query parameter is typed as `Literal[tuple(cmap.list())]`
   — i.e., the registered name becomes a validated, documented enum value
   in the API (and OpenAPI schema), not just a magic string:

   ```python
   from titiler.core.dependencies import create_colormap_dependency

   colormap_dep = create_colormap_dependency(custom_cmap)
   ```

3. **`TilerFactory(colormap_dependency=...)`** — TiTiler's tiler factory
   classes accept a `colormap_dependency` constructor parameter (default:
   `titiler.core.dependencies.ColorMapParams`, itself just
   `create_colormap_dependency(default_cmap)` built at import time). Pass
   the custom one in when constructing the factory.

### The part that needs deployment-layer, not vendored-source, changes

`VCGI/titiler-deployment` runs the upstream app unmodified
(`Mangum(titiler.application.main:app)`, per that repo's own README) — it
doesn't construct its own `TilerFactory`. Two ways to inject the custom
colormap without editing the vendored `titiler/` source:

- **Preferred — FastAPI `dependency_overrides` in `handler.py`:** after
  importing the stock `titiler.application.main.app`, override just the
  colormap dependency on the already-built app instance:

  ```python
  from titiler.application.main import app
  from titiler.core.dependencies import ColorMapParams, create_colormap_dependency
  from rio_tiler.colormap import cmap as default_cmap

  custom_cmap = default_cmap.register({
      "vt-dem-11class-feet-aligned": "titiler-colormap.json",  # bundled alongside handler.py
  })
  app.dependency_overrides[ColorMapParams] = create_colormap_dependency(custom_cmap)
  ```

  This only works if the upstream app's COG `TilerFactory` was actually
  constructed with the default `colormap_dependency=ColorMapParams` (the
  exact object), since `dependency_overrides` matches by the original
  callable's identity. That's true in the versions inspected here, but
  **not confirmed against whatever version is actually vendored in
  `titiler-deployment`** — check `titiler/src/titiler/application/main.py`
  there before assuming this applies as-is.

- **Fallback — construct a custom app:** if the override approach doesn't
  match up (e.g. a different TiTiler version wires the factory
  differently), build a small custom FastAPI app in the deployment layer
  that imports `TilerFactory` from the vendored `titiler.core` directly,
  passing `colormap_dependency` at construction time, and replicates
  whatever subset of `titiler.application.main`'s setup (TMS params,
  CORS, etc.) actually matters for this deployment. More code to
  maintain, and diverges further from pure upstream tracking — only do
  this if the override approach genuinely doesn't work.

## What's left before this is real

1. Confirm the override approach against the **actual vendored version**
   in `titiler-deployment`, not just a freshly `pip install`ed copy.
2. Actually test a tile request end-to-end (a `TestClient`/local run
   against a small test raster would be enough — no need to hit the full
   statewide DEM COG just to prove the mechanism).
3. Decide a naming convention for registered colormaps (e.g. prefix with
   `vt-` or `vcgi-` to avoid any collision with the ~211 built-in
   matplotlib-derived names already registered).
4. Decide whether to register every basemap ramp this way as they're
   built, or only ones that actually hit the ArcGIS Online URL-encoding
   problem (minifying may just keep being good enough for most cases).
5. Deploy to staging first (`vt-titiler-lambda-prod` in the staging
   account, per `titiler-deployment`'s README), verify, then production.

## Related

- [`foundational-layers.md`](foundational-layers.md#raster--titiler) —
  the confirmed ArcGIS Online minification gotcha this would solve
- [`../dem-color-ramps/11class-feet-aligned/README.md`](../dem-color-ramps/11class-feet-aligned/README.md#applying-in-titiler) —
  the ramp this was motivated by
