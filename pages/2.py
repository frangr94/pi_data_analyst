import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import folium
from streamlit_folium import st_folium

provinciales = pd.read_csv('datos_ordenados/provinciales.csv')

acceso_provincias = provinciales[(provinciales.año==2022) & (provinciales.trimestre==3)]

salarios = pd.read_csv('datos_ordenados/salarios_provincias.csv')

st.set_page_config(page_title='Estrategía de inversion internet',
                   page_icon=":bar_chart:",
                   layout='wide',
                   initial_sidebar_state='collapsed'
                   )

st.markdown(f"<h3 style='text-align: center; color: white;'>Servicio de internet por provincias </h3>", unsafe_allow_html=True)

# ---SECCION KPI ---
left,right = st.columns(2)
with left:
    acceso_promedio = acceso_provincias['accesos_100_hogares'].mean()
    st.markdown(f"<h5 style='text-align: center; color: white;'>Promedio accesos a internet nacional: </h5>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: center; color: white;'>{round(acceso_promedio,1)} </h5>", unsafe_allow_html=True)
with right:
    salario_promedio = salarios['promedio_salario'].mean()
    st.markdown(f"<h5 style='text-align: center; color: white;'>Salario promedio nacional: </h5>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: center; color: white;'>{round(salario_promedio,1)} </h5>", unsafe_allow_html=True)

st.markdown('---')

# ---SECCION MAPAS---
left,right = st.columns(2)
with left:
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
        fill_opacity=1,

    )
    choropleth.geojson.add_to(map)

    acceso_provincias.set_index('provincia',inplace=True)

    for feature in choropleth.geojson.data['features']:
        provincia=feature['properties']['name']
        feature['properties']['acceso_100']='acceso_100_hogares: '+str([acceso_provincias['accesos_100_hogares'][provincia]][0])


    choropleth.geojson.add_child(
        folium.features.GeoJsonTooltip(['name','acceso_100'],labels=False)
    )

    st_map = st_folium(map,height=700,width=700)
with right:
    # mapa ingresos promedio por provincia
    st.write('''Salarios promedio por provincia (año 2022). Fuente: INDEC''')

    map=folium.Map(location=[-34,-64],zoom_start=4.4,scrollWheelZoom=False,tiles='CartoDB positron')

    choropleth = folium.Choropleth(
        geo_data='datasets/argentina_regions.geojson',
        data=salarios,
        columns=('provincia','promedio_salario'),
        key_on='feature.properties.name',
        line_opacity=1,
        highlight=True,
        fill_color='YlOrBr',
        fill_opacity=1

    )
    choropleth.geojson.add_to(map)

    salarios.set_index('provincia',inplace=True)

    for feature in choropleth.geojson.data['features']:
        provincia=feature['properties']['name']
        feature['properties']['promedio_salario']='promedio_salario: '+str([salarios['promedio_salario'][provincia]][0])


    choropleth.geojson.add_child(
        folium.features.GeoJsonTooltip(['name','promedio_salario'],labels=False)
    )

    st_map = st_folium(map,height=700,width=700)


