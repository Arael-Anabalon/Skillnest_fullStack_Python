# ==========================================================
# SERVIDOR FLASK
# ==========================================================

from flask import Flask, render_template

from mascota import Mascota


# ==========================================================
# CREAR APLICACIÓN
# ==========================================================

app = Flask(__name__)


# ==========================================================
# RUTA PRINCIPAL
# ==========================================================

@app.route("/")
def index():
    """
    Muestra todas las mascotas.
    """

    mascotas = Mascota.get_all()

    return render_template(
        "index.html",
        mascotas=mascotas
    )


# ==========================================================
# RUTA PARA BUSCAR MASCOTA POR ID
# ==========================================================

@app.route("/mascota/<int:id>")
def mostrar_mascota(id):
    """
    Recibe un ID desde la URL y busca la mascota
    correspondiente en la base de datos.
    """

    mascota = Mascota.get_by_id(id)


    # ------------------------------------------------------
    # Si no existe la mascota, mostramos un mensaje.
    # ------------------------------------------------------

    if mascota is None:

        return "Mascota no encontrada", 404


    # ------------------------------------------------------
    # Mostrar mascota encontrada.
    # ------------------------------------------------------

    return render_template(
        "mascota.html",
        mascota=mascota
    )


# ==========================================================
# ACTIVIDAD: RUTA PARA BUSCAR MASCOTA POR NOMBRE
# ==========================================================

@app.route("/mascota/nombre/<string:nombre>")
def mostrar_mascota_por_nombre(nombre):
    """
    Recibe un nombre desde la URL y busca la mascota
    correspondiente en la base de datos.
    """

    mascota = Mascota.get_by_name(nombre)


    # ------------------------------------------------------
    # Si no existe la mascota, mostramos un mensaje.
    # ------------------------------------------------------

    if mascota is None:

        return f"Mascota '{nombre}' no encontrada", 404


    # ------------------------------------------------------
    # Mostrar mascota encontrada.
    # ------------------------------------------------------

    return render_template(
        "mascota.html",
        mascota=mascota
    )


# ==========================================================
# DESAFÍO: RUTA PARA FILTRAR MASCOTAS POR TIPO
# ==========================================================

@app.route("/mascotas/tipo/<string:tipo>")
def mostrar_mascotas_por_tipo(tipo):
    """
    Busca todas las mascotas de un tipo específico (ej. Perro, Gato)
    y las lista en pantalla usando la plantilla principal.
    """

    mascotas_filtradas = Mascota.get_by_tipo(tipo)


    # ------------------------------------------------------
    # Mostrar lista filtrada.
    # ------------------------------------------------------

    return render_template(
        "index.html",
        mascotas=mascotas_filtradas
    )


# ==========================================================
# EJECUTAR SERVIDOR
# ==========================================================

if __name__ == "__main__":

    app.run(debug=True)
