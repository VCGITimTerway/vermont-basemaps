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
| Bare Earth DEM | [`dem-bare-earth.md`](dem-bare-earth.md) | Good — sourced from published FGDC metadata | Yes (TiTiler) |
| Bare Earth Hillshade | [`hillshade-bare-earth.md`](hillshade-bare-earth.md) | Good — sourced from published FGDC metadata | Yes (TiTiler) |
| DSM Hillshade | [`hillshade-dsm.md`](hillshade-dsm.md) | Stub | No |
| Best of Color Imagery | [`orthoimagery-best-of-color.md`](orthoimagery-best-of-color.md) | Stub | No |
| Time in Daylight | [`time-in-daylight.md`](time-in-daylight.md) | Stub (unclear what this product even is) | No |
| 1' Contours (QL2 lidar) | [`contours-1ft.md`](contours-1ft.md) | Good — sourced from published FGDC metadata | Partial — Esri side only |
| Parcels (Active/Inactive) | [`parcels.md`](parcels.md) | Good — sourced from published metadata | Partial — PMTiles prototyped |
| Boundaries (State/County/Municipal/Village) | [`boundaries.md`](boundaries.md) | Good — sourced from published FGDC metadata | No |
| Protected Lands / Military Sites | [`protected-lands.md`](protected-lands.md) | Partial | No |
| Surface Waters | — not yet started | — | — |
| Base Land Cover / Impervious / Tree Canopy | — not yet started | — | — |
| Mountains and Hills | — not yet started | — | — |
| Tree Centroids / Tree Canopy (next-gen) | — not yet started | — | — |
| Wetlands (VSWI) | — not yet started | — | — |
| E911 layers (driveways, buildings, cemeteries, golf courses, quarries/mines, trails) | — not yet started | — | — |

"Good" means pulled from VCGI's own published metadata record for that
exact product (cited in each profile), not inferred. "Partial" means the
current-source facts (service URL, projection, format) are confirmed, but
stewardship/cadence/methodology/limitations are still `TODO`. "Stub" means
the file exists with the template structure but almost nothing is filled
in yet.

## Published metadata catalog

VCGI publishes FGDC/ISO metadata for most datasets at
`https://maps.vcgi.vermont.gov/gisdata/metadata/` (browsable directory,
`.htm`/`.txt`/`.xml` per record). This is the single best source for
filling in the `TODO`s above — far more reliable than guessing. Candidate
records found for layers not yet profiled (**not yet confirmed as the
right match — verify before treating as authoritative**, since several
product families have multiple similarly-named variants):

| Layer | Candidate metadata record(s) | Caveat |
|---|---|---|
| DSM Hillshade | No 2023 DSM-hillshade-specific record found; `ElevationOther_DSMFR0p35M2023` (first-return DSM) and `ElevationOther_DSMLR0p35M2023` (last-return) exist as the underlying surface models | Unclear which (if either) the "DSM Hillshade" raster in our inventory is actually generated from — FR vs. LR matters |
| Surface Waters | `WaterHydro_VHDCARTO` — VCGI's cartographic Vermont Hydrography Dataset (waterbodies + waterlines, with perenniality/Strahler order attribution, built from NHD) | Matches well on description, but you flagged this group as "tricky" — don't treat as settled without your input |
| Wetlands (VSWI) | `LandLandcov_Wetlands2016`/`LandLandcov_Wetlands2022` | **Likely a naming mismatch, not the same thing** — these look like land-cover-classification-derived wetlands, whereas VSWI (Vermont Significant Wetland Inventory) is a distinct ANR regulatory dataset. Don't conflate without confirming |
| Base Land Cover / Impervious / Tree Canopy | `LandLandcov_TreeCanopy2016`/`2022` (+ `TIF` raster variants); no obvious "base land cover" or "impervious surfaces" record found by name | Tree Canopy has a plausible match; base land cover and impervious surfaces don't |
| Building Footprints (E911) | `EmergencyE911_FOOTPRINTS` | Good name match, not yet opened/verified |
| Private Driveways (E911) | `EmergencyE911_DW` | Good name match, not yet opened/verified |
| Trails (E911) | `EmergencyE911_TRAILS` | Good name match, not yet opened/verified |
| Cemeteries / Golf Course / Quarries-Mines (E911) | No dedicated records found by name | May be subtypes within `EmergencyE911_LANDMARKS` rather than their own datasets — needs checking |
| Best of Color Imagery | No single "best of" composite record found | Many dated/resolution-specific ortho records exist (e.g. `VTORTHO_0_15M_CLRIR_2023`, `VTORTHO_0_3M_CLRIR_2024`) — "Best of Color Imagery" may be assembled from several of these rather than having its own metadata record |
| Protected Lands / Military Sites | No dedicated record found by name in this catalog | May be published under a name not yet identified |

Say the word if you want these opened up and the matching profiles filled
in the same way as the five above.
