#Importar librerias

import streamlit as st
import random

# ---- Juego 1: Adivina el Número ----

# Configuración de la página

st.set_page_config(
    page_title="Adivina",
    page_icon=":1234:"
    )

#Información y juego
st.title("🎯 Adivina el número secreto")
st.image("adivina.jpg")
st.markdown(
"""La idea central del juego —adivinar un número elegido por otro jugador mediante pistas— proviene de **juegos de lógica y adivinanzas muy antiguos**. Civilizaciones antiguas ya practicaban juegos de “sí o no” o de deducción numérica como **pasatiempos intelectuales**.
En la era victoriana, se popularizaron los llamados "parlor games" (juegos de salón), entre ellos algunos basados en adivinar **números o palabras con pistas**. Estos se consideran antecesores directos del “Adivina el número”.
Hoy en día, “Adivina el número” sigue siendo uno de los **primeros ejercicios** que se enseñan en Python, Java, C++, JavaScript y otros lenguajes, debido a su simplicidad y valor educativo.

También existen versiones más complejas (con interfaces gráficas o niveles de dificultad) que se usan como mini-juegos o proyectos introductorios en cursos de programación.

a continuación te invitamos a probar este mini juego:
"""
    )
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 20)

guess = st.slider("Elige un número del 1 al 20", 1, 20, 10)

if st.button("Comprobar"):
    if guess == st.session_state.number:
        st.balloons()
        st.success("🎉 ¡Correcto! El número era " + str(st.session_state.number))
        st.session_state.number = random.randint(1, 20)
    elif guess < st.session_state.number:
        st.warning("📉 Demasiado bajo, intenta un número mayor.")
    else:
        st.warning("📈 Demasiado alto, intenta un número menor.")
        
st.audio("Circo.mp3")

