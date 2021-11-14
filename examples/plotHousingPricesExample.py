from loadFiles import *
from plotHousingPrices import *
import webbrowser

def openMapExample():
    # Loading data from housing prices
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
    plotBcnData(data, variable = 'Preu', time = 'dt_index', bygroup = 'Barri', file = 'plot_HousingPrices.html')
    webbrowser.open("plot_HousingPrices.html")
