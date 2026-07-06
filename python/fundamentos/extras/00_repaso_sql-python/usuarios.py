from conexion import Conexion

class Usuario:
    def __init__(self, usuario = None, contrasena = None, tipo_usuario = None, created_by = "Admin"):
        self.username = usuario
        self.password = contrasena
        self.user_type = tipo_usuario
        self.created_by = created_by

    def crear_usuario (self):
        conexion = Conexion.conectar()
        cursor = conexion.cursor()
        sql = "INSERT INTO usuarios (usuario, contrasena, tipo_usuario, created_by) VALUES (%s, %s, %s, %s)"
        valores = (
            self.username, 
            self.password, 
            self.user_type,
            self.created_by
        )
        cursor.execute(sql, valores)
        conexion.commit()
        print(f"Usuario {self.username} creado correctamente.")
        cursor.close()
        conexion.close()
    
    @staticmethod
    def buscar_usuario():
        pass

    @staticmethod
    def listado_usuarios():
        pass

    @staticmethod
    def modificar_usuario():
        pass

    @staticmethod
    def eliminar_usuario():
        
    
    def validar_acceso():
        pass

    

