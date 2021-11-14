import pandas as pd
import plotly.express as px

df = pd.read_csv('../data/priceseries.csv',sep=',')
df = df.sort_values('id')
fig = px.line(df,x="Data",y="Precio_m2")
fig.add_vline(x="Junio-2021")
fig.add_vline(x="Mayo-2020")
fig.show()
