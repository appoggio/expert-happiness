import streamlit as st

from data import *
from input import image_input, webcam_input

st.title("Neural Style Transfer by INTELLIGENZAARTIFICIALEITALIA.NET")
st.text("\n\n Scegli l'input")
method = st.sidebar.radio("Da dove vuoi prendere l'immagine da modificare ? ", options=['Webcam Live', 'Voglio caricare una foto'])


st.header('Opzioni')
style_model_name = st.sidebar.selectbox("Choose the style model: ", style_models_name)

if method == 'Voglio caricare una foto':
    image_input(style_model_name)
else:
    webcam_input(style_model_name)
