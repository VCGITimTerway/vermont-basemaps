# Bare Earth Hillshade

## What is this data?

A hillshade (relief shading) raster derived from the bare-earth DEM — used
as the base relief layer underneath the elevation color ramp in the
basemaps (see [`../dem-color-ramps/`](../dem-color-ramps/)), rather than
ground truth on its own.

## Stewardship

- **Maintained by:** VCGI Lidar Program. Statewide COG build/publishing
  credited to Steve Fugate (VCGI, Lidar Program Manager). Source lidar
  acquisition/processing and hillshade generation contracted to Sanborn
  Map Company, Inc.
- **Update cadence:** "None planned" — tied to the 2023 lidar acquisition,
  not refreshed on a schedule; regenerated only if/when the source DEM is
  regenerated from a new acquisition.
- **Last known update:** Acquisition Spring 2023 (2023-04-20 to
  2023-05-13); COG published 2026-06-01.
- **Source:** [published FGDC metadata, `ElevationOther_HILSHD0p35M2023`](https://maps.vcgi.vermont.gov/gisdata/metadata/ElevationOther_HILSHD0p35M2023.htm)

## Derivation

- **Input sources:** [Bare Earth DEM](dem-bare-earth.md) (same 2023 QL1
  lidar acquisition, same vendor/program).
- **Methodology:** "Traditional" hillshade (single light source), per the
  metadata's own series title. Illumination: azimuth 315°, altitude 45°
  (standard defaults). Generated from the bare-earth DEM tiles in Global
  Mapper, one GeoTIFF per 1400×1400 m tile, then mosaicked by VCGI into a
  statewide COG via `gdal translate` (JPEG95 compression — lossy, unlike
  the DEM's lossless LERC/LZW).

## Use cases & limitations

- **Intended use cases:** Relief shading underneath a styled elevation
  color ramp; not intended as a standalone visual. (The metadata itself
  doesn't distinguish a use case beyond "produce high accuracy
  traditional Hillshade" — this repo's blended-under-a-color-ramp use is
  our own application, not a stated original purpose.)
- **Known limitations / caveats:**
  - **Value range is 0–255, and 255 is NoData** — *not* a valid bright
    illumination value. This matters directly for any TiTiler
    colormap/rescale: naively rescaling 0–255 to a grayscale ramp would
    render NoData pixels as solid white instead of transparent. Must
    explicitly mask out 255, not just clip/rescale through it.
  - The light/dark endpoints used in basemap testing so far (**20**→
    `#E2E2E2`, **254**→`#555656`) are a *display stretch* chosen in
    ArcGIS Pro, not the full valid data range (0–254, since 255 is
    NoData) — confirm whether 20 was chosen deliberately (e.g. to avoid
    using the darkest/lightest few values) or is just where the data
    happened to bottom out statewide.
  - Same accuracy caveats as the source DEM apply (no independent
    accuracy assessment of this derived product by VCGI).
- **Appropriate scale / zoom range:** TODO

## Current source

- **Service:** `https://s3.us-east-2.amazonaws.com/vtopendata-prd/Elevation/STATEWIDE_2023_35cm_HILSHD.tif`
  (key confirmed reachable; tiled originals are at
  `Elevation/_Tiles/LIDAR/0_35M/2023/HILSHD/` in the same bucket, per the
  metadata's distribution info)
- **Format:** Cloud-Optimized GeoTIFF (COG), uint8
- **Projection (EPSG):** EPSG:6589 (NAD83(2011) / Vermont, US survey
  feet), confirmed by opening the COG directly — same CRS discrepancy as
  the DEM applies here too (metadata narrative describes meters; actual
  COG is ftUS). See the [DEM profile](dem-bare-earth.md) for the full
  discrepancy note — same vendor/pipeline produced both.
- **Geometry type:** N/A (raster)
- **Other confirmed stats:** Per the published metadata's own attribute
  definition and confirmed by opening the COG directly: local illumination
  value, range 0–255, **NoData = 255**.

## Path to PMTiles / TiTiler output

- **Target format:** Served dynamically via TiTiler, same as the DEM — no
  format conversion needed.
- **Pipeline steps:**
  1. TiTiler COG endpoint with a grayscale colormap/rescale matching the
     20–254 / `#E2E2E2`–`#555656` stretch already validated in ArcGIS Pro
     testing, **with pixel value 255 explicitly masked as NoData/alpha=0**
     rather than rescaled.
  2. Needs the same per-basemap-variant styling presets work as the DEM
     (architecture doc gap #5) — hillshade stretch likely stays constant
     across variants while the DEM color ramp changes, but that assumption
     should be confirmed, not assumed.
- **Known gaps / blockers:** Exact statewide COG S3 key not yet confirmed
  (inferred from naming convention, not verified); horizontal CRS not
  independently verified against the file itself.

## Related

- Architecture doc row: [`../architecture/foundational-layers.md`](../architecture/foundational-layers.md#vcgi-maintained-raster-products)
- Blended with [`dem-bare-earth.md`](dem-bare-earth.md) at 50% opacity in
  the monochrome canvas ramp testing — see
  [`../dem-color-ramps/11class-monochrome-canvas/README.md`](../dem-color-ramps/11class-monochrome-canvas/README.md)
