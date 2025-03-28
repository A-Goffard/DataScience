from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Lista de colores y sus pistas
colores = {
    "red": "Es el color de una manzana",
    "blue": "Es el color del cielo",
    "green": "Es el color de la hierba",
    "yellow": "Es el color de un plátano",
    "orange": "Es el color de una naranja"
}

# Seleccionar un color aleatorio
color_aleatorio, pista = random.choice(list(colores.items()))

@app.route("/", methods=["GET", "POST"])
def index():
    global color_aleatorio, pista
    if request.method == "POST":
        color_usuario = request.form.get("color")
        if color_usuario == color_aleatorio:
            mensaje = "¡Correcto! Adivinaste el color."
            color_aleatorio, pista = random.choice(list(colores.items()))  # Seleccionar un nuevo color
        else:
            mensaje = "Incorrecto. Intenta de nuevo."
        return render_template("index.html", pista=pista, mensaje=mensaje, colores=colores.keys())
    return render_template("index.html", pista=pista, mensaje="", colores=colores.keys())

if __name__ == "__main__":
    app.run(debug=True)