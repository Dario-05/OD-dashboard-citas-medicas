import streamlit as st
import pandas as pd
import plotly.express as px

OD_df = pd.read_csv('OD_citas_medicas.csv')

st.title('Dashboard de Gestión de Citas Médicas')

st.subheader('Citas por Especialidad')
OD_esp = OD_df['especialidad'].value_counts().reset_index()
OD_esp.columns = ['especialidad', 'cantidad']
OD_fig1 = px.bar(OD_esp, x='especialidad', y='cantidad')
st.plotly_chart(OD_fig1)

st.subheader('Estado de las Citas')
OD_fig2 = px.pie(OD_df, names='estado')
st.plotly_chart(OD_fig2)

OD_df['fecha'] = pd.to_datetime(OD_df['fecha'])
OD_df['mes'] = OD_df['fecha'].dt.month
OD_citas_mes = OD_df.groupby('mes').size().reset_index(name='cantidad')

st.subheader('Citas por Mes')
OD_fig3 = px.line(OD_citas_mes, x='mes', y='cantidad', markers=True)
st.plotly_chart(OD_fig3)