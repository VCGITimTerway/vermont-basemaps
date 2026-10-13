# Alpine Ski Lifts — PMTiles Proof of Concept

A working, spec-compliant PMTiles archive built from the live
[VT Data — E911 Alpine Ski Lifts](https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Emergency_ALPINELIFTS_line_SP_v1/FeatureServer/0)
hosted feature layer (172 line features — chairlifts, surface lifts, etc.
— with `LIFTTYPE`/`LIFTNAME`/`RESORTNAME` attributes), proving out the
export → tile → PMTiles pipeline end to end for the first time in this
repo.

**[`alpine-ski-lifts-poc.pmtiles`](alpine-ski-lifts-poc.pmtiles)** —
26 KB, 67 tiles across zoom levels 6/8/10/12, one layer
(`alpine_ski_lifts`). Verified by reading the archive back and decoding a
tile: geometry and attributes round-trip correctly.

## How this was built — and why it's a proof of concept, not production

[`build_poc.py`](build_poc.py) is a **pure-Python** pipeline: query the
live service → clip each feature per tile (with a small buffer) using
`shapely` → encode each tile as MVT via `mapbox_vector_tile.encode()`
(its `quantize_bounds` option handles scaling coordinates to the tile's
0–4096 extent) → write a standard MBTiles sqlite file → convert to
PMTiles via the official `pmtiles` package's `mbtiles_to_pmtiles()`.

This exists because **neither Docker nor tippecanoe are available in
this environment** — tippecanoe isn't a native Windows tool and needs
Docker to run (per
[`VCGI/pmtiles`](https://github.com/VCGI/pmtiles)'s own documented
approach), and GDAL's Python bindings have no prebuilt wheel for this
Python/platform combination. The hand-rolled version above proves PMTiles
compatibility and the overall shape of the pipeline, but it's missing
what tippecanoe actually does well:

- Automatic zoom-level/simplification tuning based on feature density
  (this script uses four fixed zoom levels with no line simplification)
- Battle-tested tile-boundary clipping (this script's 5%-buffer clip is
  a reasonable approximation, not tippecanoe's actual algorithm)
- Production-scale performance for large datasets (fine for 172 features;
  not how you'd want to process, say, statewide parcels)

**For a real production build, use tippecanoe directly** once Docker is
available (your own machine, or the AWS-hosted pipeline described in
[`VCGI/pmtiles`](https://github.com/VCGI/pmtiles)):

```bash
curl -o alpine-ski-lifts.geojson \
  "https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/FS_VCGI_OPENDATA_Emergency_ALPINELIFTS_line_SP_v1/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=geojson"

tippecanoe -o alpine-ski-lifts.pmtiles \
  -l alpine_ski_lifts \
  -Z6 -z14 \
  --name="Alpine Ski Lifts" \
  alpine-ski-lifts.geojson
```

(`-Z6 -z14` picks a zoom range to taste; tippecanoe's defaults are
usually reasonable to start from and adjust after viewing the output.)

## Verifying/viewing a `.pmtiles` file

- [`VCGI/pmtiles`](https://github.com/VCGI/pmtiles)'s `inspect-pmtiles.mjs`
  script (schema, zoom range, bounds, per-layer fields) works against any
  `.pmtiles` file, local or remote.
- [pmtiles.io](https://pmtiles.io) has a browser-based viewer that accepts
  a local file directly — the quickest way to look at this one.

## Related

- [`../../architecture/cross-platform-publishing.md`](../../architecture/cross-platform-publishing.md) —
  the per-layer plan this proof of concept comes from
