"""
Proof-of-concept PMTiles build for the Alpine Ski Lifts layer, done
without tippecanoe/Docker (neither available in this environment) —
pure Python using mapbox_vector_tile (MVT encode) + the pmtiles package
(spec-compliant archive writer/converter). Real per-tile clipping and
coordinate quantization, multi-zoom, not a single blob tile.
"""
import gzip
import json
import sqlite3
import os
import urllib.request

import mapbox_vector_tile
from shapely.geometry import shape, box, mapping

SOURCE_URL = (
    "https://services1.arcgis.com/BkFxaEFNwHqX3tAw/arcgis/rest/services/"
    "FS_VCGI_OPENDATA_Emergency_ALPINELIFTS_line_SP_v1/FeatureServer/0/query"
    "?where=1%3D1&outFields=LIFTTYPE,LIFTNAME,RESORTNAME&outSR=102100&f=geojson"
)

ORIGIN_SHIFT = 2 * 3.14159265358979323846 * 6378137 / 2.0

def mercator_tile_bounds(z, x, y):
    n = 2 ** z
    tile_size = (2 * ORIGIN_SHIFT) / n
    minx = -ORIGIN_SHIFT + x * tile_size
    maxx = -ORIGIN_SHIFT + (x + 1) * tile_size
    maxy = ORIGIN_SHIFT - y * tile_size
    miny = ORIGIN_SHIFT - (y + 1) * tile_size
    return (minx, miny, maxx, maxy)

def lonlat_to_tile(lon, lat, z):
    import math
    n = 2 ** z
    x = int((lon + 180.0) / 360.0 * n)
    lat_rad = math.radians(lat)
    y = int((1.0 - math.log(math.tan(lat_rad) + 1 / math.cos(lat_rad)) / math.pi) / 2.0 * n)
    return x, y

with urllib.request.urlopen(SOURCE_URL) as resp:
    gj = json.load(resp)

features = []
for feat in gj['features']:
    geom = shape(feat['geometry'])
    props = {k: v for k, v in feat['properties'].items() if v is not None}
    features.append((geom, props))

minx = min(g.bounds[0] for g, _ in features)
miny = min(g.bounds[1] for g, _ in features)
maxx = max(g.bounds[2] for g, _ in features)
maxy = max(g.bounds[3] for g, _ in features)
print(f"data mercator bounds: {minx:.0f},{miny:.0f},{maxx:.0f},{maxy:.0f}")

ZOOMS = [6, 8, 10, 12]
LAYER_NAME = "alpine_ski_lifts"

tiles = {}  # (z,x,y) -> list of (geom, props)

for z in ZOOMS:
    n = 2 ** z
    tile_size = (2 * ORIGIN_SHIFT) / n
    x0 = int((minx + ORIGIN_SHIFT) / tile_size)
    x1 = int((maxx + ORIGIN_SHIFT) / tile_size)
    y0 = int((ORIGIN_SHIFT - maxy) / tile_size)
    y1 = int((ORIGIN_SHIFT - miny) / tile_size)
    for x in range(x0, x1 + 1):
        for y in range(y0, y1 + 1):
            tb = mercator_tile_bounds(z, x, y)
            buf = (tb[2] - tb[0]) * 0.05
            clip_box = box(tb[0] - buf, tb[1] - buf, tb[2] + buf, tb[3] + buf)
            clipped = []
            for geom, props in features:
                if not geom.intersects(clip_box):
                    continue
                g2 = geom.intersection(clip_box)
                if g2.is_empty:
                    continue
                clipped.append((g2, props, tb))
            if clipped:
                tiles[(z, x, y)] = clipped

print(f"non-empty tiles across zooms {ZOOMS}: {len(tiles)}")

mbtiles_path = "_intermediate.mbtiles"
if os.path.exists(mbtiles_path):
    os.remove(mbtiles_path)
conn = sqlite3.connect(mbtiles_path)
conn.execute("CREATE TABLE metadata (name TEXT, value TEXT)")
conn.execute("CREATE TABLE tiles (zoom_level INTEGER, tile_column INTEGER, tile_row INTEGER, tile_data BLOB)")

minlon, minlat = -73.5, 42.72
maxlon, maxlat = -71.46, 45.02
vector_layers = [{
    "id": LAYER_NAME,
    "fields": {"LIFTTYPE": "String", "LIFTNAME": "String", "RESORTNAME": "String"}
}]
meta = {
    "name": "alpine-ski-lifts-poc",
    "format": "pbf",
    "minzoom": str(min(ZOOMS)),
    "maxzoom": str(max(ZOOMS)),
    "bounds": f"{minlon},{minlat},{maxlon},{maxlat}",
    "center": f"{(minlon+maxlon)/2},{(minlat+maxlat)/2},{ZOOMS[len(ZOOMS)//2]}",
    "type": "overlay",
    "json": json.dumps({"vector_layers": vector_layers}),
}
for k, v in meta.items():
    conn.execute("INSERT INTO metadata (name, value) VALUES (?,?)", (k, v))

tile_count = 0
for (z, x, y), feats in tiles.items():
    tb = mercator_tile_bounds(z, x, y)
    layer_features = []
    for geom, props, _ in feats:
        layer_features.append({"geometry": mapping(geom), "properties": props})
    mvt = mapbox_vector_tile.encode(
        [{"name": LAYER_NAME, "features": layer_features}],
        default_options={"quantize_bounds": (tb[0], tb[1], tb[2], tb[3]), "extents": 4096},
    )
    gz = gzip.compress(mvt)
    tms_row = (2 ** z - 1) - y
    conn.execute(
        "INSERT INTO tiles (zoom_level, tile_column, tile_row, tile_data) VALUES (?,?,?,?)",
        (z, x, tms_row, sqlite3.Binary(gz)),
    )
    tile_count += 1

conn.commit()
conn.close()
print(f"wrote {tile_count} tiles to {mbtiles_path}")

from pmtiles.convert import mbtiles_to_pmtiles
pmtiles_path = "alpine-ski-lifts-poc.pmtiles"
mbtiles_to_pmtiles(mbtiles_path, pmtiles_path, max(ZOOMS))
os.remove(mbtiles_path)
print(f"wrote {pmtiles_path}, size={os.path.getsize(pmtiles_path)} bytes")
