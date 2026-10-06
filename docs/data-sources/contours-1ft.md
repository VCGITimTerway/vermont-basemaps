# 1' Contours (QL2 Lidar-Derived)

## What is this data?

Statewide 1-foot contour lines derived from lidar — finer interval than
the "major"/labeled contours shown at small scale, used for the
zoom-dependent contour basemap layer tested in
[`../dem-color-ramps/11class-monochrome-canvas/`](../dem-color-ramps/11class-monochrome-canvas/README.md)
(e.g. the 250 ft-interval contours visible in that variant's screenshots
are a generalized/filtered subset of this source at those zoom levels).

## Stewardship

- **Maintained by:** TODO
- **Update cadence:** TODO — tied to lidar acquisition cycle, not a
  regular refresh
- **Last known update:** TODO

## Derivation

- **Input sources:** QL2 airborne lidar (statewide). QL2 (USGS Lidar Base
  Specification Quality Level 2) is a lower-density class than the QL1
  lidar used for the [Bare Earth DEM](dem-bare-earth.md) — nominal pulse
  spacing ≤ 0.7 m, roughly ≥ 2 points/m². This is a general industry
  definition, not VCGI-specific — confirm actual acquisition
  parameters/vendor/flight dates separately. Worth confirming whether this
  is the *same* lidar acquisition as the QL1 DEM or a separate, coarser
  one — the differing quality level naming (QL1 vs. QL2) suggests they may
  not be the same source.
- **Methodology:** TODO — contour generation interval/smoothing/generalization
  by zoom level.

## Use cases & limitations

- **Intended use cases:** Basemap contour layer, zoom-dependent interval
  (e.g. coarser intervals at small scale, full 1 ft detail at large scale).
- **Known limitations / caveats:** TODO — positional accuracy relative to
  the QL1 DEM if they're different lidar sources; currency relative to
  more recent QL1 acquisitions.
- **Appropriate scale / zoom range:** Zoom-dependent by design — specific
  z-level/interval breakpoints not yet documented here.

## Current source

**Not a hosted feature layer** — unlike most other VSDI vector layers,
published only via ArcGIS Server/AGOL tile services, with no feature
service identified yet:

- **Service:** [ArcGIS Server MapServer, cached](https://maps.vcgi.vermont.gov/arcgis/rest/services/EGC_services/MAP_VCGI_LIDARCONTOURS_WM_CACHE_v1/MapServer)
- **Service (vector tiles):** [Esri Vector Tile Service](https://tiles.arcgis.com/tiles/BkFxaEFNwHqX3tAw/arcgis/rest/services/VECTOR_VCGI_CN1TGEN_WM_v1/VectorTileServer)
- **Format:** Cached map tiles (first service) + pre-built vector tiles
  (second service) — both are already-tiled outputs, not a queryable
  feature service
- **Projection (EPSG):** EPSG:3857 (Web Mercator), confirmed for both
  services
- **Geometry type:** Line

## Path to PMTiles / TiTiler output

- **Target format:** PMTiles (vector), for open-source/MapLibre
  consumption
- **Pipeline steps:**
  1. **Blocked on finding a source-of-truth export.** Neither existing
     service is a queryable feature service — the standard AGOL hosted
     feature layer → FlatGeobuf/GeoJSON → tippecanoe path assumed
     elsewhere in this repo doesn't have an obvious starting point here.
     Need to identify whether an underlying feature class/feature service
     exists (e.g. in ArcGIS Server's `EGC_services`) that the Vector Tile
     Service was itself generated from, and use that as the PMTiles
     source instead of trying to extract geometry from the tile services.
  2. Once a source export exists: standard tippecanoe → PMTiles pipeline
     (see [`../architecture/foundational-layers.md`](../architecture/foundational-layers.md#vector--pmtiles--parallel-esri-vector-tiles)).
- **Known gaps / blockers:**
  - This is the clearest existing case of the "two independent pipelines"
    problem in the architecture doc (gap #1) — the cached MapServer and
    the Vector Tile Service are not confirmed to be generated from a
    shared export.
  - No PMTiles equivalent exists yet.
  - Styling is currently authored directly in Esri's Vector Tile Style
    Editor against the existing Vector Tile Service (see the contour
    color work in
    [`../dem-color-ramps/11class-monochrome-canvas/`](../dem-color-ramps/11class-monochrome-canvas/README.md))
    — once a MapLibre `style.json` exists for the PMTiles version, the two
    styles will need to be kept in sync by hand (architecture doc gap #3).

## Related

- Architecture doc row: [`../architecture/foundational-layers.md`](../architecture/foundational-layers.md#vsdi-vermont-spatial-data-infrastructure)
- Contour line color recommendation: [`../dem-color-ramps/11class-monochrome-canvas/README.md`](../dem-color-ramps/11class-monochrome-canvas/README.md#companion-layers)
