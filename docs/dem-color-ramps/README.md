# DEM Color Ramps

Color ramp variants for the hydro-flattened, QL1 lidar-derived statewide
DEM (`STATEWIDE_2023_35cm_DEMHF.tif`). Each subfolder is a self-contained
variant with its own rationale, class breaks/colors, and GDAL reference
file, so alternatives can be developed without overwriting a working
version.

## Variants

- [`11class-feet-aligned/`](11class-feet-aligned/README.md) — **saved
  keeper.** 11-class classified (layer-tint) scheme, breaks aligned to
  round feet values (finer near 0–500 ft and 3500–4000 ft, 500 ft steps
  in between) to sit under foot-labeled contours. Desaturated for
  hillshade blending.
