# Bare Earth Hillshade

## What is this data?

A hillshade (relief shading) raster derived from the bare-earth DEM — used
as the base relief layer underneath the elevation color ramp in the
basemaps (see [`../dem-color-ramps/`](../dem-color-ramps/)), rather than
ground truth on its own.

## Stewardship

- **Maintained by:** TODO
- **Update cadence:** TODO — presumably regenerated whenever the source
  DEM is updated
- **Last known update:** TODO

## Derivation

- **Input sources:** [Bare Earth DEM](dem-bare-earth.md) (same QL1 lidar
  acquisition).
- **Methodology:** TODO — illumination angle/azimuth, single vs.
  multidirectional hillshade, any z-factor/exaggeration applied.

## Use cases & limitations

- **Intended use cases:** Relief shading underneath a styled elevation
  color ramp; not intended as a standalone visual.
- **Known limitations / caveats:** TODO
- **Appropriate scale / zoom range:** TODO

## Current source

- **Service:** TODO — same S3 prefix pattern as the DEM presumably
  (`vtopendata-prd`), exact key not yet confirmed here
- **Format:** Cloud-Optimized GeoTIFF (COG)
- **Projection (EPSG):** TODO — confirm against the file's own metadata
- **Geometry type:** N/A (raster)
- **Other confirmed stats:** As styled in current basemap testing — byte
  values, min **20**, max **254**, stretched continuously from `#E2E2E2`
  (light) to `#555656` (dark). (This is the *display stretch* used in
  testing, not necessarily the raw pixel value range — confirm whether
  20/254 are the actual data min/max or just the stretch endpoints chosen.)

## Path to PMTiles / TiTiler output

- **Target format:** Served dynamically via TiTiler, same as the DEM — no
  format conversion needed.
- **Pipeline steps:**
  1. TiTiler COG endpoint with a grayscale colormap/rescale matching the
     20–254 / `#E2E2E2`–`#555656` stretch already validated in ArcGIS Pro
     testing.
  2. Needs the same per-basemap-variant styling presets work as the DEM
     (architecture doc gap #5) — hillshade stretch likely stays constant
     across variants while the DEM color ramp changes, but that assumption
     should be confirmed, not assumed.
- **Known gaps / blockers:** Exact S3 key and raw pixel value range not yet
  confirmed (see Current source above).

## Related

- Architecture doc row: [`../architecture/foundational-layers.md`](../architecture/foundational-layers.md#vcgi-maintained-raster-products)
- Blended with [`dem-bare-earth.md`](dem-bare-earth.md) at 50% opacity in
  the monochrome canvas ramp testing — see
  [`../dem-color-ramps/11class-monochrome-canvas/README.md`](../dem-color-ramps/11class-monochrome-canvas/README.md)
