import pandas as pd
import numpy as np
from loadFiles import *
import time

# Loading data from housing prices
codes = ["Est_Mercat_Immobiliari_Lloguer_Mitja_Mensual", "Est_Mercat_Immobiliari_Lloguer_Nombre_Contractes","Est_Mercat_Immobiliari_Lloguer_Superficie_Mitjana","Est_Mercat_Immobiliari_Compravenda_Preu_Total"]
data = []
keys = ["Any", "Trimestre","Codi_Districte", "Nom_Districte", "Codi_Barri", "Nom_Barri"]            
contador_data = 0
variables_lista = []
df_master_new = [0]*len(codes)

# Recorre los códigos para hacer el scrapping
for k in codes:
    data = loadFiles([k])
    contador = 0
    for variable in data.columns:
        if variable not in keys:
            variables_lista.append(variable)
        if variable in keys:
            contador += 1
    # Si se tienen todas las key, entonces se hace el group by
    if contador == len(keys):
        for j in data.columns:
            if j not in keys:
                if data[j].dtype == "int64" or data[j].dtype == "float64":
                    df_master = data.groupby(keys).min()
        df_master = df_master.reset_index()
    df_master_new[contador_data] = df_master
    contador_data += 1

# Se separan las keys y las variables cuantitativas de las tablas para conseguir una limpia
concatenado = pd.concat(df_master_new, join = "inner", axis = 1)
no_keys_df = concatenado.drop(keys, axis = 1) 
no_keys_df = no_keys_df._get_numeric_data()
concatenado_dup = concatenado.loc[:,keys]
concatenado = concatenado_dup.loc[:, ~concatenado_dup.columns.duplicated()]
lista = [concatenado, no_keys_df]

# Se juntan
concatenado_final = pd.concat(lista, axis = 1)

# Se eliminan duplicadas y se renombra
concatenado_final.rename(columns={'Preu': 'Precio_m2','Valor':'Valor_compra_venta'}, inplace=True)
concatenado_final.loc[:,'Numero_de_contratos'] = concatenado_final.iloc[:,7]


# Se exporta a csv
concatenado_final.to_csv (r'./data.csv', index = False, header=True)


