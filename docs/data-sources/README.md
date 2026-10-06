# Data Sources

Per-layer profiles answering the questions that
[`../architecture/foundational-layers.md`](../architecture/foundational-layers.md)
doesn't: for each source feeding the basemaps, what *is* it, who maintains
it, on what cadence, from what inputs, by what methodology, and for what
intended use/limitations — plus the concrete steps (and gaps) to get it
into a PMTiles or TiTiler-served output.

The architecture doc stays the high-level inventory + delivery-pipeline
overview; these profiles are the deep dive per source. Link back and forth
rather than duplicating — if a fact changes, it should only need updating
in one place.

Use [`TEMPLATE.md`](TEMPLATE.md) for anything not yet profiled below.
Leave fields as `TODO` rather than guessing; most of what's missing here
is institutional knowledge (who maintains it, update cadence, methodology)
that only VCGI staff can fill in accurately.

## Status

| Layer | Profile | Metadata | Pipeline documented |
|---|---|---|---|
| Bare Earth DEM | [`dem-bare-earth.md`](dem-bare-earth.md) | Partial | Yes (TiTiler) |
| Bare Earth Hillshade | [`hillshade-bare-earth.md`](hillshade-bare-earth.md) | Partial | Yes (TiTiler) |
| DSM Hillshade | [`hillshade-dsm.md`](hillshade-dsm.md) | Stub | No |
| Best of Color Imagery | [`orthoimagery-best-of-color.md`](orthoimagery-best-of-color.md) | Stub | No |
| Time in Daylight | [`time-in-daylight.md`](time-in-daylight.md) | Stub (unclear what this product even is) | No |
| 1' Contours (QL2 lidar) | [`contours-1ft.md`](contours-1ft.md) | Partial | Partial — Esri side only |
| Parcels (Active/Inactive) | [`parcels.md`](parcels.md) | Partial | Partial — PMTiles prototyped |
| Boundaries (State/County/Municipal/Village) | [`boundaries.md`](boundaries.md) | Partial | No |
| Protected Lands / Military Sites | [`protected-lands.md`](protected-lands.md) | Partial | No |
| Surface Waters | — not yet started | — | — |
| Base Land Cover / Impervious / Tree Canopy | — not yet started | — | — |
| Mountains and Hills | — not yet started | — | — |
| Tree Centroids / Tree Canopy (next-gen) | — not yet started | — | — |
| Wetlands (VSWI) | — not yet started | — | — |
| E911 layers (driveways, buildings, cemeteries, golf courses, quarries/mines, trails) | — not yet started | — | — |

"Partial" means the current-source facts (service URL, projection, format)
are confirmed, but stewardship/cadence/methodology/limitations are still
`TODO`. "Stub" means the file exists with the template structure but
almost nothing is filled in yet.
