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
poblaciones = pd.read_csv('datos_ordenados/poblacion_provincias.csv')

locales = locales.sort_values(by='poblacion',ascending=False)

locales=locales.rename(columns={'latitud':'latitude','longitud':'longitude'})

locales.loc[(locales['fibra_opt']=='NO') | (locales['4g']=='NO'),'conexion_lenta' ] = 'SI'
locales.loc[(locales['fibra_opt']=='SI') | (locales['4g']=='SI'),'conexion_lenta' ] = 'NO'

locales['provincia']=locales['provincia'].astype(str)
poblaciones['provincia']=poblaciones['provincia'].astype(str)
locales=locales.merge(poblaciones,on='provincia',how='left')
locales.drop(columns='poblacion_y',inplace=True)
conexiones_lentas = locales[(locales['conexion_lenta']=='SI') & (locales['poblacion_x']>1000)]

#st.markdown(f"<h3 style='text-align: center; color: white;'>Localidades con conexiones lentas (más de mil habitantes) </h3>", unsafe_allow_html=True)
st.header('Localidades con conexiones lentas (más de mil habitantes)')
st.markdown('---')

poblacion = pd.read_csv('datos_ordenados/poblacion_provincias.csv')


agrupado = poblacion.groupby(by='region').sum()
agrupado.drop(columns='provincia',inplace=True)
agrupado.reset_index(inplace=True)

# ---FILTROS---
st.sidebar.header('Filtros')

region = st.sidebar.multiselect(
    'Seleccionar regiones:',
    options=agrupado['region'].unique(),
    default=agrupado['region'].unique()   
)

conexiones_lentas = conexiones_lentas.query(
    'region == @region '
)


map_con = conexiones_lentas[['latitude','longitude']]

left, right = st.columns(2)
with left:
    # scatter map
    st.write('''Localidades con conexiones lentas. Fuente: ENACOM''')
    st.map(data=map_con)
with right:
    # pie plot
    st.write('''Población por región. Fuente: INDEC''')
    fig = px.pie(
        data_frame=agrupado,
        values='poblacion',
        names='region',
        color='region',
        color_discrete_sequence=[
            px.colors.qualitative.G10[1],
            px.colors.qualitative.G10[2],
            px.colors.qualitative.G10[3],
            px.colors.qualitative.G10[4],
            px.colors.qualitative.G10[5],
            px.colors.qualitative.G10[6]],
        labels={'region':'Region'},
        template='presentation',
        width=600,
        height=600

    )
    st.plotly_chart(fig)











conexiones_lentas.drop(columns='link',inplace=True)
st.write('''Detalle localidades con conexiones lentas''')
st.write(conexiones_lentas)




# MOSTRAR PALETA DE PLOTLY
#fig = px.colors.qualitative.swatches()
#fig.show()

