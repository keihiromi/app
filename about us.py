# Importar streamlit
import streamlit as st

# ---------------------  Contenido del sitio   --------------------------#
#Configuración de la página
st.set_page_config(
    page_title="Sobre nosotros",
    page_icon=":bookmark_tabs:"
    )
# Sección Inicial
st.title("Sobre nosotros")
st.image("st.jpg")

#Información

st.header("*Contacto*", divider=True)
st.write(
"""
*Product Manager* = Francesca Di Bennedetti

*CEO and Developer* = AemondTargaryenLover78
"""
    )
st.header("Información", divider=True)
st.write(
"""
¡Hola! Somos el equipo detrás de No + Aburrimiento, la app que transforma los ratos libres en momentos de pura diversión. Nuestro objetivo es simple: ofrecerte juegos fáciles, rápidos y adictivos que te saquen una sonrisa (y quizás una que otra victoria épica).

👩‍💼 Francesca Di Bennedetti – Product Manager Extraordinaria
Francesca es la mente maestra que mantiene todo en orden (y evita que nos vayamos por la tangente jugando nuestras propias creaciones). Su nombre suena tan elegante que podrías pensar que viene con su propio fondo orquestal… y, sinceramente, probablemente sí.

💻 AemondTargaryenLover78 – CEO y Desarrolladora Principal
Sí, ese es su usuario real. Y sí, ama Game of Thrones tanto como programar. Cuando no está corrigiendo bugs, está tratando de convencer a todos de que los dragones son una metáfora del código perfecto.

Juntas, creemos que los juegos no tienen que ser complicados para ser divertidos. Solo necesitan un toque de creatividad, una pizca de locura y muchas ganas de pasarlo bien.
"""
    )

st.audio("juego.mp3")
