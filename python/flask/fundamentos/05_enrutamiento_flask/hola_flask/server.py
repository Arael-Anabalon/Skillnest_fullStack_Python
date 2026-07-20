from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "¡Hola Mundo!"

@app.route("/saludo/<nombre>")
def saludo(nombre):
    return f"Hola {nombre}"

if __name__ == "__main__":
    @app.errorhandler(404)
    def pagina_no_encontrada(error):
        return """
        <h1><font color="red">⚠️ Error 404</font></h1>
        <h2><font color="orange">¡Falsa alarma!</font></h2>
        
        <p><b><font color="navy">Mensaje del sistema:</font></b> 
        Buscaste tan bien que rompiste el internet. O simplemente escribiste cualquier cosa en la URL. 🤡</p>
        
        <p><i><font color="purple">"No todos los que vagan están perdidos, pero tú definitivamente sí lo estás."</font></i> 
        <br><font color="gray">— Sabiduría Digital</font></p>
        
        <p>👉 <a href="/"><font color="green"><b>🏠 ¡Sácame de aquí y vuelve al inicio!</b></font></a></p>
        """, 404
    app.run(debug=True)