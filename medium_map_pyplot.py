# import packages
import pandas as pd
import plotly.express as px
import numpy as np
# get data
url = 'https://raw.githubusercontent.com/kefeimo/DataScienceBlog/master/2.geo_plot/df_mapbox_demo.csv'
df_plot_tmp = pd.read_csv(url)
df_plot_tmp.head()
# two-line code
fig = px.scatter_mapbox(df_plot_tmp, lat="latitude", lon="longitude", color="gender", zoom=3, mapbox_style='open-street-map')
fig.show()