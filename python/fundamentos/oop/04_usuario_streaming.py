class UsuarioStreaming:
    def __init__(self, nombre, email, suscripcion="Gratis"):
        self.nombre = nombre
        self.email = email
        self.suscripcion = suscripcion
        self.lista_reproduccion = []

    def agregar_a_lista(self, titulo):
        """Agrega un contenido a la lista de reproducción del usuario."""
        self.lista_reproduccion.append(titulo)
        print(f'El video "{titulo}" fué agregado correctamente.')


    def ver_contenido(self, titulo):
        """Simula que el usuario reproduce un contenido."""
        if titulo in self.lista_reproduccion:
            print(f"Usuario {self.nombre} está viendo: {titulo}")
        else:
            print(f'Título "{titulo}" no encontrado . . .')


    def cambiar_suscripcion(self, nueva_suscripcion):
        """Cambia el tipo de suscripción del usuario."""
        

    def mostrar_info_usuario(self):
        """Muestra la información del usuario y su lista de reproducción."""
        pass

def crearUsuario():
    nombre = input("Ingresa el nombre de usuario: ")
    email = input("Ingresa una dirección de gmail: ")
    while '@gmail.com' not in email:
        print("Asegurate de usar una cuenta de Google")
        email = input("Ingresa una dirección de GMAIL: ")
    return UsuarioStreaming(nombre, email)
usuario = crearUsuario()

def anadirVideo():
    repro = input("Ingresa el nombre del video: ")
    usuario.agregar_a_lista(repro)
    return repro

continuar = True
while continuar:
    print("\n---Ejercicios Python ---")
    print("--- 1. Agragar a lista ---")
    print("--- 2. Ver video---")
    print("--- 3. Cambiar suscripción ---")
    print("--- 4. Mostrar info ---")
    opcion = input("\n---Elije una opción: (1-4) (0 para salir)")
    if opcion == "1":
        print("\nEjecutando 1era instrucción: ")
        anadirVideo()
    elif opcion == "2":
        print("\nEjecutando 2da instrucción: ")
        usuario.ver_contenido()
    elif opcion == "3":
        print("\nEjecutando 3era instrucción: ")
        
    elif opcion == "4":
        print("\nEjecutando 4ta instrucción: ")
        
    elif opcion == "0":
        print("Saliendo...")
        continuar = False
    else:
        print("Opción no válido. Intenta otra vez.")





