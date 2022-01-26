import streamlit as st

from data import *
from input import image_input, webcam_input

st.title("Neural Style Transfer by INTELLIGENZAARTIFICIALEITALIA.NET")
html_string = "<h3>this is an html string</h3>"

st.markdown(html_string, unsafe_allow_html=True)

method = st.radio("Da dove vuoi prendere l'immagine da modificare ? ", options=['Webcam Live', 'Voglio caricare una foto'])

style_model_name = st.selectbox("Scegli il modello che vuoi applicare", style_models_name)

if method == 'Voglio caricare una foto':
    image_input(style_model_name)
else:
    webcam_input(style_model_name)
