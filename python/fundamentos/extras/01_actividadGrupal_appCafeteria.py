class CafeteriaCliente:
    costosMembrecia = {"Bronce": 0, "Plata": 1000, "Oro": 2500}

    def __init__(self, usuario, membrecia="Bronce"):
        self.nombre = usuario
        self.tipoMembrecia = membrecia
        self.puntosAcumulados = 0
        self.saldoPendiente = 0
        self.totalClientes = 0

        CafeteriaCliente.totalClientes += 1

    def realizar_compra(self, monto):
        # Aumentar saldo pendiente
        self.saldoPendiente += monto
        # Acumular puntos
        puntosNuevos = (self.saldoPendiente // 1000) * 10
        self.puntosAcumulados += puntosNuevos
        print(f"{self.nombre} realizó una compra.")

    def pagar_saldo(self, monto):
        if monto > self.saldoPendiente:
            print(f"ERROR: No puedes pagar ${monto}, porque tu deuda es de solo ${self.saldoPendiente}")
        elif monto <= 0:
            print("ERROR: El monto deve ser mayor a $0")
        else:
            self.saldoPendiente -= monto
            print(f"Pago de ${monto} realizado correctamente!\nSaldo restante: ${self.saldoPendiente}.")
        
    @classmethod
    def mostrar_total_clientes(cls):
        print(f"Total de clientes registrados: {cls.totalClientes}")


   
