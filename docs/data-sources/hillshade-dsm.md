# DSM Hillshade

## What is this data?

A hillshade derived from the **digital surface model** (DSM) rather than
the bare-earth DEM — i.e., it includes buildings, tree canopy, and other
above-ground features in the shading, unlike
[Bare Earth Hillshade](hillshade-bare-earth.md). TODO: confirm the
intended use case this serves that bare-earth hillshade doesn't (e.g.
urban/canopy context layers vs. pure terrain relief).

## Stewardship

- **Maintained by:** TODO
- **Update cadence:** TODO
- **Last known update:** TODO

## Derivation

- **Input sources:** A digital surface model (DSM) derived from the same
  lidar acquisition as the bare-earth products — TODO: confirm which DSM
  product and acquisition.
- **Methodology:** TODO

## Use cases & limitations

- **Intended use cases:** TODO
- **Known limitations / caveats:** TODO
- **Appropriate scale / zoom range:** TODO

## Current source

- **Service:** TODO
- **Format:** Cloud-Optimized GeoTIFF (COG), presumed (per the raster
  products list in [`../architecture/foundational-layers.md`](../architecture/foundational-layers.md#vcgi-maintained-raster-products))
- **Projection (EPSG):** TODO
- **Geometry type:** N/A (raster)

## Path to PMTiles / TiTiler output

- **Target format:** TiTiler, presumably — not yet tested
- **Pipeline steps:** TODO
- **Known gaps / blockers:** Not yet tested with TiTiler; no styling
  preset defined; unclear whether this basemap effort needs DSM hillshade
  at all or only bare-earth

## Related

- Architecture doc row: [`../architecture/foundational-layers.md`](../architecture/foundational-layers.md#vcgi-maintained-raster-products)
