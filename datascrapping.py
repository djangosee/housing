import pandas as pd
import numpy as np
from loadFiles import *
import time

# Loading data from housing prices
codes = ["Est_Mercat_Immobiliari_Lloguer_Mitja_Mensual", "Est_Mercat_Immobiliari_Lloguer_Nombre_Contractes","Est_Mercat_Immobiliari_Lloguer_Superficie_Mitjana","Est_Mercat_Immobiliari_Compravenda_Preu_Total"]
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
                    df_master = data.groupby(keys).min()
        df_master = df_master.reset_index()
    df_master_new[contador_data] = df_master
    contador_data += 1

concatenado = pd.concat(df_master_new, join = "inner", axis = 1)
no_keys_df = concatenado.drop(keys, axis = 1) 
no_keys_df = no_keys_df._get_numeric_data()
concatenado_dup = concatenado.loc[:,keys]

print("DUPLICADOS:", concatenado_dup.columns.duplicated())


concatenado = concatenado_dup.loc[:, ~concatenado_dup.columns.duplicated()]


#print("Concatenado duplicado", concatenado_dup)
#print("No keys", no_keys_df)
#print("Concatenado", concatenado)


lista = [concatenado, no_keys_df]

concatenado_final = pd.concat(lista, axis = 1)

concatenado_final.rename(columns={'Preu': 'Precio_m2','Valor':'Valor_compra_venta'}, inplace=True)
#concatenado_final[["Num_contratos_alquiler"]] = concatenado_final[["Nombre"]]
#concatenado_final.drop(concatenado_final.columns[[5]], axis='columns', inplace = True)

print(concatenado_final.iloc[:,7])


#concatenado_final[["Numero_de_contratos"]] = concatenado_final.iloc[:,7]
concatenado_final.loc[:,'Numero_de_contratos'] = concatenado_final.iloc[:,7]
#concatenado_final.drop(concatenado_final.columns[[7]],axis='columns', inplace =True)


print(concatenado_final)

print(concatenado_final.describe())


concatenado_final.to_csv (r'./data.csv', index = False, header=True)

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
