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
    Consulta todas las mascotas y las envía
    hacia la plantilla index.html.
    """

    # ------------------------------------------------------
    # OBTENER MASCOTAS DESDE MYSQL
    # ------------------------------------------------------

    mascotas = Mascota.get_all()


    # ------------------------------------------------------
    # MOSTRAR RESULTADOS EN TERMINAL
    # ------------------------------------------------------

    print(mascotas)


    # ------------------------------------------------------
    # ENVIAR DATOS A JINJA2
    # ------------------------------------------------------

    return render_template(

        "index.html",

        todas_mascotas=mascotas

    )


# ==========================================================
# NUEVA RUTA: FILTRAR POR PERROS
# ==========================================================

@app.route("/mascotas/perros")
def perros():
    """
    Consulta únicamente las mascotas de tipo Perro
    y las envía a la plantilla perros.html.
    """

    # ------------------------------------------------------
    # OBTENER PERROS DESDE MYSQL
    # ------------------------------------------------------

    # Nota: Asegúrate de implementar este método en tu clase Mascota
    perros_filtrados = Mascota.get_by_tipo("Perro")


    # ------------------------------------------------------
    # ENVIAR DATOS A JINJA2
    # ------------------------------------------------------

    return render_template(

        "perros.html",

        los_perros=perros_filtrados

    )


# ==========================================================
# EJECUTAR SERVIDOR
# ==========================================================

if __name__ == "__main__":

    app.run(debug=True)
