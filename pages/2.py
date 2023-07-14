import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import folium
from streamlit_folium import st_folium

provinciales = pd.read_csv('datos_ordenados/provinciales.csv')

acceso_provincias = provinciales[(provinciales.año==2022) & (provinciales.trimestre==3)]

st.set_page_config(page_title='Estrategía de inversion internet',
                   page_icon=":bar_chart:",
                   layout='wide',
                   initial_sidebar_state='collapsed'
                   )

st.write('''### Servicio de internet por provincias''')

# mapa acceso a internet por provincia
st.write('''Accesos a internet cada 100 hogares (tercer trimestre 2022). Fuente: ENACOM''')
map=folium.Map(location=[-34,-64],zoom_start=4.4,scrollWheelZoom=False,tiles='CartoDB positron')

choropleth = folium.Choropleth(
    geo_data='datasets/argentina_regions.geojson',
    data=acceso_provincias,
    columns=('provincia','accesos_100_hogares'),
    key_on='feature.properties.name',
    line_opacity=1,
    highlight=True,

)
choropleth.geojson.add_to(map)

acceso_provincias.set_index('provincia',inplace=True)

for feature in choropleth.geojson.data['features']:
    provincia=feature['properties']['name']
    feature['properties']['acceso_100']='acceso_100_hogares: '+str([acceso_provincias['accesos_100_hogares'][provincia]][0])

    

choropleth.geojson.add_child(
    folium.features.GeoJsonTooltip(['name','acceso_100'],labels=False)
)



st_map = st_folium(map)


