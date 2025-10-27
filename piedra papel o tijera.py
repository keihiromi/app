#Importar librerias

import streamlit as st
import random
import cachipun

# ---- Juego 2: Piedra, Papel o Tijeras ----

#Configuración de la página

st.set_page_config(
    page_title="Cachipun",
    page_icon=":zany:"
    )
#Información y juego
st.title("*Bienvenido al Cachipun*")
st.image("piedra.jpg")
st.markdown(
"""Es el clásico juego de **Piedra Papel o Tijera** pero simplificado para tu diversión personal, es bastante simple con resultados rápidos y aleatorios.
La historia del cachipún —también conocido como piedra, papel o tijera— es muy antigua y tiene sus raíces en Asia, particularmente en China y Japón.El juego se remonta a la antigua China, durante la dinastía Han (206 a. C. – 220 d. C.), donde existía un juego llamado “shoushiling”, que se jugaba con las manos para decidir un ganador de forma rápida y justa.
El juego llegó a Japón probablemente entre los siglos XVII y XVIII, donde se transformó en “jan-ken”, con las tres figuras que conocemos hoy, la piedra, papel y tijera.
El jan-ken se popularizó mucho en la cultura japonesa y se usaba tanto para tomar decisiones como para entretenimiento. Es en Japón donde se fijaron las reglas modernas: piedra vence tijeras, tijeras vence papel, papel vence piedra.

El nombre “Cachipún”

En Chile, el juego se conoce como cachipún, aunque su origen etimológico exacto no está claro. Probablemente provenga de una deformación de sonidos usados durante el juego (como “ca-chi-pún” al marcar el ritmo con las manos).
La expresión “¡cachipún!” se dice al momento de mostrar las manos, como en otras versiones donde se dice “¡piedra, papel o tijera!”.

*Curiosidades*

Es considerado **un juego de azar con estrategia**, ya que los jugadores pueden intentar anticipar el patrón del rival.

Existen **torneos internacionales** de piedra, papel o tijera.

En la cultura popular, se ha usado para **resolver disputas** de forma humorística o justa.

"""
    )
st.write("Dado este breve contexto, para jugar, por favor selecciona: piedra, papel o tijera.")

options = ["Piedra", "Papel", "Tijera"]
pc_opt = random.choice(options)

option = st.selectbox(
    'Selecciona tu opción',
    ('Piedra', 'Papel', 'Tijera'))

st.write('La computadora ha seleccionado:', pc_opt)

st.markdown(f"### {cachipun.result(pc_opt, option)}")

st.audio("Circo.mp3")

