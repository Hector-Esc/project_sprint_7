''' Projecto de Sprint 7 '''

import streamlit as st
import pandas as pd
import plotly_express as px

url = "https://raw.githubusercontent.com/Hector-Esc/project_sprint_7/main/vehicles_us.csv"
car_data = pd.read_csv(url)

# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')

option_x = st.selectbox(
    'Seleccionar Eje X para el histograma',  # Etiqueta
    ['price', 'model_year', 'model', 'condition', 'cylinders', 'fuel',
       'odometer', 'transmission', 'type', 'paint_color', 'is_4wd',
       'date_posted', 'days_listed']  # Opciones
)

if build_histogram: # si la casilla de verificación está seleccionada
         # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
         # crear un histograma
    fig = px.histogram(car_data, x=option_x)
     
         # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox('Construir un grafico de dispersion')

option2_x = st.selectbox(
    'Seleccionar Eje X para grafico de dispersion',  # Etiqueta
    ['price', 'model_year', 'model', 'condition', 'cylinders', 'fuel',
       'odometer', 'transmission', 'type', 'paint_color', 'is_4wd',
       'date_posted', 'days_listed']  # Opciones
)

option2_y = st.selectbox(
    'Seleccionar Eje Y para grafico de dispersion',  # Etiqueta
    ['price', 'model_year', 'model', 'condition', 'cylinders', 'fuel',
       'odometer', 'transmission', 'type', 'paint_color', 'is_4wd',
       'date_posted', 'days_listed']  # Opciones
)

if build_scatter:
        # escribir un mensaje
    st.write('Creación de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')
         
         # crear un histograma
    fig = px.scatter(car_data, x=option2_x, y = option2_y)
     
         # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
