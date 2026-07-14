from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "¡Hola Mundo!"

@app.route("/exito")
def exito():
    return "¡Éxito!"

if __name__ == "__main__":
    app.run(debug=True)



