import feedparser
import pprint
import requests
import pandas as pd
import numpy as np


def loadFiles( codes ):
    """Devuelve una lista de dataframes para cada codigo"""
    codes = ['Est_Mercat_Immobiliari_Lloguer_Mitja_Mensual']
    parameters = {'rows': '1000'}
    url = 'http://opendata-ajuntament.barcelona.cat/data/api/3/action/package_search'
    response = requests.get(url,params=parameters)
    catalogo = pd.DataFrame(response.json()['result']['results'])

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

    data = []
    for i in range(len(codes)):
        datasets_info = fuente_datos[fuente_datos['code'] == codes[i]]
        tables = []
        for j in range(len(datasets_info)):
            tables.append(pd.read_csv(datasets_info['url'][j]))
        data.append(pd.concat(tables))

    return(data)
