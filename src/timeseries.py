import pandas as pd
import plotly.express as px



def getPriceSeriesPlot():
    """Devuelve la serie temporal de los precios durante los últimos años"""

    df = pd.read_csv('../data/priceseries.csv',sep=',')
    df = df.sort_values('id')
    df2 = pd.DataFrame(df["Precio_m2"])
    df2 = df2.reset_index()
    fig = px.line(df,x="Data",y="Precio_m2")
    fig.add_vline(x="Junio-2021")
    fig.add_vline(x="Mayo-2020")

    return(fig.show())

#df2["date"] =  pd.date_range(start="6/1/2008",end="10/1/2021",freq="MS")
##ADF test(non-stationary serie for arima)
#result = adfuller(df2.Precio_m2.dropna())
#print('ADF Statistic: %f' % result[0])
#print('p-value: %f' % result[1])
#
#from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
#ptest = 0.20
#ptrain = 1 - ptest
#ntrain = int(round(len(df2)*ptrain,0))
#ntest = int(len(df2) - ntrain)
#train = pd.DataFrame(df2[['Precio_m2','date']][:ntrain])
#train = train.set_index('date')
#
#test = df2[['Precio_m2','date']][-ntest:]
#test = test.set_index('date')
#
#plt.plot(train.Precio_m2)
#plt.plot(test.Precio_m2)
#plt.show()
#
#from pmdarima import *
#
#arima_model = auto_arima(train.Precio_m2,start_p=0,d=1,strat_q=0,max_p=5,max_d=5,max_q=5,start_P=0,D=1,start_Q=0,max_P=5,max_D=5,error_action='warn',trace=True,supress_warnings=True,stepwise = True,random_state=20,n_fits=50)
#
#prediction = pd.DataFrame(arima_model.predict(n_periods=ntest),index=test.index)
#prediction.columns = ['predicted_sales']
#plt.figure(figsize=(0,5))
#plt.plot(train.Precio_m2,label="Training")
#plt.plot(test.Precio_m2,label="Test")
#plt.plot(prediction.predicted_sales,label="Prediction")
#plt.show()
#
## Forecast
#n_periods = 24
#fc,confint = arima_model.predict(n_periods=n_periods, return_conf_int=True)
#index_of_fc = np.arange(len(df.Precio_m2), len(df.Precio_m2)+n_periods)
#
## make series for plotting purpose
#fc_series = pd.Series(fc, index=index_of_fc)
#lower_series = pd.Series(confint[:, 0], index=index_of_fc)
#upper_series = pd.Series(confint[:, 1], index=index_of_fc)
#
## Plot
#plt.plot(df.Precio_m2)
#plt.plot(fc_series, color='darkgreen')
#plt.fill_between(lower_series.index, 
#                 lower_series, 
#                 upper_series, 
#                 color='k', alpha=.15)
#
#plt.title("Final Forecast of WWW Usage")
#plt.show()
#
#
#
#from sklearn.metrics import r2_score
#test['predicted_sales'] = prediction
#r2_score(test['Precio_m2'],test['predicted_sales'])
