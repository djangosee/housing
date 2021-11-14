# Housing Challenge
El reto consiste en analizar la situación actual (y a futuro) de los precios del alquiler en Barcelona. Posibles migraciones poblacionales y qué perfil de individuo podrá permitirse un alquiler en barcelona.

# Objetivos
 - Estadística descriptiva sobre el precio del alquiler en Barcelona.
 - Clustering de barrios.
 - Forecasting del precio del alquiler en los próximos años.

# Datos
Los datos se han obtenido a través de la API de [OpenDataBCN](https://opendata-ajuntament.barcelona.cat/dataset), la documentación de estos la encontramos [aquí](https://github.com/djangosee/housing/blob/main/docu/variables.md).

## Housing.py

El script principal tiene dos funcionalidades. 

### Mapa de Barcelona mediante el paquete folium

La primera funcionalidad consiste en la creación de un mapa interactivo usando los datos de los precios del alquiler en los barrios o distritos.

```
python3.7 housing.py -m 
```
El output que genera lo encontramos en el siguiente <a id="raw-url" href="https://raw.githubusercontent.com/djangosee/housing/main/fig/plot_HousingPrices.html">html</a>.

![Mapa distritos de barcelona y el precio medio del alquiler durante los años](https://github.com/djangosee/housing/blob/main/fig/map.png)


La idea a futuro sería la posibilidad de introducir el código del dataset y la variable númerica:

```
python3.7 housing.py -m "Est_Mercat_Immobiliari_Lloguer_Mitja_Mensual" Preu
```
### Decarga de datasets automática de OpenDataBcn (One code)
La funcionalidad unifica todos los datasets existentes en OpenDataBcn para un código (de todos los años) en un solo dataset y los guarda en un csv:

```
python3.7 housing.py -d "Est_Mercat_Immobiliari_Lloguer_Mitja_Mensual" 
```

### Decarga de datasets automática de OpenDataBcn (Múltiple code)
Mediante el script loadFiles.py se leen los ficheros csv de [OpenDataBCN](https://opendata-ajuntament.barcelona.cat/dataset) pasándole como parámetro a la función únicamente la url sin el año. Ya que se consigue que se descarguen y concatenen todos los ficheros con el mismo código, independientemente del año. 

El script datascrapping.py consigue agrupar las todas las tablas de las url de alquiler mensual, número de contratos de alquiler, superficie media de las viviendas y precio de la compraventa agrupadas por año, trimestre, código de distrito, nombre de distrito, código de barrio y nombre de barrio.

El output es la tabla data.csv con estas claves y las variables cuantitativas anteriores.

```
python3.7 housing.py -s
```
