#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

@app.route("/jugar_piedra_papel_tijera")
def jugar_piedra_papel_tijera():
    opciones = ["piedra", "papel", "tijera"]
    puntuacion = {"jugador": 0, "oponente": 0}

    while True:
        oponente = random.choice(opciones)
        jugador = input("Elige piedra, papel o tijera: ").lower()

        if jugador not in opciones:
            print("Opción no válida. Por favor, elige piedra, papel o tijera.")
            continue

        resultado_ronda = ""
        if jugador == oponente:
            resultado_ronda = "Empate."
        elif (
            (jugador == "piedra" and oponente == "tijera") or
            (jugador == "papel" and oponente == "piedra") or
            (jugador == "tijera" and oponente == "papel")
        ):
            resultado_ronda = "¡Ganaste esta ronda!"
            puntuacion["jugador"] += 1
        else:
            resultado_ronda = "¡Perdiste esta ronda!"
            puntuacion["oponente"] += 1

        mensaje_puntuacion = f"Puntuación actual - Jugador: {puntuacion['jugador']} Oponente: {puntuacion['oponente']}"

        return f"Oponente eligió: {oponente}\n{resultado_ronda}\n{mensaje_puntuacion}"

if __name__ == "__main__":
    print('hello world')
    app.run()


