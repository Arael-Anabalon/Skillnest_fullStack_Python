from flask import Flask, render_template, abort
app = Flask(__name__)

jugadores = [
    {"nombre": "AlexGamer", "puntaje": 5000},
    {"nombre": "PixelMaster", "puntaje": 7500},
    {"nombre": "ShadowNinja", "puntaje": 8200},
    {"nombre": "CyberWarrior", "puntaje": 9100},
    {"nombre": "UltraNoob", "puntaje": 3000}
]

@app.route("/")
def ranking():
    return render_template(
        "ranking.html",
        jugadores=jugadores,
        color=None
    )

@app.route("/ranking/<int:cantidad>")
def ranking_limitado(cantidad):
    if 1 <= cantidad <= 5:
        return render_template("ranking.html",
                                jugadores=jugadores[:cantidad],
                                color=None)
    else:
        return abort(404)

@app.route("/ranking/<int:cantidad>/<color>")
def ranking_color(cantidad, color):
    return render_template("ranking.html",
                        jugadores=jugadores[:cantidad],
                        color=color
                        )

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return "⚠️ Error 404 - Página no encontrada.", 404

if __name__ == "__main__":
    app.run(debug=True)