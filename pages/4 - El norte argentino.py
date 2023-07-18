import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import plotly.graph_objects as go


st.set_page_config(page_title='Estadísticas nacionales',
                   page_icon=":bar_chart:",
                   layout='wide',
                   initial_sidebar_state='collapsed'
                   )

df=pd.read_csv('datasets/encc_2017.csv')
df.head()

df = df[(df['region']=='NEA') | (df['region']=='NOA')]

#st.markdown(f"<h3 style='text-align: center; color: white;'>El norte argentino: mejor conectado </h3>", unsafe_allow_html=True)
st.header('El norte argentino: mejor conectado')
st.markdown('---')

left,right = st.columns(2)

with left:
    # pie plot minutos de consumos culturales ENCC
    agrupados = pd.DataFrame(columns=['Minutos'])
    agrupados.loc['Internet']=df['minutos_internet_total'].mean()
    agrupados.loc['Diario']=df['minutos_diario_total'].mean()
    agrupados.loc['Televisión']=df['minutos_tv_total'].mean()
    agrupados.loc['Radio']=df['minutos_radio_total'].mean()
    agrupados=round(agrupados,0)
    agrupados.reset_index(inplace=True)
    agrupados.rename(columns={'index':'Dispositivo'},inplace=True)
    st.write('''Consumos culturales diarios en minutos. Norte Argentina (NOA y NEA). Fuente: ENCC 2017''')
    fig = px.pie(
        data_frame=agrupados,
        values='Minutos',
        names='Dispositivo',
        color='Dispositivo',
        color_discrete_sequence=[
            px.colors.qualitative.G10[1],
            px.colors.qualitative.G10[2],
            px.colors.qualitative.G10[3],
            px.colors.qualitative.G10[4],
            px.colors.qualitative.G10[5],
            px.colors.qualitative.G10[6]],
        labels={'consumo':'Dispositivo'},
        template='presentation',
        width=600,
        height=600

    )
    st.plotly_chart(fig)

with right:
    # pie plot uso de internet
    uso_in = df.groupby(by='p72').id.count()
    uso_in.reset_index()
    uso_in=pd.DataFrame(uso_in)
    uso_in.reset_index(inplace=True)
    uso_in.rename(columns={'p72':'usa_internet','id':'count'},inplace=True)

    st.write('''Uso de internet. Norte Argentina (NOA y NEA). Fuente: ENCC 2017''')
    fig = px.pie(
        data_frame=uso_in,
        values='count',
        names='usa_internet',
        color='usa_internet',
        color_discrete_sequence=[
            px.colors.qualitative.G10[1],
            px.colors.qualitative.G10[2],
            px.colors.qualitative.G10[3],
            px.colors.qualitative.G10[4],
            px.colors.qualitative.G10[5],
            px.colors.qualitative.G10[6]],
        labels={'consumo':'usa_internet'},
        template='presentation',
        width=600,
        height=600

    )
    st.plotly_chart(fig)


with left:
    # grafico redes
    st.write('''Porcentaje de la población activa en redes sociales (nación). Fuente: ENCC 2019''')
    redes_dict = {'2013':['57%'],
                '2017':['70%'],
                '2022':['95%']}

    redes = pd.DataFrame(redes_dict)

    redes = redes.T.reset_index()
    redes.rename(columns={'index':'Año',0:'Uso redes'},inplace=True)

    fig = px.bar(
        data_frame=redes,
        x='Año',
        y='Uso redes',
        text='Uso redes',
        color_discrete_sequence=[px.colors.qualitative.G10[1],
                px.colors.qualitative.G10[2],
                px.colors.qualitative.G10[3],],
        width=650,
        height=500

    )

    st.plotly_chart(fig)

with right:
    # plot consumo tv
    st.write('Total nacional de subscripciones a TV. Fuente: ENACOM')
    tv = pd.read_csv('datasets/Television.csv')
    tv['Accesos TV por suscripción']=tv['Accesos TV por suscripción'].str.replace('.','')
    tv['Accesos TV por suscripción']=tv['Accesos TV por suscripción'].astype(int)
    tv.rename(columns={'Accesos TV por suscripción':'Subscripciones'},inplace=True)
    tv=tv.groupby(['Año'])['Subscripciones'].sum()
    layout = go.Layout(
                xaxis=dict(title='Período'),
                yaxis=dict(title='Subscripciones'),
                width=650,
                height=500,
                )
    
    fig = go.Figure(data=go.Scatter(x=tv.index, y=tv),layout=layout)
    st.plotly_chart(fig)