# Bare Earth DEM

## What is this data?

A statewide, hydro-flattened digital elevation model: ground-surface
elevation with water surfaces (rivers, lakes, flooded quarries) flattened
to a constant elevation per water body rather than left as noisy
lidar-return surface. This is the raster the basemap color ramps in
[`../dem-color-ramps/`](../dem-color-ramps/) are built against.

## Stewardship

- **Maintained by:** TODO
- **Update cadence:** TODO — presumably tied to the statewide lidar
  acquisition cycle, not a regular refresh
- **Last known update:** 2023 acquisition (per filename
  `STATEWIDE_2023_35cm_DEMHF.tif`)

## Derivation

- **Input sources:** QL1 airborne lidar (statewide). QL1 (USGS Lidar Base
  Specification Quality Level 1) is the higher-density lidar class —
  nominal pulse spacing ≤ 0.35 m, roughly ≥ 8 points/m². This is a general
  industry definition, not VCGI-specific — confirm VCGI's actual
  acquisition parameters/vendor/flight dates separately.
- **Methodology:** Hydro-flattening applied to the bare-earth surface
  (TODO: specifics of the hydro-flattening/breakline process used).

## Use cases & limitations

- **Intended use cases:** Elevation color ramps / hypsometric tinting for
  basemaps (this repo's primary use), hillshade generation, general
  terrain analysis.
- **Known limitations / caveats:**
  - Min elevation in the data (-2.60 m / -8.5 ft) is almost certainly a
    flooded quarry or other depression rather than true sea-level
    elevation — don't treat the statewide min as a data error without
    checking.
  - Vertical units are **meters** despite the horizontal CRS being in US
    survey feet (see below) — easy to mix up when setting stretch/classify
    breaks.
  - NoData value is `-999999` (not `0` or `NaN`) — reclassification logic
    needs to explicitly exclude it.
- **Appropriate scale / zoom range:** TODO

## Current source

- **Service:** `https://s3.us-east-2.amazonaws.com/vtopendata-prd/Elevation/STATEWIDE_2023_35cm_DEMHF.tif`
- **Format:** Cloud-Optimized GeoTIFF (COG), float32
- **Projection (EPSG):** EPSG:6589 (NAD83(2011) / Vermont, horizontal —
  US survey feet); vertical values are in **meters**
- **Geometry type:** N/A (raster)
- **Other confirmed stats:** NoData `-999999`; statewide min **-2.60 m**
  (-8.5 ft), max **1339.65 m** (4,395 ft, matches Mt. Mansfield's summit)

## Path to PMTiles / TiTiler output

- **Target format:** Served dynamically via TiTiler (no format conversion
  needed — the COG works as-is). A separate Terrarium RGB-encoded PMTiles
  tileset also exists for open-source/client-side elevation use (see
  [`../architecture/foundational-layers.md`](../architecture/foundational-layers.md#vector--pmtiles--parallel-esri-vector-tiles))
  — that's a different use case (encoded values, not a styled visual) and
  isn't usable directly in ArcGIS Online.
- **Pipeline steps:**
  1. Already live: `https://titiler.geo.vermont.gov/cog/...?url=s3://vtopendata-prd/Elevation/STATEWIDE_2023_35cm_DEMHF.tif` with `colormap`/`rescale` query params for styling.
  2. Per-basemap-variant styling presets (Light/Dark/Physical Geography)
     still need to be decided and captured via `titiler-endpoint-generator`
     — see architecture doc gap #5.
- **Known gaps / blockers:** None for basic serving; styling presets per
  basemap variant are the remaining work (shared with the hillshade below).

## Related

- Architecture doc row: [`../architecture/foundational-layers.md`](../architecture/foundational-layers.md#vcgi-maintained-raster-products)
- Color ramp work built on this DEM: [`../dem-color-ramps/`](../dem-color-ramps/)
