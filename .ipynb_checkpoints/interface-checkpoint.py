import streamlit as st
import pandas as pd
from models1 import VF_classifier

st.title("Detector de noticias falsas")

st.subheader("Introduzca una noticia: ")
noticia = st.text_area('', 'Ej: El Partido Popular ha ganado las elecciones generales con 136 escaños, 47 más que en 2019, aunque lejos de la mayoría absoluta necesaria para gobernar...')

st.write("\n\n")
st.write("\n\n")

prediccion = VF_classifier([noticia])

if st.button('Comprobar veracidad'):
    if prediccion == 0:
        st.write('Predicción: ', "Verdadera")
    if prediccion == 1:
        st.write('Predicción: ', "FALSAAAAA")