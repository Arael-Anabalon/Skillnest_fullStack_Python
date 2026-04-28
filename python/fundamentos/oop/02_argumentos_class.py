class Usuario:
    # El constructor ahora recibe datos externos (argumentos)
    def __init__(self, nombre, apellido, email):
        # Asignamos los argumentos a los atributos de la instancia
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        
        # Atributos con valores iniciales fijos (no vienen por argumentos)
        self.limite_credito = 30000
        self.saldo_pagar = 0

# Creamos instancias pasando los datos requeridos
# Nota: 'self' no se pasa, Python lo gestiona internamente
miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la")
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la")
dany = Usuario("Dany", "Hernández", "danyhernandez@gmail.com")

# Comprobación de que cada objeto tiene sus propios datos
print(f"Instancia 1: {miyagi.nombre} - Email: {miyagi.email}")
print(f"Instancia 2: {daniel.nombre} - Email: {daniel.email}")

# Los valores fijos son iguales para ambos al iniciar
print(f"Saldo inicial de {daniel.nombre}: ${daniel.saldo_pagar}")

print("-" * 20)

"""
Tarea rápida:
- Crear una clase estudiante
- Asignar atributos:
    + Rut
    + Nombre
    + Apellido
    + Fecha nacimiento
- Crear 3 instancias para la clase con distintas personas
- Impimir nombre, apellido y especialidad
"""
class Estudiante:
    def __init__(self, rut, nombre, apellido, especialidad, fechaNac):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.especialidad = especialidad
        self.fechaNac = fechaNac

martin = Estudiante("22.840.632-5", "Martín", "Rojas", "Programación", "04-10-2008")
yulieth = Estudiante("27.461.998-8", "Yulieth", "Gonzáles", "Programación", "12-03-2008")
isidora = Estudiante("22.796.812-5", "Isidora", "Valenzuela", "Programación", "19-06-2008")

print(f"Nombre: {martin.nombre}\nApellido: {martin.apellido}\nEspecialidad: {martin.especialidad}")