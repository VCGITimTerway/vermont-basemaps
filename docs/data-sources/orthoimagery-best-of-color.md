# Best of Color Imagery

## What is this data?

A statewide "best available" color orthoimagery mosaic — presumably
compiled from multiple acquisitions/years, selecting the best source per
area, but that's an assumption from the name, not yet confirmed. TODO:
confirm what "best of" means here (newest available vs. some quality
criterion vs. a fixed year).

## Stewardship

- **Maintained by:** TODO
- **Update cadence:** TODO
- **Last known update:** TODO

## Derivation

- **Input sources:** TODO — which acquisition(s)/years this mosaic draws
  from
- **Methodology:** TODO — mosaicking/color-balancing approach, resolution

## Use cases & limitations

- **Intended use cases:** Likely an imagery basemap layer/toggle, possibly
  independent from the Light/Dark/Physical Geography basemap family rather
  than blended into them — TODO confirm.
- **Known limitations / caveats:** TODO — currency (imagery can be several
  years old in places), resolution varies by source acquisition if it's a
  multi-year mosaic
- **Appropriate scale / zoom range:** TODO

## Current source

- **Service:** TODO
- **Format:** Cloud-Optimized GeoTIFF (COG), presumed
- **Projection (EPSG):** TODO
- **Geometry type:** N/A (raster)

## Path to PMTiles / TiTiler output

- **Target format:** TiTiler, presumably (RGB COG, no colormap styling
  needed — it's already a visual image, not an encoded value raster)
- **Pipeline steps:** TODO
- **Known gaps / blockers:** Not yet tested with TiTiler for this project

## Related

- Architecture doc row: [`../architecture/foundational-layers.md`](../architecture/foundational-layers.md#vcgi-maintained-raster-products)
