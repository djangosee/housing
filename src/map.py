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
# First let's call the libraries we are going to use
# Loading data from housing prices
data = loadFiles(['Est_Mercat_Immobiliari_Lloguer_Mitja_Mensual'])
data = data[0]

# variables interesantes:
data.describe()

data['Lloguer_mitja'].value_counts()
# Lloguer mitjà per superfície (Euros/m2 mes)    2190
# Lloguer mitjà mensual (Euros/mes)              2190

data_crosstab = pd.crosstab(data['Lloguer_mitja'],
                            data['Any'],margins = False)

# select only Lloguer mitjà mensual (Euros/mes)  (for now)
data = data[data['Lloguer_mitja'] == 'Lloguer mitjà per superfície (Euros/m2 mes)']

# start by one year (e.g. 2021)
data2021 = data[(data['Any'] == 2019)]
