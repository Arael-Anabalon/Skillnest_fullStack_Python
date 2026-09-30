from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

# Clave secreta necesaria para firmar y proteger las sesiones de Flask
app.secret_key = "clave-secreta-visitas"

@app.route("/")
def index():
    if "visitas" in session:
        session["visitas"] += 1
    else:
        session["visitas"] = 1

    if "reinicios" not in session:
        session["reinicios"] = 0

    session.modified = True

    return render_template(
        "index.html",
        visitas=session["visitas"],
        reinicios=session["reinicios"]
    )

@app.route("/incrementar_doble")
def incrementar_doble():
    if "visitas" not in session:
        session["visitas"] = 0
    
    session["visitas"] += 1
    return redirect(url_for("index"))

@app.route("/restablecer_contador")
def restablecer_contador():
    if "reinicios" not in session:
        session["reinicios"] = 0

    session["reinicios"] += 1
    session["visitas"] = 0 # Restablece las visitas a cero sin borrar los reinicios
    return redirect(url_for("index"))

@app.route("/incrementar_por_cantidad", methods=["POST"])
def incrementar_por_cantidad():
    cantidad = int(request.form["cantidad"])

    if "visitas" not in session:
        session["visitas"] = 0

    session["visitas"] += cantidad
    return redirect(url_for("index"))

@app.route("/limpiar_sesion")
def limpiar_sesion():
    session.clear() # Limpia por completo la sesión (visitas y reinicios vuelven a empezar)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
