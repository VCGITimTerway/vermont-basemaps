# Reference Basemaps

External basemap styles kept here as design and technical references, not
as styles this repo depends on or redistributes. They're useful for two
different reasons:

- **Design reference** — established, widely-used visual treatments
  (muted/canvas-style light, dark, general-purpose "bright", 3D) worth
  comparing our own Light/Dark/Physical Geography/monochrome work against.
- **Technical reference** — most entries below are [MapLibre/Mapbox GL
  style.json](https://maplibre.org/maplibre-style-spec/) documents, several
  built against the [OpenMapTiles](https://github.com/openmaptiles/openmaptiles)
  vector tile schema, a mature, widely-adopted schema for exactly the kind
  of vector basemap tiles this project is moving toward with PMTiles (see
  [`../architecture/foundational-layers.md`](../architecture/foundational-layers.md)).
  Worth consulting for source-layer naming and layer-ordering conventions
  when designing our own PMTiles vector schema.

Entries are grouped by source below, since not everything here will come
from OpenMapTiles — add a new `## <Source>` section for anything from
elsewhere rather than assuming everything shares a license or schema.

## Source: OpenMapTiles

Maintained under the [openmaptiles GitHub org](https://github.com/openmaptiles);
source for the vector tile schema itself lives in
[openmaptiles/openmaptiles](https://github.com/openmaptiles/openmaptiles).

| Style | Repo | Vermont demo | Description | License |
|---|---|---|---|---|
| MapTiler Basic | [maptiler-basic-gl-style](https://github.com/openmaptiles/maptiler-basic-gl-style) | [demo](https://openmaptiles.github.io/maptiler-basic-gl-style/#7.57/43.96/-72.485) | Tries to stay in the background and only give the most relevant information. | BSD-3-Clause (style code); derived from Mapbox Open Styles |
| OSM Bright | [osm-bright-gl-style](https://github.com/openmaptiles/osm-bright-gl-style) | [demo](https://openmaptiles.github.io/osm-bright-gl-style/#7.95/43.899/-72.682) | General-purpose basemap showcasing the detail of OpenStreetMap data; a good starting point for more complex basemaps. | BSD-3-Clause (style code); derived from Mapbox Open Styles |
| Positron | [positron-gl-style](https://github.com/openmaptiles/positron-gl-style) | [demo](https://openmaptiles.github.io/positron-gl-style/#7.85/43.863/-72.595) | Light basemap, ideal as a non-obtrusive base for data visualizations. | BSD-3-Clause (style code); **cartography by Stamen Design/Paul Norman, via CartoDB Basemaps, CC-BY 3.0** — attribution required if we reuse/derive from this design |
| Dark Matter | [dark-matter-gl-style](https://github.com/openmaptiles/dark-matter-gl-style) | [demo](https://openmaptiles.github.io/dark-matter-gl-style/#7.85/43.9/-72.506) | Dark basemap, a good starting point for other darker designs. | BSD-3-Clause (style code); **cartography by Stamen Design/Paul Norman, via CartoDB Basemaps, CC-BY 3.0** — attribution required if we reuse/derive from this design |
| Fiord Color | [fiord-color-gl-style](https://github.com/openmaptiles/fiord-color-gl-style) | [demo](https://openmaptiles.github.io/fiord-color-gl-style/#7.88/43.88/-72.539) | Cool blue-toned basemap optimized for data visualizations; muted palette keeps overlay data layers in focus. | BSD-3-Clause (style code); **same CartoDB/Stamen lineage as Positron/Dark Matter, CC-BY 3.0** — attribution required if we reuse/derive from this design |
| MapTiler 3D | [maptiler-3d-gl-style](https://github.com/openmaptiles/maptiler-3d-gl-style) | [demo](https://openmaptiles.github.io/maptiler-3d-gl-style) (global demo, no Vermont-specific view provided) | 3D buildings extrusion style; a GL basemap demonstrating 3D building rendering from the OpenMapTiles schema. | BSD-3-Clause (style code); derived from Mapbox Open Styles |

### Notes

- "BSD-3-Clause (style code)" covers the `style.json`/build tooling in each
  repo. It's separate from the cartographic design license — GitHub's own
  license detector reports `NOASSERTION` for all six repos since the
  license terms are nonstandard (split between code and design), so always
  check each repo's `LICENSE.md` directly rather than trusting the
  detected badge.
- Positron, Dark Matter, and Fiord Color all trace back to the same
  Stamen/CartoDB-designed cartography (CC-BY 3.0). If our own Light, Dark,
  or monochrome basemaps end up visually derivative of one of these three
  specifically (as opposed to just "inspired by, redrawn independently"),
  attribution is required, not optional.
- MapTiler Basic, OSM Bright, and MapTiler 3D trace back to Mapbox Open
  Styles instead, with no equivalent CC-BY design requirement noted in
  their license files.
