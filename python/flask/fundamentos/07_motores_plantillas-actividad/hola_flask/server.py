from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def bienvenido():
    return render_template('index.html', cancion="Macarena - Los del Río", repite=5)

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return "⚠️ Error 404 - Página no encontrada.", 404

# Ejecuta el servidor
if __name__ == "__main__":
    app.run(debug=True)