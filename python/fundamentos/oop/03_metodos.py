class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = 30000
        self.saldo_pagar = 0
    def hacer_compra(self, monto):  #recibe como argumento el monto de la compra
        self.saldo_pagar += monto   #el saldo a pagar del usuario aumenta en la cantidad del valor recibido
    def aumentar_credito(self, nuevo_credito):
        self.limite_credito = nuevo_credito
    def cambiar_correo(self, nuevo_email):
        self.email = nuevo_email
    
miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la")
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la")

miyagi.hacer_compra(2000)
print(f"Primera compra: ${miyagi.saldo_pagar}")
miyagi.hacer_compra(300)
print(f"Segunda compra: ${miyagi.saldo_pagar}")
print(f"Creadito disponible: ${miyagi.limite_credito - miyagi.saldo_pagar}")
daniel.hacer_compra(45)
print(miyagi.saldo_pagar) #Imprime: 350
print(daniel.saldo_pagar) #Imprime: 45

"""
1. Crear un nuevo método que permita aumentar el límite de crédito.
- Imprimir el nuevo límite de crédito 
"""
nuevoCredito = int(input("Ingrese nuevo credito: "))
miyagi.aumentar_credito(nuevoCredito)
print(miyagi.limite_credito)
"""
2. Crear un nuevo método que permita cambiar el correo de la instancia.
- Mostrar el nuevo correo.
"""
nuevoCorreo = input("Ingrese un nuevo correo: ")
miyagi.cambiar_correo(nuevoCorreo)
print(miyagi.email)