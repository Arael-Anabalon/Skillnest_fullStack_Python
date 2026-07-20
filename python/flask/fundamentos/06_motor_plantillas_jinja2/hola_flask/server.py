from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html", 
            nombre = "Arael",
            ciudad = "Santiago",
            curso = "Flask - Jinja2",
            anio = 2026,
            profesor = False,
            tecnologias = ["Python","Flask","HTML","CSS"])

@app.route("/jugador")
def jugador():
    return render_template("jugador.html",
                jugador = "Ara173jkC",
                puntaje = 1730,
                lider = False)

@app.route("/institucion")
def institucion():
    return render_template("institucion.html",
                nombre = "",
                apellido = "",
                curso = "",
                institucion = "",
                anio = 2000,
                es_docente = False,
                tecnologias = ["Python","Flask","HTML","CSS"])

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return "⚠️ Error 404 - Página no encontrada.", 404

if __name__ == "__main__":
    app.run(debug=True)

    
