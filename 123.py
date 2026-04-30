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
    for i in texto[i]:
        

    

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



# 5. Crear una función que reciba una lista de precios de productos y aplique un descuento del 10%, mostrando el valor original y el nuevo valor.
def mostrarDescuento(productos, precios):
    descuento = 0.1
    conDescuento = []
    for i in range(len(productos)):
        valor = precios[i] * (1 - descuento)
        conDescuento.append(valor)
        print(f"Producto: {productos[i]}\nPrecio original: ${precios[i]}\nPrecio con descuento: ${conDescuento[i]}")

def recibirProductos():
    cantidad = int(input("Ingrese la cantidad de productos: "))
    listaProductos = []
    listaPrecios = []
    for i in range(cantidad):
        producto = input(f"{i + 1}. ")
        listaProductos.append(producto)
        precio = int(input(f"Ingrese el valor de {producto}: "))
        listaPrecios.append(precio)
    mostrarDescuento(listaProductos, listaPrecios)



# 6. Crear una función que reciba un número entero y determine si es par o impar.
def parImpar(numero):
    if numero % 2 == 0:
        print(f"El número {numero} es Par.")
    elif numero % 3 == 0:
        print(f"El número {numero} es Impar.")

def recibirNum():
    num = int(input("Ingrese un número: "))
    parImpar(num)



# 7. Crear una función que reciba una lista de edades y muestre cuántas personas son mayores de edad (18 años o más).
def mayoresEdad(edades):
    mayoresEdad = 0
    for i in range(len(edades)):
        if edades[i] >= 18:
            mayoresEdad += 1
    print(f"En la lista de edades {mayoresEdad} personas son mayores de edad.")

def recibirEdades():
    cantidad = int(input("Ingrese la cantidad de edades: "))
    listaEdades = []
    for i in range(cantidad):
        edad = int(input(f"Edad N°{i +1}: "))
        listaEdades.append(edad)
    mayoresEdad(listaEdades)



# 8. Crear una función que reciba una lista de palabras y permita buscar cuántas veces aparece una palabra específica ingresada por el usuario.
def vecesAparece(palabras):
    buscar = input("Ingresa la palabra que deseas buscar: ")
    cantidadEncontrada = 0
    for i in range(len(palabras)):
        if buscar == palabras[i]:
            cantidadEncontrada += 1
    print(f"La palabra {buscar} ah sido encontrada {cantidadEncontrada} veces en la lista de palabras.")

def recibirPalabras():
    cantidad = int(input("Ingrese la cantidad de palabras: "))
    listapalabras = []
    for i in range(cantidad):
        palabra = input(f"{i + 1}. ")
        listapalabras.append(palabra)
    vecesAparece(listapalabras)



# 9. Crear una función que reciba una lista de números y genere una nueva lista que contenga únicamente los números positivos.
def numsPositivos(numeros):
    positivos = 0
    lista = []
    for i in range(len(numeros)):
        if numeros[i] > 0:
            positivos += 1
            lista.append(numeros[i])
    print(f"LA lista enviada tiene {positivos} números positivos:\n{lista}")

def recibirNums2():
    cantidad = int(input("Cantidad de números a ingresar: "))
    cadena = []
    for i in range(cantidad):
        num = int(input(f"{i + 1}. "))
        cadena.append(num)
    numsPositivos(cadena)



# 10. Crear una función que reciba una lista de productos (utilizando diccionarios con nombre y stock) y muestre cuáles tienen un stock menor a 5 unidades.
