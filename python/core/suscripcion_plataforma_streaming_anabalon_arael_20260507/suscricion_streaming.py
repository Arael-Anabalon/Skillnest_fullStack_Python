class SuscripcionStreaming:
    costos_suscripcion = {"Gratis": 0, "Estándar": 5.99, "Premium": 10.99}

    def __init__(self, usuario, tipo_suscripcion = "Gratis"):
        self.usuario = usuario
        self.tipo_suscripcion = tipo_suscripcion
        self.costo_mensual = self.costos_suscripcion[tipo_suscripcion]
        self.saldo_pendiente = 0

        self.saldo_pendiente += self.costo_mensual # <-- Simular cobro mensual

    def realizar_pago(self, monto):
        """Reduce el saldo pendiente según el monto pagado."""
        pass

    def cambiar_suscripcion(self, nuevo_tipo):
        """Cambia el tipo de suscripción y actualiza el costo mensual."""
        if nuevo_tipo not in self.costos_suscripcion:
            print("Tipo de suscripción inválido!")

    def ver_contenido_exclusivo(self):
        """Permite ver contenido exclusivo según el tipo de suscripción."""
        if self.tipo_suscripcion == "Gratis":
            print(f"Este contenido requiere suscripcion Estándar o superior...")
            cambiarSuscripcion = input('Desea cambiar su tipo de suscripción?(S/N): ')
            if cambiarSuscripcion == "S":
                print(f'1. Gratis(Tienes): ${self.costos_suscripcion["Gratis"]}/mes\n2. Estándar: ${self.costos_suscripcion["Estándar"]}\n3. Premium: ${self.costos_suscripcion["Premium"]}')
                nuevoTipo = input("Ingrese una opción(Escríbelo): ")
                self.cambiar_suscripcion(nuevoTipo)
            else:
                print("Ok")
        else:
            print(f"Reproduciendo contenido exclusivo...")

    def mostrar_info_suscripcion(self):
        """Muestra la información de la suscripción del usuario."""
        print(f"Mostrando información de {self.usuario}:")
        print(f"Tipo de suscripción: {self.tipo_suscripcion}\nCosto mensual: ${self.costo_mensual}\nSaldo pendiente: ${self.saldo_pendiente}")