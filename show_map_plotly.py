import pandas as pd
import plotly.express as px
import os

file_path = './Desktop/GNSS_data/fotballbane/RawData.csv'

if not os.path.exists(file_path):
    raise FileNotFoundError(f"File not found at {file_path}")

df_orig = pd.read_csv(file_path)

lat_ext_dd = df_orig["Latitude"].values
lon_ext_dd = df_orig["Longitude"].values

df = pd.DataFrame({'lat': lat_ext_dd, 'lon': lon_ext_dd})


fig = px.scatter_mapbox(df,
                        lat='lat',
                        lon='lon',
                        center={'lat': df['lat'].mean(),
                                'lon': df['lon'].mean()},
                        zoom=15)

fig.update_layout(mapbox_style='open-street-map')

fig.show()
