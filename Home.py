import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

st.set_page_config(page_title='Home',
                   page_icon=":bar_chart:",
                   layout='wide',
                   initial_sidebar_state='collapsed'
                   )

st.image('src/henry_logo.png')
# ---TITULO---
st.write('''
## :bar_chart: Dashboard PI data analyst ops
''')
st.write('''### ¡Bienvenidos!''')
st.write('''### Este dashboard contiene información sobre mercado del internet en Argentina entre los años 2014 y 2022 :satellite:''')
st.write('''### Fue confeccionado en el marco de la cursada de Henry usando las librerías Streamlit y Plotly.''')
st.write('''### Para navegar en la app, haz click en la barra de navegación a la izquierda de la pantalla. En dicha sección también podrás encontrar filtros para aplicar a las distintas visualizaciones.''')
st.write('''### Si deseas obtener más información visita el README adjunto al repositorio.''')

left, centre, right = st.columns(3)

with centre:
    st.image('src/internet_img.png')


