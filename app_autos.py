
import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Análisis de datos de ventas de coches usados')

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:  # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna condición del coche')

    # crear un histograma
    fig = px.histogram(car_data, x="condition")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

line_button = st.button('Construir gráfico de lineas')  # crea un botón

if line_button:  # al hacer clic en el botón
    # escribir mensaje
    st.write(
        'Creación de un gráfico de lineas para comparar el modelo, precio y condición del coche')
    # agrupación de los datos
    df_model_price = car_data.groupby(['model_year', 'condition'])[
        'price'].mean().reset_index()
    # crea un gráfico de lineas
    fig_2 = px.line(df_model_price, x="model_year",
                    y="price", color='condition')
    st.plotly_chart(fig_2, use_container_width=True)
