# Building Footprints (Esri Community Maps composite)

## What is this data?

The building footprint layer VCGI contributes to Esri's Community Maps
program — and, via that program, the likely ultimate source of the
"Buildings 2022" vector tile layer used in this repo's webmap tests
(though that connection runs through Esri's own processing, not a direct
republish — see [Related](#related)).

**This is a static, point-in-time composite, not a live feed.** The
service's own internal name is `ESRICMP_BuildingFootprintsVT_Ready2Publish`,
and every sampled record's `DATA_SOURCE` field reads **"ESRI CMP EXPORT
20211027"** — confirming it was built once, around **2021-10-27**, from
both land-cover-derived buildings and E911 building footprints as they
existed at that time, with schema changes to match Community Maps'
requirements (`Carto` category codes, `LABEL_LOCAL`, etc.). VCGI hasn't
yet decided what feeds *future* updates to this layer or on what cadence
— that's an open question, not a gap in this documentation.

## Stewardship

- **Maintained by:** TODO (who owns decisions about refreshing this
  composite going forward)
- **Update cadence:** None currently — static since the 2021-10-27 export
- **Last known update:** 2021-10-27 (per `DATA_SOURCE` field, confirmed
  directly from the live service)

## Derivation

- **Input sources:** Land-cover-derived buildings + E911 building
  footprints, as they existed as of the 2021-10-27 export. The per-record
  `DATASOURCENAME`/`DATA_SOURCE` fields exist but don't appear to
  distinguish which original source a given feature came from (sampled
  records all show the same export-batch value, not per-source lineage).
- **Methodology:** TODO — exact merge/dedup process between the two
  source datasets not documented here.

## Use cases & limitations

- **Intended use cases:** Building footprint contribution to Esri
  Community Maps / Living Atlas.
- **Known limitations / caveats:**
  - Static since 2021-10-27 — doesn't reflect any construction/demolition
    since then, nor updates to either source dataset.
  - Schema is Community-Maps-specific (`Carto` numeric category codes,
    `LABEL_LOCAL`/`LABEL_GLOBAL`), not VCGI's native building schema —
    translating back to a VCGI-native building footprint dataset isn't
    a straightforward reversal.
- **Appropriate scale / zoom range:** TODO

## Current source

- **Service:** [`ESRICMP_BuildingFootprintsVT_v1`](https://maps.vcgi.vermont.gov/arcgis/rest/services/VCGI_services/ESRICMP_BuildingFootprintsVT_v1/MapServer/2)
- **Format:** ArcGIS Server MapServer sublayer, `capabilities: Map,Query,Data`
- **Projection (EPSG):** EPSG:32145 (VT State Plane), confirmed
- **Geometry type:** Polygon
- **Key fields:** `Carto` (numeric category, 13 values — Recreation,
  Government, Commercial, Education, Medical, etc.), `LABEL_LOCAL`,
  `Height`/`HeightUnits`/`Levels`/`BuildingHeight`, `DATA_SOURCE`,
  `LASTUPDATE`

## Esri Community Maps contribution

Feeds Esri's Community Maps program as "Building Footprint," filtered by
`Carto` code into 13 categories (Recreation, CommunityCenter,
Transportation, Government, CulturalHeritage, Medical, Hotel, Commercial,
General, Airport, Industrial, Education, Religious), labeled via
`LABEL_LOCAL`, with building height/levels passed through via
`Height`/`HeightUnits`/`BuildingHeight`. Part of VCGI's broader Community
Maps contribution — see
[`../architecture/foundational-layers.md`](../architecture/foundational-layers.md#esri-community-maps-separate-existing-pipeline)
for the full list of layers VCGI contributes and the shared 6-month pull
cadence (though this specific layer's static nature means the "pull" may
just be re-fetching the same 2021 snapshot until VCGI defines a refresh
source).

## Path to PMTiles / TiTiler output

- **Target format:** Undecided — resolve the "what feeds future updates"
  question first. Exporting this static composite as-is would just
  freeze the 2021-10-27 snapshot into a second format, not fix its
  staleness.
- **Known gaps / blockers:** No decision yet on future sourcing/cadence.

## Related

- [`../architecture/foundational-layers.md`](../architecture/foundational-layers.md#esri-community-maps-separate-existing-pipeline)
- [`../architecture/cross-platform-publishing.md`](../architecture/cross-platform-publishing.md) —
  Buildings 2022 row
