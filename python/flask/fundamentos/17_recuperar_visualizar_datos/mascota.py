# ==========================================================
# MODELO MASCOTA
# ==========================================================

from mysqlconnection import connectToMySQL


# ==========================================================
# CLASE MASCOTA
# ==========================================================

class Mascota:
    """
    Representa un registro de la tabla mascotas.
    """

    def __init__(self, data):
        """
        Recibe un diccionario proveniente de MySQL
        y lo transforma en atributos del objeto.
        """

        self.id = data["id"]

        self.nombre = data["nombre"]

        self.tipo = data["tipo"]

        self.color = data["color"]

        self.created_at = data["created_at"]

        self.updated_at = data["updated_at"]


    # ======================================================
    # OBTENER TODAS LAS MASCOTAS
    # ======================================================

    @classmethod
    def get_all(cls):
        """
        Consulta todas las mascotas almacenadas
        en la base de datos.

        Retorna una lista de objetos Mascota.
        """

        # --------------------------------------------------
        # CONSULTA SQL
        # --------------------------------------------------

        query = """
            SELECT *
            FROM mascotas;
        """


        # --------------------------------------------------
        # EJECUTAR CONSULTA
        # --------------------------------------------------

        resultados = connectToMySQL(
            "primera_flask"
        ).query_db(query)


        # --------------------------------------------------
        # CREAR LISTA DE OBJETOS
        # --------------------------------------------------

        mascotas = []


        # --------------------------------------------------
        # CONVERTIR RESULTADOS EN OBJETOS
        # --------------------------------------------------

        for mascota in resultados:

            mascotas.append(
                cls(mascota)
            )


        # --------------------------------------------------
        # RETORNAR RESULTADOS
        # --------------------------------------------------

        return mascotas


    # ======================================================
    # OBTENER MASCOTAS POR TIPO
    # ======================================================

    @classmethod
    def get_by_tipo(cls, tipo):
        """
        Consulta únicamente las mascotas cuyo tipo coincida
        con el criterio especificado.

        Retorna una lista de objetos Mascota.
        """

        # --------------------------------------------------
        # CONSULTA SQL ESPECÍFICA (CON PLACEHOLDER)
        # --------------------------------------------------

        query = """
            SELECT * 
            FROM mascotas 
            WHERE tipo = %(tipo)s;
        """


        # --------------------------------------------------
        # DICCIONARIO DE DATOS PARA EL PLACEHOLDER
        # --------------------------------------------------

        data = {
            "tipo": tipo
        }


        # --------------------------------------------------
        # EJECUTAR CONSULTA PASANDO LOS DATOS
        # --------------------------------------------------

        resultados = connectToMySQL(
            "primera_flask"
        ).query_db(query, data)


        # --------------------------------------------------
        # CREAR LISTA DE OBJETOS
        # --------------------------------------------------

        mascotas_filtradas = []


        # --------------------------------------------------
        # CONVERTIR RESULTADOS EN OBJETOS
        # --------------------------------------------------

        if resultados:
            for mascota in resultados:
                mascotas_filtradas.append(
                    cls(mascota)
                )


        # --------------------------------------------------
        # RETORNAR RESULTADOS
        # --------------------------------------------------

        return mascotas_filtradas
