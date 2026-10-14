# Webmap Tests

Named ArcGIS Online web maps built to test basemap appearance, each
embedded as a live, working example via GitHub Pages (plain repo
markdown can't render an `<iframe>` — github.com strips them — so each
test gets a small static HTML page alongside its documentation).

**Prerequisite for every entry here:** the web map item's sharing level
must be set to **Everyone (public)** in ArcGIS Online (Content → item →
Share). There's no separate "allow embedding" setting for Web Map items —
public sharing alone is sufficient. A `save as` copy does **not** carry
over the original's sharing setting, so this needs doing again for every
new test, not just the first one. Without it, the embed shows a sign-in
wall instead of the map for anyone outside VCGI's org.

## Adding a new test

1. In ArcGIS Online: set the item's sharing to Everyone, and grab the
   share URL (Share → Link, or the `arcg.is` short link — either works as
   the iframe `src`).
2. Create `docs/webmap-tests/<slug>/` with:
   - `index.html` — the embed page (copy an existing one, swap the title
     and iframe `src`)
   - `README.md` — layers shown + design decisions (pull the actual
     layer list from the web map JSON once the item is public, rather
     than describing from memory)
3. Add a row below **and** a matching `<li>` entry in
   [`index.html`](index.html) (the index page's own live-served listing —
   this file is **not** auto-generated from the README table, so both
   need updating or the new test won't be reachable from the top-level
   webmap-tests landing page).
4. Live URL pattern: `https://vcgitimterway.github.io/vermont-basemaps/webmap-tests/<slug>/`

The `index.html` entry includes a thumbnail `<img>` pointing at the
item's live AGOL thumbnail URL:
`https://vcgi.maps.arcgis.com/sharing/rest/content/items/<itemId>/info/thumbnail/ago_downloaded.png`
(confirm the actual filename — it's taken from the item's own `thumbnail`
field, fetchable via `.../sharing/rest/content/items/<itemId>?f=json`,
and isn't always `ago_downloaded.png`). No need to download/commit a
copy — it updates automatically if the item is ever re-saved.

## Tests

| Test | Live embed | Notes |
|---|---|---|
| [Topographic — Test 01 (Styled DEM)](topographic-test-01-styled-dem/README.md) | [embed](https://vcgitimterway.github.io/vermont-basemaps/webmap-tests/topographic-test-01-styled-dem/) | Styled DEM + hillshade terrain, VCGI-sourced water labels, E911 recreation layers |
| [Topographic — Test 01b (World Terrain Labels)](topographic-test-01b-world-terrain-labels/README.md) | [embed](https://vcgitimterway.github.io/vermont-basemaps/webmap-tests/topographic-test-01b-world-terrain-labels/) | Save-as of Test 01; swaps four label layers for one Esri "World Terrain Reference"-styled layer |
| [Topographic — Test 02 (Physical Topo Light)](topographic-test-02-physical-topo-light/README.md) | [embed](https://vcgitimterway.github.io/vermont-basemaps/webmap-tests/topographic-test-02-physical-topo-light/) | Muted hillshade-only terrain (no DEM color ramp), new "Light Roads" and "Buildings White" style variants, intended as a basemap for user-added thematic data |
| [Topographic — Test 02b (World Terrain Labels)](topographic-test-02b-world-terrain-labels/README.md) | [embed](https://vcgitimterway.github.io/vermont-basemaps/webmap-tests/topographic-test-02b-world-terrain-labels/) | Save-as of Test 02; swaps four label layers for the same Esri "World Terrain Reference" layer used in Test 01b |
