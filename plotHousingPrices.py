import pandas as pd
import folium
import xlrd
import json
import feedparser
import pprint
import requests 
import numpy as np
from loadFiles import *
from folium.plugins import TimeSliderChoropleth
from branca.colormap import linear
import geopandas

def plotBcnData(data, variable = 'Preu', time = 'dt_index', bygroup = 'Barri', legend_name = 'Housing prices', file = 'plot.html'):

	# plot Bcn data by barri or district
	# by = 'Barri'
	# by = 'District'
	

	max_color = max(data[variable])
	min_color = min(data[variable])
	        
	cmap = linear.YlOrRd_04.scale(min_color, max_color)
	data['color'] = data[variable].fillna(0).apply(cmap)
	# nas grey:
	data.loc[np.isnan(data[variable]), 'color'] = 'gray'
	
	styledata = data.groupby(bygroup)[[time,'color','opacity']].apply(lambda x: x.set_index(time).to_dict(orient='index')).to_dict()
	#styledata


	BCNGeo = geopandas.read_file('https://raw.githubusercontent.com/martgnz/bcn-geodata/master/barris/barris.geojson')
	# BCNGeo.head()
	# BCNGeo.plot()
	# BCNGeo['BARRI']
	if bygroup == 'Barri': 
		geo_group = 'BARRI'
		feat = 'feature.properties.BARRI'
	if bygroup == 'Districte': 
		geo_group = 'DISTRICTE'
		feat = 'feature.properties.DISTRICTE'
	BCN_map = folium.Map(location=[41.39, 2.17], zoom_start=12) # in location we must add the city's coordinates
	folium.TileLayer('Stamen Terrain').add_to(BCN_map)
	folium.TileLayer('Stamen Toner').add_to(BCN_map)
	folium.TileLayer('Stamen Water Color').add_to(BCN_map)
	folium.TileLayer('cartodbpositron').add_to(BCN_map)
	folium.TileLayer('cartodbdark_matter').add_to(BCN_map)
	folium.TileLayer('openstreetmap').add_to(BCN_map)
	g = TimeSliderChoropleth(
	    BCNGeo.set_index(geo_group).to_json(),
	    styledict=styledata, 
	    overlay = True).add_to(BCN_map)
	BCN_map.choropleth(
	    geo_data=BCNGeo,
	    data=data,
	    columns=[bygroup, variable],
	    key_on=feat,
	    fill_color= 'YlOrRd',
	    fill_opacity=0.0,
	    line_opacity=0.0,
	    legend_name=legend_name
	)
	folium.LayerControl().add_to(BCN_map)
	BCN_map.save(file)
	BCN_map
