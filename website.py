# Importar streamlit
import streamlit as st

# Configurar la pagina
st.set_page_config(
    page_title="App",
    page_icon=":star:", # Usar el comando python -m rich.emoji para ver lista de emojis
    layout="centered",
)

pg = st.navigation(["Inicio.py", "piedra papel o tijera.py", "trivia.py", "contador.py", "adivina el numero.py", "about us.py"])
pg.run()
