import pandas as pd
import plotly.express as px

df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/flights.csv', sep=',')




grafico = px.line(data_frame=df, x=df['month'], y=df['passengers'], color=df["year"])

grafico.show()



input()