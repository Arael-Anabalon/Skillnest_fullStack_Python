class Usuario: 
    def __init__(self, userName, userId, email):
        self.usuario = userName
        self.id_usuario = userId
        self.correo = email
    
    def mostrar_datos(self):
        print(f"Usuario: {self.usuario}\nID: {self.id_usuario}\nCorreo electrónico: {self.correo}")
    
    def actualizar_correo(self, nuevoCorreo):
        self.correo = nuevoCorreo
        print(f"Correo cambiado con exito a {nuevoCorreo}")

class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo_libro = titulo
        self.nombre_autor = autor
        self.isbn_libro = isbn
        self.disponible = True
    
    def mostrar_informacion(self):
        print(f"Libro: {self.titulo_libro}\nAutor: {self.nombre_autor}\nISBN: {self.isbn_libro}")
    
    def cambiar_disponibilidad(self, cambiar_estado):
        self.disponible = cambiar_estado

class Prestamo:
    def __init__(self, prestamoId):
        self.id_prestamo = prestamoId
        self.usuario = None
        self.libro = None
    
    def registrar_prestamo(self, usuario, libro):
        if libro.disponible:
            self.usuario = usuario
            self.libro = libro
            print(f"Prestamo registrado!\nEl libro '{self.libro.titulo_libro}' ha sido entregado a {self.usuario.usuario}\n")
            libro.cambiar_disponibilidad(False)
        else:
            print(f"El libro no está disponible")
    
    def devolver_libro(self):
        if self.libro is not None:
            self.libro.cambiar_disponibilidad(True)
            self.usuario = None
            self.libro = None
        else:
            print(f"No hay ningún libro registrado.")

usuario1 = Usuario("Arael", 1, "araelanabalon@liceovvh.cl")
usuario2 = Usuario("Juan", 2, "juandonoso@liceovvh.cl")
usuario3 = Usuario("Jonathan", 3, "jonathanalquinta@liceovvh.cl")
usuario4 = Usuario("Alexander", 4, "alexanderpino@liceovvh.cl")

libro1 = Libro("Adiós a las armas", "Ernest Hemingway", "9788490622827")
libro2 = Libro("El Spleen de París", "Charles Baudelaire", " 9788420684512")
libro3 = Libro("Los ojos del perro siberiano", "Antonio Santa Ana", "9789504653110")

prestamo_actual = Prestamo(1)

continuar = True 
while continuar:
    print("\n--- Sistema de Biblioteca ---")
    print("1. Mostrar datos de usuarios")
    print("2. Actualizar correo de un usuario")
    print("3. Mostrar información de libros")
    print("4. Registrar un préstamo")
    print("5. Devolver un libro")
    print("0. Salir")
    
    opcion = input("\nElije una opción (0-5): ")
    if opcion == "1":
        usuario1.mostrar_datos()
        usuario2.mostrar_datos()
        usuario3.mostrar_datos()
        usuario4.mostrar_datos()
    elif opcion == "2":
        nuevo_correo = input("Ingresa el nuevo correo para Arael: ")
        usuario1.actualizar_correo(nuevo_correo)
    elif opcion == "3":
        libro1.mostrar_informacion()
        libro2.mostrar_informacion()
        libro3.mostrar_informacion()
    elif opcion == "4":
        prestamo_actual.registrar_prestamo(usuario2, libro1)
    elif opcion == "5":
        prestamo_actual.devolver_libro()
    elif opcion == "0":
        continuar = False
    else:
        print("Opción no válida. Intenta otra vez.")