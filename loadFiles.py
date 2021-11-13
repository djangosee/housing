import feedparser
import pprint
import requests 
import pandas as pd
import numpy as np


# Listado de data sets disponible en opendata   
parameters = {'rows': '1000'}

url = 'http://opendata-ajuntament.barcelona.cat/data/api/3/action/package_search'
response = requests.get(url,params=parameters)
# Incluimos a tabla pandas Data sets contienen diferentes fuentes de datos columna resources
catalogo = pd.DataFrame(response.json()['result']['results']) 

# Creamos tabla con las fuentes de datos del catalogo

i = 0
for index, row in catalogo.iterrows():
    if i== 0:
        fuente_datos = pd.DataFrame(row['resources']) 
        fuente_datos['code'] = row['code']   
    i = 1
    aux =  pd.DataFrame(row['resources'])
    aux['code'] = row['code']
    fuente_datos = fuente_datos.append(aux)
fuente_datos = fuente_datos[['code','size', 'description', 'format' , 'downloads_absolute', 'token_required', 'url',  'name']]

catalogo[['code', 'title', 'frequency', 'fuente', 'relationships_as_object']]

fuente_datos[fuente_datos.code == 'ITINERARIS' ]

fuente_datos


# BBD codes to download:
codes = ['Est_Mercat_Immobiliari_Lloguer_Mitja_Mensual']

# BBDD:
data = []
for i in 1:len(codes):
	datasets_info = fuente_datos[fuente_datos['code'] == codes[i]]
	tables = []
	for j in range(len(datasets_info)):
		tables.append(pd.read_csv(datasets_info['url'][j]))

	data[i] = pd.concat(tables)

# data contains a list of dataframes, whose codes are listed in 'codes'
