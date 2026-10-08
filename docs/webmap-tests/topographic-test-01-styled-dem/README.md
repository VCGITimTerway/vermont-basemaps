# Topographic — Test 01 (Styled DEM)

**Live embed:** https://vcgitimterway.github.io/vermont-basemaps/webmap-tests/topographic-test-01-styled-dem/
**ArcGIS Online item:** https://vcgi.maps.arcgis.com/apps/mapviewer/index.html?webmap=c6a5d16848b84f02a67a2e73be6958f9

## Status

**Embed will not render for outside viewers yet.** The item's sharing
level is currently not set to "Everyone (public)" — as of this writing,
the AGOL sharing REST API returns 403 for anonymous requests to this item
ID. Having a "Share" link (even the short `arcg.is` one) is not the same
as the item being publicly shared; that's a separate setting on the item
itself (Content → item → **Share** → set to **Everyone**), and the
item's **"Allow others to embed this map"** option (item Settings) also
needs to be on. Until both are set, this page's iframe will show a
sign-in wall instead of the map, both here and for anyone else visiting
the link.

## Layers shown & design decisions

*Not yet documented* — the item isn't publicly accessible yet, so this
couldn't be pulled from the actual web map JSON (the sharing REST API's
`/data` endpoint, which returns the full operational-layer list, also
403s until sharing is public). Once it's set to public, say so and this
can be filled in automatically from the real web map definition rather
than guessed at.

Working assumption based on recent work in this repo (confirm/correct
when filling this in): this is likely testing the
[11-class, feet-aligned color ramp](../../dem-color-ramps/11class-feet-aligned/README.md)
applied to the [Bare Earth DEM](../../data-sources/dem-bare-earth.md) via
TiTiler, per the [titiler-colormap.min.json](../../dem-color-ramps/11class-feet-aligned/titiler-colormap.min.json)
work and the ArcGIS Online rendering fix from that session.

## Related

- [`../README.md`](../README.md) — index of all webmap tests
- [`../../dem-color-ramps/11class-feet-aligned/README.md`](../../dem-color-ramps/11class-feet-aligned/README.md)
