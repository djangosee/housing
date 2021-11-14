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
El output que genera lo encontramos en el siguiente [html]().

La idea a futuro sería la posibilidad de introducir el código del dataset y la variable númerica:

```
python3.7 housing.py -m "Est_Mercat_Immobiliari_Lloguer_Mitja_Mensual" Preu
```

### Decarga de datasets automática de OpenDataBcn
