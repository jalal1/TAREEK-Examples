# SPDX-License-Identifier: CC-BY-4.0
"""Make site/county_points.csv: one map point and population per US county.

Run this only to refresh the table (for example after a new census vintage). It
needs geopandas and the county files that the TAREEK web app downloads into
TAREEK's data/counties/ folder:

    python site/make_county_points.py <TAREEK>/data/counties

The point is the county centroid computed in an equal-area CRS (EPSG:5070),
the same as the TAREEK web app, so the pins are in the same places.
"""
import csv
import json
import sys
from pathlib import Path

import geopandas as gpd

counties_dir = Path(sys.argv[1])
gdf = gpd.read_file(counties_dir / "cb_2022_us_county_500k.shp")
population = json.loads((counties_dir / "county_population.json").read_text())
centroids = gdf.to_crs("EPSG:5070").geometry.centroid.to_crs("EPSG:4326")
rows = sorted((g, round(p.y, 4), round(p.x, 4), population.get(g, 0))
              for g, p in zip(gdf["GEOID"], centroids))
out = Path(__file__).with_name("county_points.csv")
with open(out, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(["geoid", "lat", "lng", "population"])
    w.writerows(rows)
print(f"{len(rows)} counties -> {out}")
