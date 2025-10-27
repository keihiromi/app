# Importar streamlit
import streamlit as st

# ---------------------  Contenido del sitio   --------------------------#
#Configuración de la página
st.set_page_config(
    page_title="inicio",
    page_icon=":speaking_head:"
    )
# Sección Inicial
st.title("NO + aburrimiento ")
st.image("mono.jpg")

# Subtítulo
st.header("*Problema a resolver*", divider=True)

#Introducción a la página
st.write(
"""
Muchos estudiantes se aburren durante los recreos, clases libres o tiempos muertos, y no saben cómo entretenerse de forma sana y rápida esta app va designada para estudiantes de 12 a 18 años. 

"""
    )
st.header("*Usuario objetivo*", divider=True)
st.write(
"""
Escolares con acceso a internet para que puedan acceder a la app.
Con preferencia para jovenes con poco tiempo libre, que les gusten los desafíos y que sean curiosos.
que busquen entretenimiento ligero y juegos rápidos que puedan disfrutar.

"""
    )

st.header("*¿Cómo ayuda al usuario a resolver su problema?*", divider=True)
st.write(
"""
La creación busca entretener y ayudar a jovenes del rango de edad antes mencionado, no busca distraer de sus responsabilidades sino buscar que sea más divertido y facilitar el acceso a actividades recreativas usando la tecnologia.

"""
    )

