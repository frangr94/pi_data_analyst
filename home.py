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

# ---TITULO---
st.write('''
## :bar_chart: Dashboard PI data analyst ops
''')
st.write('''### Bienvenidos!''')
st.write('''### Este dashboard contiene información sobre mercado del internet en Argentina entre los años 2014 y 2022 :satellite:''')
st.write('''### Para navegar en la app, haz click en la barra de navegación a la izquierda de la pantalla. En dicha sección también podrás encontrar filtros para aplicar a las distintas visualizaciones.''')