# Tratamiento de datos
# ==============================================================================
import numpy as np
import pandas as pd
from sklearn.datasets import make_blobs
import seaborn as sns
import time

# Gráficos
# ==============================================================================
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot') or plt.style.use('ggplot')

# Preprocesado y modelado
# ==============================================================================
from sklearn.cluster import KMeans
from sklearn.preprocessing import scale
from sklearn.metrics import silhouette_score
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram
from sklearn.preprocessing import scale
from sklearn.metrics import silhouette_score
from scipy import stats


####==============================================================================


df = pd.read_csv(r'./data.csv', delimiter = ",", index_col = ["Any", "Trimestre", "Codi_Districte", "Nom_Districte", "Codi_Barri", "Nom_Barri"])
#print(df.head(5))
df.fillna(df.mean(), inplace = True)


#print("Jugadores con más partidas: ", df.nlargest(10,"NumGames"))

df_new_stand = df
for i in df.columns.values:
    mu = df[i].mean()
    sigma = df[i].std()
    df_new_stand[i] = (df[i]-mu)/sigma







# Método silhouette para identificar el número óptimo de clusters
# ==============================================================================
range_n_clusters = range(2, 20)
valores_medios_silhouette = []

for n_clusters in range_n_clusters:
    modelo_kmeans = KMeans(
                        n_clusters   = n_clusters, 
                        n_init       = 20, 
                        random_state = 123
                    )
    cluster_labels = modelo_kmeans.fit_predict(df_new_stand)
    silhouette_avg = silhouette_score(df_new_stand, cluster_labels)
    valores_medios_silhouette.append(silhouette_avg)
    print("Número de clusters: ", n_clusters, " silhouette medio:  ",silhouette_avg)
    
fig, ax = plt.subplots(1, 1, figsize=(6, 3.84))
ax.plot(range_n_clusters, valores_medios_silhouette, marker='o')
ax.set_title("Evolución de media de los índices silhouette")
ax.set_xlabel('Número clusters')
ax.set_ylabel('Media índices silhouette')
plt.show()
#Según el método de Silhouette se obtiene el número óptimo de clústers en n=2



#IMPLEMENTAR KMEANS CON K=2 AÑADIR ETIQUETA AL DATAFRAME Y ANALIZAR CADA CLUSTER POR SEPARADO
# Modelo
# ==============================================================================

#Matriz de correlación
plt.figure(figsize=(18,18))
correlation_mat = df_new_stand.corr()
xticks = df_new_stand.columns
sns.heatmap(correlation_mat, annot = True, xticklabels = xticks )
plt.xticks(rotation = 90)
plt.show()

#Modelo kmeans
modelo_kmeans = KMeans(n_clusters=2, n_init=25, random_state=123)
modelo_kmeans.fit(X=df_new_stand)



# Clasificación con el modelo kmeans
# ==============================================================================
y_predict = modelo_kmeans.predict(X=df_new_stand)

## Se añade la columna de etiquetas al data set
df_cl = df_new_stand
df_cl["predicted"] = y_predict

# Se crean los dataframes de cada cluster por separado
zeroo = df_cl[df_cl["predicted"] == 0]
oness = df_cl[df_cl["predicted"] == 1]

# Imprime los id de los jugadores del cluster 1 (comentar si no interesa)
#indices = oness.index.to_list()
#contador = 0
#for index in indices:
#    contador += 1
#    print(contador, int(index))

## Número de jugadores en cada cluster

print(" Jugadores en cluseter 0: ", len(zeroo))
print("Jugadores en cluster 1: ", len(oness))



## En qué se diferencian (apuesta, dinero inicial, gastado en extra, numero de bolas extra compradas, tiempo jugando...)
## =======================================================================================================================================
#histograma de las variables para cada cluster

df_cl = df
df_cl["predicted"] = y_predict
df_cl_stand = df_new_stand
df_cl_stand["predicted"] = y_predict

### Imprime histogramas conjuntos de cada variable para cada cluster
### Calcula el contraste de hipótesis de igualdad de medias
### Dibuja la distribución de cada variable para cada cluster en un boxplot
for i in df_cl.columns.values:
    print('Test de igualdad de medias para la variable ', i, stats.ttest_ind(df_cl_stand[i][df_cl_stand['predicted'] == 0], df_cl_stand[i][df_cl_stand['predicted'] == 1]))
    #Histogramas (un poco inútiles, si se quiere, comentar)
    plt.figure()
    plt.hist(zeroo[i],
         alpha = 0.3,
         label = "0")
    plt.hist(oness[i],
         alpha = 0.3,
         label = "1")
    plt.xlabel(i, size=14)
    plt.ylabel("Count", size=14)
    plt.title(i + " by cluster")
    plt.legend(loc='upper right')
    plt.show()
     
    ## Boxplot 
    fig = plt.figure(figsize= (10, 10))
    ax = fig.add_subplot(111)
    ax.set_title("Box Plot of " +i+ " by cluster", fontsize= 20)
    ax.set
    data = [df_cl[i][df_cl['predicted'] == 0],
               df_cl[i][df_cl['predicted'] == 1]]
    ax.boxplot(data,
           labels= ['0', '1'],
           showmeans= True)
    plt.xlabel("Cluster")
    plt.ylabel( i + " Score")
    plt.show()


