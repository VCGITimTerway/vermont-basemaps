# Bare Earth DEM

## What is this data?

A statewide, hydro-flattened digital elevation model: ground-surface
elevation with water surfaces (rivers, lakes, flooded quarries) flattened
to a constant elevation per water body rather than left as noisy
lidar-return surface. This is the raster the basemap color ramps in
[`../dem-color-ramps/`](../dem-color-ramps/) are built against.

## Stewardship

- **Maintained by:** VCGI Lidar Program. Statewide COG build/publishing
  credited to Steve Fugate (VCGI, Lidar Program Manager). Source lidar
  acquisition/processing contracted to Sanborn Map Company, Inc.
- **Update cadence:** "None planned" (per published metadata's
  `Maintenance_and_Update_Frequency`) — this is a point-in-time product
  tied to the 2023 statewide lidar acquisition, not refreshed on a
  schedule. A new version would come from a new statewide (or partial)
  lidar acquisition, not a periodic update to this one.
- **Last known update:** Acquisition: Spring 2023 (2023-04-20 to
  2023-05-13). COG published/repackaged 2026-06-01 (see Derivation —
  this is a later repackaging of the same 2023 acquisition, not a new
  survey).
- **Source:** [published FGDC metadata, `ElevationDEM_DEMHF0p35M2023`](https://maps.vcgi.vermont.gov/gisdata/metadata/ElevationDEM_DEMHF0p35M2023.htm)

## Derivation

- **Input sources:** QL1 airborne lidar, statewide, nominal pulse spacing
  0.35 m, flown Spring 2023 (no snow cover, rivers at/below normal
  levels). Project spec: USGS National Geospatial Program Base Lidar
  Specification 2022, Revision A (3DEP QL1). Classified LAS 1.4 point
  cloud, Class 2 (ground) returns used for the DEM. Calibrated against
  103 ground control points; accuracy independently checked against 348
  additional points (200 NVA — bare earth/urban; 148 VVA — tall
  grass/brush/low trees), not used in calibration.
- **Methodology:**
  1. Class 2 (ground) lidar points + hydro breaklines → 0.35 m
     hydro-flattened raster DEM, via automated LP360 scripting (one
     GeoTIFF per 1400×1400 m tile).
  2. Each tile manually reviewed in Global Mapper for surface
     anomalies/incorrect elevations.
  3. Vendor-delivered tiles imported, renamed to current convention, and
     mosaicked by VCGI into **this statewide COG** via `gdal translate`
     with LERC compression (`MAX_Z_ERROR=0.01`); per-tile COGs use LZW
     instead.
- **Required vertical accuracy:** 19.6 cm NVA; produced to ASPRS (2014)
  10 cm RMSEz vertical accuracy class.

## Use cases & limitations

- **Intended use cases (per published metadata):** Conservation planning,
  design, research, floodplain mapping, dam safety assessments, elevation
  modeling. This repo's use (color ramps/hypsometric tinting, hillshade
  generation for basemaps) isn't one of the originally stated use cases
  but isn't precluded by them either.
- **Known limitations / caveats:**
  - Min elevation in the data (-2.60 m / -8.5 ft) is almost certainly a
    flooded quarry or other depression rather than true sea-level
    elevation — don't treat the statewide min as a data error without
    checking. (Confirmed by the published metadata's own attribute range:
    `Range_Domain_Minimum: -2.60`, `Range_Domain_Maximum: 1339.65`,
    units meters — exact match to what we found by opening the COG
    directly.)
  - NoData value is `-999999` (not `0` or `NaN`) — reclassification logic
    needs to explicitly exclude it.
  - **No accuracy assessment of this specific DEM/derived products has
    been made by VCGI** (explicit use-constraint language in the
    metadata) — the ASPRS accuracy class above describes the *target
    specification*, not a post-hoc verification of this exact file.
  - Acknowledgement of USGS 3DEP is "appreciated" for derived products
    (not a hard legal requirement per the metadata, but a stated
    courtesy request) — worth doing for any public-facing basemap built
    from this.
  - **CRS discrepancy worth resolving, not silently reconciling:** the
    published metadata's narrative text describes the horizontal
    CRS/datum as *"NAD83(2011), Vermont, **Meters**"* (State Plane zone
    4400) throughout — but opening the actual published COG directly
    (via `rasterio`) returns **EPSG:6589**, which is NAD83(2011) /
    Vermont in **US survey feet**. Either the GDAL translate/mosaic step
    reprojected/re-declared the horizontal units between the vendor
    deliverable and this final COG, or the metadata's CRS narrative is
    stale/copied from a template and never updated for this product.
    Don't assume which is correct — confirm with VCGI before relying on
    either description for a horizontal-unit-sensitive calculation.
- **Appropriate scale / zoom range:** TODO

## Current source

- **Service:** `https://s3.us-east-2.amazonaws.com/vtopendata-prd/Elevation/STATEWIDE_2023_35cm_DEMHF.tif`
  (tiled originals also available under `Elevation/_Tiles/LIDAR/0_35M/2023/DEMHF/`
  in the same bucket)
- **Format:** Cloud-Optimized GeoTIFF (COG), float32
- **Projection (EPSG):** EPSG:6589 (NAD83(2011) / Vermont, horizontal —
  US survey feet, confirmed by opening the COG directly); vertical values
  are in **meters**. See the CRS discrepancy note above — the metadata
  record itself describes the horizontal units as meters, not feet.
- **Geometry type:** N/A (raster)
- **Other confirmed stats:** NoData `-999999`; statewide min **-2.60 m**
  (-8.5 ft), max **1339.65 m** (4,395 ft, matches Mt. Mansfield's summit) —
  confirmed both by opening the COG directly and by the published
  metadata's attribute range.

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
