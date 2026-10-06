<!--
Copy this file to docs/data-sources/<layer-slug>.md and fill it in.
Leave a field as "TODO" rather than guessing — a wrong "who maintains this"
or "update cadence" is worse than an honest blank, since someone will
eventually act on it as if it were confirmed.
-->

# <Layer Name>

## What is this data?

Plain-language description of what the dataset represents and why it
exists. Not "how it's formatted" — that's below.

## Stewardship

- **Maintained by:** TODO — program/division/partner organization
- **Update cadence:** TODO — e.g. annual, on-demand, tied to a lidar
  acquisition cycle
- **Last known update:** TODO

## Derivation

- **Input sources:** TODO — imagery/lidar acquisition, survey data,
  municipal submissions, other source datasets it's built from
- **Methodology:** TODO — how it's produced/classified/QA'd from those
  inputs

## Use cases & limitations

- **Intended use cases:** TODO
- **Known limitations / caveats:** TODO — positional accuracy, currency
  lag, known gaps in coverage, anything a consumer could misuse this data
  by not knowing
- **Appropriate scale / zoom range:** TODO

## Current source

- **Service:** TODO — link
- **Format:** TODO — hosted feature layer / MapServer / vector tile
  service / COG, etc.
- **Projection (EPSG):** TODO — confirm against the service's own
  `spatialReference`, don't infer from naming alone
- **Geometry type:** TODO

## Path to PMTiles / TiTiler output

- **Target format:** PMTiles (vector) / TiTiler-served COG (raster) /
  parallel Esri Vector Tile Service — pick what applies
- **Pipeline steps:**
  1. TODO
- **Known gaps / blockers:** TODO — e.g. no confirmed source-of-truth
  export, no PMTiles equivalent built yet, style authoring not yet ported

## Related

- Architecture doc row: [`../architecture/foundational-layers.md`](../architecture/foundational-layers.md)
- Other notes
