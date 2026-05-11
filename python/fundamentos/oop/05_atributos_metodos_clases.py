"""
05. Atributos, Métodos y Clases
"""
# Definición de la clase:
class Estudiante:
    colegio = "Liceo comercial Vate Vicente Huidobro" # <-- Atributo de clase
    alumnos = [] # <-- Lista en donde están todos los estudiantes

    # Método constructor:
    def __init__(self, nombre, nota):
        # Atributos de instancia:
        self.nombre = nombre
        self.nota = nota
    
        Estudiante.alumnos.append(self) # <-- Agregar elementos a la lista "alumnos"

    def mostrarInfo(self): # <-- Método de instancia
        print(f"Nombre: {self.nombre}\nNota: {self.nota}")

    @classmethod # <-- Método de clase
    def cambiarColegio(cls, nuevoNombre):
        cls.colegio = nuevoNombre
    
    @classmethod
    def cantidadEstudiantes(cls, estudiantes):
        return len(cls.alumnos)
    
    @staticmethod
    def aprobador(nota):
        if nota >= 4.0:
            return True
        else:
            return False
# Creación de objetos (Instancias):
estudiante1 = Estudiante("Donovan", 4.6)
estudiante2 = Estudiante("Randy", 6.7)

# Uso de métodos (Instancias):
print(" <== ATRIBUTO DE CLASE ==> ")
estudiante1.mostrarInfo()
estudiante2.mostrarInfo()

print()

# Uso de métodos (Instancias):
print(" <== MÉTODO DE CLASE ==> ")
Estudiante.cambiarColegio("Purkuyen")
print(estudiante1.colegio)
print(estudiante2.colegio)

print()

# Contar estudiantes:
print(" <== CONTAR ESTUDIANTES ==> ")
print(f"Totál estudiantes: {Estudiante.cantidadEstudiantes()}")

# Método estático:
print(" <== MÉTODO ESTÁTICO ==> ")
# WIP

# Función de repaso:
def validadorDatos(usuario, contrasena):
    if usuario == "Matias123" and contrasena == "matias123":
        print(f"Bienvenido usuario {usuario}!")
        return True
    else:
        print("Acceso denegado...")
        return False

def ingresarDatos():
    user = input("Ingrese nombre de Usuario: ")
    password = input(f"Ingrese la contraseña de {user}")
    validador = validadorDatos(user, password)
ingresarDatos()

