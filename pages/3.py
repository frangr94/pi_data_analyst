import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import folium
from streamlit_folium import st_folium
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title='Estadísticas nacionales',
                   page_icon=":bar_chart:",
                   layout='wide',
                   initial_sidebar_state='collapsed'
                   )

locales = pd.read_csv('datos_ordenados/locales.csv')

#locales = locales.loc[(locales['provincia'] == 'Mendoza')| (locales['provincia'] == 'Santa Cruz') ]

locales = locales.sort_values(by='poblacion',ascending=False)

locales=locales.rename(columns={'latitud':'latitude','longitud':'longitude'})

locales.loc[(locales['fibra_opt']=='NO') | (locales['4g']=='NO'),'conexion_lenta' ] = 'SI'
locales.loc[(locales['fibra_opt']=='SI') | (locales['4g']=='SI'),'conexion_lenta' ] = 'NO'
conexiones_lentas = locales[(locales['conexion_lenta']=='SI') & (locales['poblacion']>1000)]

st.markdown(f"<h3 style='text-align: center; color: white;'>Localidades con conexiones lentas (más de mil habitantes) </h3>", unsafe_allow_html=True)

map_con = conexiones_lentas[['latitude','longitude']]

left, right = st.columns(2)
with left:
    # scatter map
    st.map(data=map_con)
with right:
    poblacion = pd.read_csv('datos_ordenados/poblacion_provincias.csv')
    agrupado = poblacion.groupby(by='region').sum()
    agrupado.drop(columns='provincia',inplace=True)
    agrupado.reset_index(inplace=True)

    fig, ax = plt.subplots()
    ax.pie(agrupado.poblacion,labels=agrupado.region)
    ax.axis('equal')
    st.pyplot(fig)


 # cuadro
st.write(conexiones_lentas)