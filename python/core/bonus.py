""" 
MINI DESAFÍO (nivel core) 
"""



datos = [
   {"nombre": "Carlos", "puntaje": 80},
   {"nombre": "María", "puntaje": 95},
   {"nombre": "Pedro", "puntaje": 70}
]
# 1. Cambiar el puntaje de Pedro a 75
datos[2]["puntaje"] = 75

# 2. Crear función que imprima:
#    "Carlos obtuvo 80 puntos"
def puntaje_carlos(lista):
    for usuario in lista:
        if usuario["nombre"] == "Carlos":
            print(f"{usuario["nombre"]} obtuvo {usuario["puntaje"]} puntos.")

puntaje_carlos(datos)

# 3. Crear función que reciba "nombre" o "puntaje" e imprima solo esos valores
def recibir_nombre_apellido(lista):
    opcion = input("Nombre/Puntaje: ")
    if opcion == "Nombre":
        print("Nombres almacenados:")
        for nombres in lista:
            print(nombres["nombre"])
    elif opcion == "Puntaje":
        print("Puntajes almacenados:")
        for puntajes in lista:
            print(puntajes["puntaje"])
    else:
        print("Ingrese un valor válido")

recibir_nombre_apellido(datos)