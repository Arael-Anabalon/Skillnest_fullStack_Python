# 1. Crear una función que reciba una lista de números enteros y muestre cuál es el número mayor y cuál es el menor.
def mayor_menor(numeros):
    numMenor = min(numeros)
    numMayor = max(numeros)
    print(f"Número mayor: {numMayor}\nNúmero menor: {numMenor}")

def recibirNums():
    cantidad = int(input("Cantidad de números a ingresar: "))
    cadena = []
    for i in range(cantidad):
        num = int(input(f"{i + 1}. "))
        cadena.append(num)
    mayor_menor(cadena)


# 2. Crear una función que reciba una cadena de texto y cuente cuántas vocales contiene.
def devolverVocales(texto):
    vocales = "aeiouAEIOU"
    

def recibirCadena():
    cadena = input("Ingrese una palabra: ")
    devolverVocales(cadena)



# 3. Crear una función que reciba una lista de nombres y muestre únicamente aquellos que tengan más de 5 letras.
def mas5letras(nombres, cantidad):
    mas5letras = []
    for i in range(cantidad):
        if len(nombres[i]) > 5:
            mas5letras.append(nombres[i])
    print(f"Nombres con más de 5 letras:\n{mas5letras}")

def ingresarNombres():
    cantidad = int(input("Cantidad de nombres a ingresar: "))
    listaNombres = []
    for i in range(cantidad):
        nombre = input(f"{i + 1}.")
        listaNombres.append(nombre)
    mas5letras(listaNombres, cantidad)



# 4. Crear una función que reciba una lista de notas (números decimales), calcule el promedio e indique si el estudiante aprueba (promedio mayor o igual a 4.0).
def calcularPromedio(notas):
    promedio = sum(notas) / len(notas)
    print(f"Promedio general del estudiante: {promedio}")
    return promedio

def aprobadoReprobado(promedio, nombre):
    if promedio >= 4.0:
        print(f"El estudiante {nombre} aprobó con un promedio general de {promedio}")
    elif promedio < 4.0:
        print(f"El estudiante {nombre} reprobó con un promedio general de {promedio}")
    else:
        print("Error")

def recibirNotas():
    estudiante = input("Ingrese el nombre del estudiante: ")
    cantidad = int(input("Ingresa la cantidad de notas a ingresar: "))
    listaNotas = []
    for i in range(cantidad):
        nota = float(input(f"Ingrese la nota N°{i + 1} de {estudiante}: "))
        listaNotas.append(nota)
    promedioFinal = calcularPromedio(listaNotas)
    aprobadoReprobado(promedioFinal, estudiante)

recibirNotas()