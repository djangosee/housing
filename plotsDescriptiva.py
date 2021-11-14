from loadFiles import *
from plotHousingPrices import *

##################################
# Housing prices by barri and year
data = loadFiles(['Est_Mercat_Immobiliari_Lloguer_Mitja_Mensual'])

data['Lloguer_mitja'].value_counts()
# Lloguer mitjà per superfície (Euros/m2 mes)    2190
# Lloguer mitjà mensual (Euros/mes)              2190

# select only Lloguer mitjà mensual (Euros/mes)  (for now)
data = data[data['Lloguer_mitja'] == 'Lloguer mitjà mensual (Euros/mes)']

# new variables:
data['Month'] = data['Trimestre']*3
data['formattedDate'] = data.Any.apply(str) + data.Month.apply(str).str.zfill(2) + '01'
data['date'] = pd.to_datetime(data['formattedDate'], format='%Y%m%d', yearfirst=True)
data['dt_index']=(data['date'].astype(int)// 10**9).astype('U10')
data['opacity'] = 0.8
#data['Preu'] = data['Preu'].fillna(0)
#plt.hist(x=data['Preu'])
data['Barri'] =  data.Codi_Barri.apply(str)
data['Barri'] = data['Barri'].str.zfill(2)

plotBcnData(data, variable = 'Preu', time = 'dt_index', bygroup = 'Barri', legend_name = 'Housing prices in BCN', file = 'fig/plot_HousingPrices.html')

##################################
# Housing prices/m2 by barri and year:

data = loadFiles(['Est_Mercat_Immobiliari_Lloguer_Mitja_Mensual'])
data = data[data['Lloguer_mitja'] == 'Lloguer mitjà per superfície (Euros/m2 mes)']

# new variables:
data['Month'] = data['Trimestre']*3
data['formattedDate'] = data.Any.apply(str) + data.Month.apply(str).str.zfill(2) + '01'
data['date'] = pd.to_datetime(data['formattedDate'], format='%Y%m%d', yearfirst=True)
data['dt_index']=(data['date'].astype(int)// 10**9).astype('U10')
data['opacity'] = 0.8
#data['Preu'] = data['Preu'].fillna(0)
#plt.hist(x=data['Preu'])
data['Barri'] =  data.Codi_Barri.apply(str)
data['Barri'] = data['Barri'].str.zfill(2)

plotBcnData(data, variable = 'Preu', time = 'dt_index', bygroup = 'Barri', legend_name = 'Housing prices in BCN', file = 'fig/plot_HousingPricesm2.html')

##################################
# Distribució territorial de la renda familiar a la ciutat de Barcelona

data = loadFiles(['Est_Renda_Familiar'])
data.columns
# Index(['Any', 'Codi_Districte', 'Nom_Districte', 'Codi_Barri', 'Nom_Barri',
#        'Població', 'Índex RFD Barcelona = 100'],
#       dtype='object')

# new variables:
data['Index'] = data['Índex RFD Barcelona = 100']
data['Index'].value_counts()
# replace value '-' by nan
data['Index'] = data['Index'].replace('-', np.nan)
data['Index'] = pd.to_numeric(data['Index'])

data['formattedDate'] = data.Any.apply(str) + '0101'
data['date'] = pd.to_datetime(data['formattedDate'], format='%Y%m%d', yearfirst=True)
data['dt_index']=(data['date'].astype(int)// 10**9).astype('U10')
data['opacity'] = 0.8
#data['Preu'] = data['Preu'].fillna(0)
#plt.hist(x=data['Preu'])
data['Barri'] =  data.Codi_Barri.apply(str)
data['Barri'] = data['Barri'].str.zfill(2)

plotBcnData(data, variable = 'Index', time = 'dt_index', bygroup = 'Barri', legend_name = 'Renda familiar in BCN', file = 'fig/plot_RendaFamiliar.html')

