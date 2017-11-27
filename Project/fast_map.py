#!/usr/bin/env python3

import numpy as np
import pandas as pd
import geopandas as gpd
import pickle
from tqdm import tqdm
import wikipedia
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import shapely.wkt


import folium
from folium.plugins import MarkerCluster, FastMarkerCluster
from folium import IFrame

with open('conflict.pickle', 'rb') as data_source:
        conflict_df = pickle.load(data_source)

with open('refugee.pickle', 'rb') as data_source:
        refugee_df = pickle.load(data_source)

geometry = conflict_df['geom_wkt'].map(shapely.wkt.loads)
conflict_df = conflict_df.drop('geom_wkt', axis=1)
crs = {'init': 'epsg:4326'}
gdf = gpd.GeoDataFrame(conflict_df, crs=crs, geometry=geometry)

table = """
<!DOCTYPE html>
<html>
<head>
<style>
table {{
    width:100%;
}}
table, th, td {{
    border: 1px solid black;
    border-collapse: collapse;
}}
th, td {{
    padding: 5px;
    text-align: left;
}}
table#t01 tr:nth-child(odd) {{
    background-color: #eee;
}}
table#t01 tr:nth-child(even) {{
   background-color:#fff;
}}
</style>
</head>
<body>

<table id="t01">
  <tr>
    <td>Type</td>
    <td>{}</td>
  </tr>
  <tr>
    <td>Name</td>
    <td>{}</td>
  </tr>
  <tr>
    <td>Nbr</td>
    <td>{}</td>
  </tr>
</table>
</body>
</html>
""".format


m = folium.Map(tiles='cartodbpositron')

print("Rows to parse:{}".format(len(gdf)))

width, height = 310,110
popups, locations = [], []
for idx, row in tqdm(gdf.iterrows()):
    locations.append([row['geometry'].y, row['geometry'].x])
    name = row['conflict_name'].encode('ascii', 'xmlcharrefreplace')
    deaths = row['best']
    iframe = folium.IFrame(table('Deaths', name, deaths), width=width, height=height)
    popups.append(iframe)


h = folium.FeatureGroup(name='Deaths')
h.add_child(FastMarkerCluster(locations))
m.add_child(h)

m.save("output_map.html")
