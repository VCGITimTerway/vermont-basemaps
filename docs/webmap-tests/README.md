# Webmap Tests

Named ArcGIS Online web maps built to test basemap appearance, each
embedded as a live, working example via GitHub Pages (plain repo
markdown can't render an `<iframe>` — github.com strips them — so each
test gets a small static HTML page alongside its documentation).

## Reusable Group Layers

For development purposes (adding these basemap layers into your own app
or web map), these **Group layer items** are the priority reference —
add by item ID rather than rebuilding the layer stack by hand. All are
shared publicly. See [Group layers](#group-layers) below for what reuse
does and doesn't give you.

These are designed to combine into a single basemap "style," and **must
be stacked in the order listed** (top row drawn last, i.e. on top).
There will be more than one such combination — the one below is keyed to
**Base Topo** (includes the Lidar DEM Hillshade); a second keyed to a
plain **Base** (without hillshade) is forthcoming.

### Base Topo configuration

| Order | Group | Item ID | Contents |
|---|---|---|---|
| Top | Labels | `0ff87dab7daf4141a5e95a2f8be0715e` | World Terrain Reference Labels Light, VCGI Town Labels, and VCGI City Points, layered for a statewide-to-close-in zoom handoff |
| — | Boundaries | `78853d8236e04a1d8d6df5c0f94e7c13` | Town Boundaries, styled as a two-layer halo (white backing + dotted line + labels) |
| Bottom | Base Topo | `d5173a686f4844fd8584cfecb37ab940` | Terrain, protected lands, recreation features, roads, buildings, the VT mask, the state boundary line, and surrounding-state context boundaries |

[Test 02b](topographic-test-02b-world-terrain-labels/README.md) is the
reference example for this combination — see its layer tables for
exactly what each group currently contains and how it's configured
there.

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
     and iframe `src`). Keep the `<head>` fonts/stylesheet block as-is —
     every page here links the
     [VCGI State of Vermont-themed stylesheet](https://files.vcgi.vermont.gov/other/css/vcgi-sov-stylesheet-v.1.1.css)
     plus its required "Source Sans 3" Google Font, and the inline
     `<style>` block's colors (`#003300` header, `#007834`/`#00417e`
     links) are picked to match that stylesheet's palette rather than
     being ad hoc
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

## Group layers

Operational layers can be organized into groups within a web map (e.g.
Test 02b's "Base Topo," "Boundaries," and "Labels" groups — see
[Reusable Group Layers](#reusable-group-layers) above). Two distinct
things both get called "groups" in ArcGIS Online, with very different
behavior:

- **Ad-hoc groups** — created via **Options → Group** on a layer in Map
  Viewer, then adding more layers into it. These exist only inside that
  one web map's JSON (an `id`/`title` on a `GroupLayer` entry in
  `operationalLayers`, no `itemId` or service URL of its own) and can't
  be referenced from, or added to, another web map.
- **Group layer items** — created from an ad-hoc group via its
  **Options → Save as**. This produces a standalone AGOL item with its
  own item ID, shareable and addable to other web maps from Content, the
  Add Layer browser, etc., without re-building the stacking order by
  hand each time.

**Important limitation, confirmed via Esri's documentation:** saving a
group as a Group layer item does **not** create a live link. Per
[ArcGIS Online Help](https://doc.arcgis.com/en/arcgis-online/create-maps/organize-layers-mv.htm):
> "Group layer property configurations, such as styling, labels, and
> visibility settings, are imported into the web map, and the map is not
> updated as changes are made separately to the group layer item. Only
> updates to the underlying data are reflected across all maps where the
> group layer is used."

So a web map captures a snapshot of the group's styling/structure at the
time the Group layer item is added. Later edits to the item (adding,
removing, reordering, or restyling sublayers) do **not** propagate to
maps that already reference it — there's no documented refresh/sync
action either, only removing and re-adding the group layer item. Only
edits to the underlying feature *data* (not structure/styling) update
live everywhere the group is used.

**Practical implication for this repo:** Group layer items are worth
creating once a group is stable and meant to be handed to others as a
consistent starting point — Test 02b's Base Topo, Boundaries, and Labels
groups are now all saved this way (see
[Reusable Group Layers](#reusable-group-layers) above). While a group is
still actively being revised, editing it as an ad-hoc group directly
inside a test webmap stays simpler than maintaining a Group layer item
that won't reflect those edits anywhere else.

## Web Map Examples

Preconfigured examples for seeing how the basemaps look and function —
not what to build against directly; use
[Reusable Group Layers](#reusable-group-layers) above for that.

### Base Topo configuration example

| Test | Live embed | Notes |
|---|---|---|
| [Topographic — Test 02b (World Terrain Labels)](topographic-test-02b-world-terrain-labels/README.md) | [embed](https://vcgitimterway.github.io/vermont-basemaps/webmap-tests/topographic-test-02b-world-terrain-labels/) | Reference example for the Base Topo + Boundaries + Labels combination above; shared muted "World Terrain Reference Labels Light" style, plus custom VCGI City Points and Town Labels layers |

### Development Web Map Tests

Earlier test iterations — predate the Group Layer composition above,
kept for reference.

| Test | Live embed | Notes |
|---|---|---|
| [Topographic — Test 01 (Styled DEM)](topographic-test-01-styled-dem/README.md) | [embed](https://vcgitimterway.github.io/vermont-basemaps/webmap-tests/topographic-test-01-styled-dem/) | Styled DEM + hillshade terrain, VCGI-sourced water labels, E911 recreation layers |
| [Topographic — Test 01b (World Terrain Labels)](topographic-test-01b-world-terrain-labels/README.md) | [embed](https://vcgitimterway.github.io/vermont-basemaps/webmap-tests/topographic-test-01b-world-terrain-labels/) | Save-as of Test 01; swaps four label layers for one Esri "World Terrain Reference"-styled layer |
| [Topographic — Test 02 (Physical Topo Light)](topographic-test-02-physical-topo-light/README.md) | [embed](https://vcgitimterway.github.io/vermont-basemaps/webmap-tests/topographic-test-02-physical-topo-light/) | Muted hillshade-only terrain (no DEM color ramp), new "Light Roads" and "Buildings White" style variants, intended as a basemap for user-added thematic data |
| [Topographic — Test 02c (Physical Topo Light Admin)](topographic-test-02c-admin/README.md) | [embed](https://vcgitimterway.github.io/vermont-basemaps/webmap-tests/topographic-test-02c-admin/) | Save-as of Test 02b; adds a Town Boundaries layer, a new muted-text label style, and a sample thematic sketch layer demonstrating the basemap's intended use |
