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

st.write('''### Estadísticas nacionales sobre el servicio de internet''')

# ---FILTROS---
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

left, middle, right = st.columns(3)

with left:
    st.write('''##### Ingresos totales:''')
    st.write(f'''###### AR${ingresos_totales} mil''')

with middle:
    st.write(''' ##### Promedio de velocidad:''')
    st.write(f'''###### {round(promedio_velocidad,2)} mbps''')

with right:
    st.write('''##### Conexiones a banda ancha:''')
    st.write(f'''###### {total_conexiones}''')

st.markdown('---')

st.sidebar.header('Filtros')

# --- GRAFICOS ---

left,right = st.columns(2)
with left:
    # velocidad de internet promedio
    layout = go.Layout(title='Velocidad de internet promedio en MBPS',
                    xaxis=dict(title='Período'),
                    yaxis=dict(title='Velocidad en MBPS'),
                    width=700,
                    height=350)
    fig = go.Figure(data=go.Scatter(x=nacionales_s.periodo, y=nacionales_s.mbps_media),layout=layout)
    st.plotly_chart(fig)

with right:
    # conexiones
    conexiones = go.Scatter(x=nacionales_s.periodo,y=nacionales_s.total_conexiones)
    layout = go.Layout(title='Conexiones totales',
                    xaxis=dict(title='trimestre'),
                    yaxis=dict(title='Total de conexiones'),
                    width=700,
                    height=350)
    fig=go.Figure(data=conexiones,layout=layout)
    st.plotly_chart(fig)


# ingresos trimestrales
# velocidad de internet promedio
layout = go.Layout(title='Ingresos por prestacion de servicios (miles de pesos)',
                xaxis=dict(title='Período'),
                yaxis=dict(title='Ingresos (miles de pesos)'),
                height=350,
                width=1400)
fig = go.Figure(data=go.Scatter(x=nacionales_s.periodo, y=nacionales_s.ingresos_miles),layout=layout)
st.plotly_chart(fig)


