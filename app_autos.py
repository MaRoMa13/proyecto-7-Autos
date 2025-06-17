import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv('../vehicles_us.csv')  # leer los datos
