def result(pc_opt, user_opt):
    if pc_opt == user_opt:
        resultado = "Empate 😐"
    elif pc_opt == "Piedra" and user_opt == "Papel":
        resultado = "Ganaste 😂"
    elif pc_opt == "Piedra" and user_opt == "Tijera":
        resultado = "Perdiste 😒"
    elif pc_opt == "Papel" and user_opt == "Piedra":
        resultado = "Perdiste 😒"
    elif pc_opt == "Papel" and user_opt == "Tijera":
        resultado = "Ganaste 😂"
    elif pc_opt == "Tijera" and user_opt == "Piedra":
        resultado = "Ganaste 😂"
    elif pc_opt == "Tijera" and user_opt == "Papel":
        resultado = "Perdiste 😒"

    return resultado
