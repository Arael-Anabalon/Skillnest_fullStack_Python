from conexion import Conexion


class Usuario:

    def __init__(self, usuario=None, contrasena=None, tipo_usuario = 1, created_by="Admin"):
        self.username = usuario
        self.password = contrasena
        self.tipo_usuario = tipo_usuario
        self.created_by = created_by

    def crear_usuario(self):
        conexion = Conexion.conectar()
        cursor = conexion.cursor()
        sql = "INSERT INTO usuarios (usuario, contrasena, tipo_usuario, created_by) VALUES (%s, %s, %s, %s)"
        valores = (
            self.username,
            self.password,
            self.tipo_usuario,
            self.created_by,
        )
        cursor.execute(sql, valores)
        conexion.commit()
        print(f"Usuario {self.username} creado correctamente.")
        cursor.close()
        conexion.close()

    @staticmethod
    def buscar_usuario(id_usuario):
        conexion = Conexion.conectar()
        cursor = conexion.cursor()
        sql = "SELECT id_usuario, usuario, tipo_usuario FROM usuarios WHERE id_usuario = %s AND deleted = 0"
        cursor.execute(sql, (id_usuario,))
        resultado = cursor.fetchone()
        cursor.close()
        conexion.close()
        return resultado

    @staticmethod
    def listado_usuarios():
        conexion = Conexion.conectar()
        cursor = conexion.cursor()
        sql = "SELECT id_usuario, usuario, tipo_usuario FROM usuarios WHERE deleted = 0 ORDER BY id_usuario ASC"
        cursor.execute(sql)
        usuarios = cursor.fetchall()
        cursor.close()
        conexion.close()
        return usuarios

    @staticmethod
    def modificar_usuario(nuevo_tipo, id_usuario):
        conexion = Conexion.conectar()
        cursor = conexion.cursor()
        sql = "UPDATE usuarios SET tipo_usuario = %s WHERE id_usuario = %s"
        cursor.execute(sql, (nuevo_tipo, id_usuario))
        conexion.commit()
        cursor.close()
        conexion.close()

    @staticmethod
    def eliminar_usuario(id_usuario):
        conexion = Conexion.conectar()
        cursor = conexion.cursor()
        sql = "UPDATE usuarios SET deleted = 1 WHERE id_usuario = %s"
        cursor.execute(sql, (id_usuario,))
        conexion.commit()
        print(f"Usuario con ID {id_usuario} eliminado correctamente.")
        cursor.close()
        conexion.close()

    @staticmethod
    def validar_acceso(user, password):
        conexion = Conexion.conectar()
        cursor = conexion.cursor()
        sql = "SELECT id_usuario, usuario, tipo_usuario FROM usuarios WHERE usuario = %s AND contrasena = %s AND deleted = 0"
        cursor.execute(sql, (user, password))
        resultado = cursor.fetchone()
        cursor.close()
        conexion.close()
        return resultado

    @staticmethod
    def cerrar_sesion(username):
        print(f"Sesión del usuario '{username}' cerrada correctamente.")
        return True
