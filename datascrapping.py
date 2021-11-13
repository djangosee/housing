import pandas as pd
import numpy as np
from loadFiles import *
import time

# Loading data from housing prices
codes = ["Est_Mercat_Immobiliari_Lloguer_Mitja_Mensual", "Est_Mercat_Immobiliari_Lloguer_Nombre_Contractes"]
data = []
contador_data = 0
#for k in codes:
   # data[contador_data] = loadFiles(k)
    #contador_data += 1
data = loadFiles([codes[1]])
print(data)
columnas = data.columns
keys = ["Any", "Trimestre","Codi_Districte", "Nom_Districte", "Codi_Barri", "Nom_Barri"]
#boolean = False
contador = 0
for j in keys:
    if j in columnas:
        contador += 1 
if contador == len(keys):
    for j in columnas:
        if j not in keys:
            if data[j].dtype == "int64" or data[j].dtype == "float64":
                print(j,"HOLAAAAA")
                df_master = data.groupby(['Any', 'Trimestre','Codi_Districte', 'Nom_Districte', 'Codi_Barri','Nom_Barri']).sum()
df_master = df_master.reset_index()
#for j in codes:
#    data = loadFiles(j)
#    df.concat(data)
print(df_master)
