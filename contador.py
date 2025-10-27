# Importar librerias
import streamlit as st


# ----  Juego 3: Contador de clics ----

# Configuración de la página

st.set_page_config(
    page_title="Contador",
    page_icon=":8ball:"
    )
#Información y juego
st.title("🖱️ Contador de clics")
st.image("Click.jpg")
st.markdown(
"""Este juego te permite tener como pasatiempo darle clic al botón, no es muy complicado solo sigue haciendolo hasta cuando tu quieras.
"""
    )

# Guardar el puntaje en el estado
if "puntos" not in st.session_state:
    st.session_state.puntos = 0

# Mostrar puntaje
st.metric("Puntaje actual", st.session_state.puntos)

# Botón para sumar puntos
if st.button("¡Haz clic para sumar 1 punto!"):
    st.session_state.puntos += 1
    st.balloons()

# Botón para reiniciar
if st.button("🔄 Reiniciar"):
    st.session_state.puntos = 0
    st.rerun()
    
st.audio("Circo.mp3")