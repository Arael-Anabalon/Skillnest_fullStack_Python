from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template(
        "index.html", 
        nombre = "", 
        apellido = "", 
        curso = "", 
        instruccion = "", 
        anio = 0,
        docente = False,
        lenguajes = [
            "Python",
            "Flask",
            "HTML",
            "CSS",
            "JavaScript"
            ]
        )

if __name__ == "__main__":
    app.run(debug = True)