# Definición de la clase (el molde)
class Usuario:
    # El constructor inicializa al objeto
    def __init__(self):
        # self es la referencia al objeto mismo
        self.nombre = "Nombre por defecto"
        self.apellido = "Apellido por defecto"

# Instanciación: crear el objeto basado en la clase
usuario_ejemplo = Usuario()

# Acceso a atributos mediante el punto (.)
print(usuario_ejemplo.nombre) 
