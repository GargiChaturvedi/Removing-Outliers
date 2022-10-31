import pandas
import statistics
import plotly.express as px

df = pandas.read_csv('savings_data_final.csv')
fig = px.scatter(df, x='female', y='quant_saved', color='rem_any')
fig.show()