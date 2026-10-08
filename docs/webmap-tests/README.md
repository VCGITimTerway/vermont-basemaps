# Webmap Tests

Named ArcGIS Online web maps built to test basemap appearance, each
embedded as a live, working example via GitHub Pages (plain repo
markdown can't render an `<iframe>` — github.com strips them — so each
test gets a small static HTML page alongside its documentation).

**Prerequisite for every entry here:** the web map item's sharing level
must be set to **Everyone (public)** in ArcGIS Online, and the item's
**"Allow others to embed this map"** option must be enabled (both in
Content → item → Share/Settings). Without both, the embed shows a
sign-in wall instead of the map for anyone outside VCGI's org — this has
bitten the first entry below already, see its README.

## Adding a new test

1. In ArcGIS Online: set the item's sharing to Everyone, enable
   embedding, and grab the share URL (Share → Link, or the `arcg.is`
   short link — either works as the iframe `src`).
2. Create `docs/webmap-tests/<slug>/` with:
   - `index.html` — the embed page (copy an existing one, swap the title
     and iframe `src`)
   - `README.md` — layers shown + design decisions (pull the actual
     layer list from the web map JSON once the item is public, rather
     than describing from memory)
3. Add a row below.
4. Live URL pattern: `https://vcgitimterway.github.io/vermont-basemaps/webmap-tests/<slug>/`

## Tests

| Test | Live embed | Notes |
|---|---|---|
| [Topographic — Test 01 (Styled DEM)](topographic-test-01-styled-dem/README.md) | [embed](https://vcgitimterway.github.io/vermont-basemaps/webmap-tests/topographic-test-01-styled-dem/) | Public, layer list documented from the actual web map JSON |
