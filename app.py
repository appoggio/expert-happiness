import streamlit as st

from data import *
from input import image_input, webcam_input


st.markdown("<h1 style='text-align: center; background-color: black;font-size:16px;'><bold style='color:green;'>INTELLIGENZA<bold style='color:white;'>ARTIFICIALE<bold style='color:red;'>ITALIA</bold></bold></bold></h1><br><center><small>Prova la nostra Intelligenza Artificiale di Neural Style Transfer", unsafe_allow_html=True)



with st.beta_expander("Opzioni"):
	method = st.radio("Da dove vuoi prendere l'immagine da modificare ? ", options=['Webcam Live', 'Voglio caricare una foto'])

	style_model_name = st.selectbox("Scegli il modello che vuoi applicare", style_models_name)

html_string = "<h3><br></h3>"

st.markdown(html_string, unsafe_allow_html=True)

if method == 'Voglio caricare una foto':
    generated = image_input(style_model_name)
    st.image(generated)
else:
    webcam_input(style_model_name)
