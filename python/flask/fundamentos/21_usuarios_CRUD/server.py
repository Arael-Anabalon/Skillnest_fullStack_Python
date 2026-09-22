from flask import Flask, render_template, request, redirect, url_for
from usuario import Usuario

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('usuarios'))

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html', todos_usuarios=Usuario.get_all())

@app.route('/usuarios/nuevo')
def usuario_nuevo():
    return render_template('usuario_nuevo.html')

@app.route('/usuarios/crear', methods=['POST'])
def crear_usuario():
    Usuario.save(request.form)
    return redirect(url_for('usuarios'))

@app.route('/usuarios/<int:id>')
def mostrar_usuario(id):
    data = {"id": id}
    return render_template('usuario.html', usuario=Usuario.get_one(data))

@app.route('/usuarios/<int:id>/editar')
def editar_usuario(id):
    data = {"id": id}
    return render_template('usuario_editar.html', usuario=Usuario.get_one(data))

@app.route('/usuarios/actualizar', methods=['POST'])
def actualizar_usuario():
    Usuario.update(request.form)
    return redirect(url_for('mostrar_usuario', id=request.form['id']))

@app.route('/usuarios/<int:id>/eliminar')
def eliminar_usuario(id):
    data = {"id": id}
    Usuario.delete(data)
    return redirect(url_for('usuarios'))

if __name__ == "__main__":
    app.run(debug=True)
