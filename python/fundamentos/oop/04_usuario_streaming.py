class UsuarioStreaming:
    def __init__(self, nombre, email, suscripcion="Gratis"):
        self.nombre = nombre
        self.email = email
        self.suscripcion = suscripcion
        self.lista_reproduccion = []


    def agregar_a_lista(self, titulo):
        """Agrega un contenido a la lista de reproducción del usuario."""
        self.lista_reproduccion.append(titulo)
        print(usuario1.lista_reproduccion)

    def ver_contenido(self, titulo):
        """Simula que el usuario reproduce un contenido."""

        pass

    def cambiar_suscripcion(self, nueva_suscripcion):
        """Cambia el tipo de suscripción del usuario."""
        pass

    def mostrar_info_usuario(self):
        """Muestra la información del usuario y su lista de reproducción."""
        pass

usuario1 = UsuarioStreaming("Ara", "araelanabalon@liceovvh.cl")

reproducciones = []
def agregarRepro():
    cantidad = int(input("Cuantos títulos desea agregar?: "))
    for i in range(cantidad):
        nuevaReproduccion = input("Ingrese nueva reproducción: ")
        reproducciones.append(nuevaReproduccion)
    usuario1.agregar_a_lista(reproducciones)
agregarRepro()
def verRepro():

    pass

