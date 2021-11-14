import pandas as pd
import numpy as np
from loadFiles import *
import time

# Loading data from housing prices
codes = ["Est_Mercat_Immobiliari_Lloguer_Mitja_Mensual", "Est_Mercat_Immobiliari_Lloguer_Nombre_Contractes","Est_Mercat_Immobiliari_Lloguer_Superficie_Mitjana"]
#codes = ["Est_Mercat_Immobiliari_Lloguer_Nombre_Contractes"]
data = []
keys = ["Any", "Trimestre","Codi_Districte", "Nom_Districte", "Codi_Barri", "Nom_Barri"]            
#contador = 0
contador_data = 0
variables_lista = []
df_master_new = [0]*len(codes)
for k in codes:
    data = loadFiles([k])
   # print(data)
# print(len(data))
    contador = 0
    for variable in data.columns:
        if variable not in keys:
            variables_lista.append(variable)
        if variable in keys:
            contador += 1
  #  print(contador)
    if contador == len(keys):
       
        for j in data.columns:
            if j not in keys:
                if data[j].dtype == "int64" or data[j].dtype == "float64":
                    print("ESTAMOS READY MI MAMI", k, len(keys))
                    df_master = data.groupby(keys).sum()
        df_master = df_master.reset_index()
    df_master_new[contador_data] = df_master
    contador_data += 1
#print(df_master_new[0])
#print(df_master_new[1])
#print(df_master_new[1])
#print(variables_lista)
   # contador_data += 1

concatenado = pd.concat(df_master_new, join = "inner", axis = 1)
no_keys_df = concatenado.drop(keys, axis = 1) 
concatenado_dup = concatenado.loc[:,keys]
concatenado = concatenado_dup.iloc[:, ~concatenado.columns.duplicated()]

lista = [concatenado, no_keys_df]

concatenado_final = pd.concat(lista, axis = 1)
print(concatenado)
print(concatenado.columns)
print(len(concatenado))

#print(df_master_new[1])
#contador_data += 1

#print(variables_lista)

#time.sleep(59)
#data = loadFiles([codes])
#print(data)
#columnas = data.columns
#keys = ["Any", "Trimestre","Codi_Districte", "Nom_Districte", "Codi_Barri", "Nom_Barri"]
#boolean = False
#contador = 0
#for j in keys:
#    if j in columnas:
#        contador += 1 
#if contador == len(keys):
#    for j in columnas:
#        if j not in keys:
#            if data[j].dtype == "int64" or data[j].dtype == "float64":
#                print(j,"HOLAAAAA")
#                df_master = data.groupby(['Any', 'Trimestre','Codi_Districte', 'Nom_Districte', 'Codi_Barri','Nom_Barri']).sum()
#df_master = df_master.reset_index()


#print(df_master)
