#Importar librerias

import streamlit as st
import random

# ---- Juego 4: Trivia ----

# Configuración de la página}

st.set_page_config(
    page_title="Trivia",
    page_icon=":brain:"
    )

st.title("🤔 Juego: Trivia Sí o No")
st.image("time.jpg")
st.markdown("Este juego es una trivia de preguntas de cultura general, con ello puedes ganar puntos y sí no lo sabes también sirve para darte un dato interesante!")

# Lista de preguntas (pregunta, respuesta correcta)
preguntas = [
    ("El sol es una estrella.", "Sí"),
    ("La capital de Francia es Berlín.", "No"),
    ("2 + 2 = 4.", "Sí"),
    ("Los pingüinos vuelan.", "No"),
    ("Python es un lenguaje de programación.", "Sí"),
    ("Blancanieves fue la primera princesa emitida por Disney", "Sí"),
    ("Sócrates se envenenó con Cicuta", "Sí"),
    ("París es la capital de Estados Unidos", "No"),
    ("Van Gogh pintó la Mona Lisa","No")
]

# Guardar estado
if "pregunta" not in st.session_state:
    st.session_state.pregunta = random.choice(preguntas)
    st.session_state.puntaje = 0

# Mostrar pregunta
st.write(f"**Pregunta:** {st.session_state.pregunta[0]}")

# Opción del jugador
respuesta = st.radio("Tu respuesta:", ["Sí", "No"])

# Botón para verificar
if st.button("Comprobar"):
    if respuesta == st.session_state.pregunta[1]:
        st.success("✅ ¡Correcto!")
        st.session_state.puntaje += 1
        st.balloons()
    else:
        st.error(f"❌ Incorrecto. La respuesta era {st.session_state.pregunta[1]}.")
    # Nueva pregunta
    st.session_state.pregunta = random.choice(preguntas)
    st.rerun()

# Mostrar puntaje
st.write(f"Puntaje actual: **{st.session_state.puntaje}**")
st.audio("Circo.mp3")
