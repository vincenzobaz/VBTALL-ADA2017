#!/usr/bin/env python3
import os

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
from folium.plugins import MarkerCluster, FastMarkerCluster, HeatMapWithTime
from folium import IFrame

with open(os.path.join('pickle', 'conflict.pickle'), 'rb') as data_source:
        conflict_df = pickle.load(data_source)

with open(os.path.join('pickle', 'refugee.pickle'), 'rb') as data_source:
        refugee_df = pickle.load(data_source)

conflict_df.date_start = pd.to_numeric(conflict_df.date_start)
conflict_df = conflict_df.sort_values("date_start")

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


m = folium.Map(tiles='cartodbpositron', world_copy_jump = True, no_wrap=True)

print("Rows to parse:{}".format(len(gdf)))

width, height = 310,110
empty_year_array = [[] for year in conflict_df.date_start.unique()]
popups, locations = empty_year_array, empty_year_array
for idx, row in tqdm(gdf.iterrows()):
    year = row['year'] - 1989
    locations[year].append([row['geometry'].y, row['geometry'].x])
    name = row['conflict_name'].encode('ascii', 'xmlcharrefreplace')
    deaths = row['best']
    time = row['date_start']
    iframe = folium.IFrame(table('Deaths', name, deaths, time), width=width, height=height)
    popups[year].append(iframe)


h = folium.FeatureGroup(name='Deaths')
print(len(locations))
print(len(popups))
#for year in tqdm(conflict_df.date_start.unique()-1989):
#
#    mc = MarkerCluster(locations=locations[year], popups=popups[year], overlay=True, control=True)
#    mc.add_to(m)
#folium.LayerControl().add_to(m)

h.add_child(FastMarkerCluster(locations))
#m.add_child(h)
m.save(os.path.join('results', "output_map.html"))

m = folium.Map(tiles='cartodbpositron', world_copy_jump = True, no_wrap=True)

event_list = conflict_df[["latitude", "longitude", "best", "date_start"]]
list_of_event= [[row.latitude, row.longitude, row.best] for row in event_list.itertuples()]
date_list = [row.date_start for row in event_list.itertuples()]
hm = HeatMapWithTime(data=list_of_event[:100], index=event_list.date_start[:100], max_opacity=0.3)
hm.add_to(m)
m.save(os.path.join('results', "output_map_heat.html"))
