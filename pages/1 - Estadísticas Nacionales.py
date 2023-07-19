import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

st.set_page_config(page_title='Estadísticas nacionales',
                   page_icon=":bar_chart:",
                   layout='wide',
                   initial_sidebar_state='collapsed'
                   )


        
nacionales = pd.read_csv('datos_ordenados/nacionales.csv')
nacionales=nacionales.iloc[::-1]
# total de conexiones
nacionales['total_conexiones']=nacionales['dial_up']+nacionales['banda_ancha_fija']

#st.markdown(f"<h3 style='text-align: center; color: white;'>Estadísticas nacionales sobre el servicio de internet </h3>", unsafe_allow_html=True)
st.header('Estadísticas nacionales sobre el servicio de internet')
st.markdown('---')
# ---FILTROS---
st.sidebar.header('Filtros')

año = st.sidebar.select_slider(
    'Seleccionar años:',
    options=nacionales['año'].unique(),
    value=max(nacionales.año.unique())   
)

trimestre = st.sidebar.multiselect(
    'Seleccionar trimestre:',
    options=nacionales['trimestre'].unique(),
    default=nacionales['trimestre'].unique()
)

nacionales_s = nacionales.query(
    'año <= @año & trimestre == @trimestre'
)

# --SECCION KPI---
ingresos_totales = nacionales_s['ingresos_miles'].sum()
promedio_velocidad = nacionales_s['mbps_media'].mean()
total_conexiones = nacionales_s['total_conexiones'].sum()

ing_anuales = nacionales_s.groupby(['año'])['ingresos_miles'].sum()
ing_anuales = pd.DataFrame(ing_anuales)
ing_anuales.reset_index(inplace=True)
ing_anuales['año_ant']=''
for i in ing_anuales.index:
    print(i)
    if i == 0:
        ing_anuales['año_ant'][i] = np.NaN
    else:
        ing_anuales['año_ant'][i] = ing_anuales['ingresos_miles'][i-1]

ing_anuales['año_ant']=ing_anuales['año_ant'].astype(float)

ing_anuales['variacion_interanual'] = ing_anuales['año_ant']/ing_anuales['ingresos_miles']*100

crecimiento_interanual = ing_anuales['variacion_interanual'].mean()

left, middle, right = st.columns(3)

with left:
    st.markdown(f"<h5 style='text-align: center; color: white;'>Crecimiento promedio interanual de los ingresos: </h5> ", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: center; color: white;'>{round(crecimiento_interanual,2)}%</h5>", unsafe_allow_html=True)

with middle:
    st.markdown(f"<h5 style='text-align: center; color: white;'>Promedio nacional de velocidad: </h5>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: center; color: white;'>{round(promedio_velocidad,2)} mbps</h5>", unsafe_allow_html=True)

with right:
    st.markdown(f"<h5 style='text-align: center; color: white;'>Conexiones a banda ancha: </h5>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: center; color: white;'>{total_conexiones}</h5>", unsafe_allow_html=True)

st.markdown('---')



# --- GRAFICOS ---

# ingresos trimestrales
layout = go.Layout(title='Ingresos por prestacion de servicios (miles de pesos). Fuente: ENACOM',
                xaxis=dict(title='Período'),
                yaxis=dict(title='Ingresos (miles de pesos)'),
                height=350,
                width=1530)
fig = go.Figure(data=go.Scatter(x=nacionales_s.periodo, y=nacionales_s.ingresos_miles),layout=layout)
st.plotly_chart(fig)


left,right = st.columns(2)
with right:
    # velocidad de internet promedio
    layout = go.Layout(title='Velocidad de internet promedio en MBPS. Fuente: ENACOM ',
                    xaxis=dict(title='Período'),
                    yaxis=dict(title='Velocidad en MBPS'),
                    width=700,
                    height=350)
    fig = go.Figure(data=go.Scatter(x=nacionales_s.periodo, y=nacionales_s.mbps_media),layout=layout)
    st.plotly_chart(fig)

with left:
    # conexiones
    conexiones = go.Scatter(x=nacionales_s.periodo,y=nacionales_s.total_conexiones)
    layout = go.Layout(title='Conexiones fijas totales. Fuente: ENACOM',
                    xaxis=dict(title='trimestre'),
                    yaxis=dict(title='Total de conexiones'),
                    width=700,
                    height=350)
    fig=go.Figure(data=conexiones,layout=layout)
    st.plotly_chart(fig)




