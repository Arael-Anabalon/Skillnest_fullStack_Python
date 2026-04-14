# 1. Números Pares Dinámicos
def paresDinamicos():
    pares = int(input("Cuantos números pares desea ver? "))
    for i in range(1, pares + 1):
        print(i * 2)



# 2. Verificador de Edad y Acceso
def verificadorEdad():
    anioNAcimiento = int(input("Anio de nacimiento: "))
    calculoEdad = 2026 - anioNAcimiento
    if calculoEdad >= 18:
        print(f"Eres mayor de edad, tienes {calculoEdad} anios")
    elif calculoEdad < 18:
        print(f"Eres menor de edad, tienes {calculoEdad} anios")
    else:
        print("Error")



# 3. Calculadora de Descuentos
def calculadoraDescuentos():
    precioProducto = int(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad de unidades compradas: "))
    total = precioProducto * cantidad
    descuento = 0
    final = 0
    if (total > 100):
        descuento = total * (10 / 100)
        final = total - descuento
        print(f"Total: {total}\nDescuento: {descuento}\nFinal: {final}")



# 4. Clasificador de Números
def clasificadorNum():
    num = int(input("Ingrese un número: "))
    if (num > 0):
        if (num % 2 == 0):
            print(f"El número {num} es Positivo y Par")
        elif (num % 2 == 1):
            print(f"El número {num} es Positivo e Impar")
    elif (num < 0):
        if (num % 2 == 0):
            print(f"El número {num} es Negativo y Par")
        elif (num % 2 == 1):
            print(f"El número {num} es Negativo e Impar")



# 5. Tabla de Multiplicar Personalizada
def tablaPresonalizada():
    num = int(input("Ingresa un número: "))
    for i in range(1, 13):
        resultado = num * i
        if (resultado % 3 == 0):
            print(f"{num} * {i} = {resultado}")



# 6. Sumatoria con Centinela
def sumatoriaCentinela():
    sumaTotal = 0
    while True:
        num = int(input("Ingresa un número: "))
        if num < 0:
            break
        sumaTotal += num
        print(f"Suma total: {sumaTotal}")



# 7. Contador de Vocales
def contadorVocales():
    texto = input("Ingresa una palabra o frase: ").lower()
    vocales = 0
    for i in range(len(texto)):
        if texto[i] == "a" or texto[1] == "e" or texto[1] == "i" or texto[1] == "o" or texto[1] == "u":
            vocales += i
        elif texto[i] == "á" or texto[i] == "é" or texto[i] == "í" or texto[i] == "ó" or texto[i] == "ú":
            vocales += i
    print(f"La cadena {texto} tiene : {vocales} en total")



# 8. Validación de Contraseña
def validadorPassword():
    password = "a1b2c3"
    intentos = 3
    for i in range(intentos):
        passIngresada = input("Ingresa la contraseña: ")
        if passIngresada == password:
            print(f"Contraseña correcta, {intentos}/3 restantes")
            break
        else:
            intentos -= 1
            print(f"Contraseña incorrecta, {intentos}/3 restantes")



# 9. Registro de Nombres
def registroNombres():
    nombres = []
    print("Por favor, ingresa 5 nombres")
    for i in range(5):
        nombre = input(f"Nombre N°{i + 1}: ")
        if nombre != "":
            nombres.append(nombre)
        else:
            print("Tienes que ingresar un nombre.")
    print(reversed(nombres))



# 10. Promedio de Notas
def promedioNotas():
    cantidad = int(input("Cuantas notas desea ingresar?: "))
    sumaNotas = 0
    for i in range(cantidad):
        notas = int(input(f"Ingrese la nota N°{i}: "))
        sumaNotas += notas
    promedio = sumaNotas / cantidad
    print(f"Notas ingresadas: {cantidad} \nPromedio: {promedio}")



# 11. Filtro de Arreglos
def filtroArrays():
    cantidad = int(input("Cuantos valores desea ingresar?: "))
    valores = []
    mayor50 = []
    for i in range(cantidad):
        valores = int(input(f"Ingrese el valor N°{i}: "))
        if valores > 50:
            mayor50.append(valores)
    print(f"Cantidad de valores: {cantidad} \nValores mayor a 50: {mayor50}")



# 12. Buscador de Elementos
def buscadorElemento():
    ciudades = ["Miami", "Lima", "Tokio", "París", "Nueva York", "Roma", "Buenos Aires", "Estambul", "Kioto", "Londres"]
    ciudad = input("Ingresar ciudad (con mayus al principio): ").capitalize()
    esta = ciudades.index(ciudad)
    if esta < int(ciudades):
        print(f"Tu ciudad esta en el arreglo, en la posicion {esta}")
    else:
        print("Tu ciudad no esta en el arreglo.")



# 13. Simulación de Inventario
def simuladorInv():
    nombreProductos = []
    precioProductos = []
    for i in range(3):
        nombre = input("Nombre del producto: ")
        precio = float(input("Precio: "))
        nombreProductos.append(nombre)
        precioProductos.append(precio)
    print("\nInventario: ")
    for i in range(3):
        print(f"Producto: {nombreProductos[i]}, precio ${precioProductos[i]}")



# 14. Generador de Lista de Compras
def listaCompras():
    lista = []
    while True:
        item = input("Articulo (o 'terminar': )")
        if item.lower() == "terminar":
            break
        lista.append(item)
    print(f"Ordenada: {sorted(lista)}")



# 15. Análisis de Temperaturas
def analisisTemp():
    diasSemana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    tempDias = []
    tempMayor25 = 0
    sumaTemps = 0
    for i in range(len(diasSemana)):
        temperatura = int(input(f"Ingresa la temperatura del día {diasSemana[i]}: "))
        tempDias.append(temperatura)
        sumaTemps += temperatura
        if temperatura > 25:
            tempMayor25 += 1
        sumaTemps += temperatura
    promedio = sumaTemps / len(diasSemana)
    minTemp = min(tempDias)
    minTempIndex = tempDias.index(minTemp)
    minTempDia = diasSemana[minTempIndex]
    print(f"Promedio semanal: {promedio}°")
    print(f"Cantidad de días con temperatura sobre 25°: {tempMayor25}")
    print(f"Día con la temperatura mas baja: {minTempDia}, con {minTemp}°")



continuar = True
while continuar:
    print("\n---Ejercicios Python---")
    print("---Ejercicio 1---")
    print("---Ejercicio 2---")
    print("---Ejercicio 3---")
    print("---Ejercicio 4---")
    print("---Ejercicio 5---")
    print("---Ejercicio 6---")
    print("---Ejercicio 7---")
    print("---Ejercicio 8---")
    print("---Ejercicio 9---")
    print("---Ejercicio 10---")
    print("---Ejercicio 11---")
    print("---Ejercicio 12---")
    print("---Ejercicio 13---")
    print("---Ejercicio 14---")
    print("---Ejercicio 15---")
    opcion = input("\n---Elije una opción: (1-15) (0 para salir)")
    if opcion == "1":
        print("\nEjecutar ejercicio 1: ")
        paresDinamicos()
    elif opcion == "2":
        print("\nEjecutar ejercicio 2: ")
        verificadorEdad()
    elif opcion == "3":
        print("\nEjecutar ejercicio 3: ")
        calculadoraDescuentos()
    elif opcion == "4":
        print("\nEjecutar ejercicio 4: ")
        clasificadorNum()
    elif opcion == "5":
        print("\nEjecutar ejercicio 5: ")
        tablaPresonalizada()
    elif opcion == "6":
        print("\nEjecutar ejercicio 6: ")
        sumatoriaCentinela()
    elif opcion == "7":
        print("\nEjecutar ejercicio 7: ")
        contadorVocales()
    elif opcion == "8":
        print("\nEjecutar ejercicio 8: ")
        validadorPassword()
    elif opcion == "9":
        print("\nEjecutar ejercicio 9: ")
        registroNombres()
    elif opcion == "10":
        print("\nEjecutar ejercicio 10: ")
        promedioNotas()
    elif opcion == "11":
        print("\nEjecutar ejercicio 11: ")
        filtroArrays()
    elif opcion == "12":
        print("\nEjecutar ejercicio 12: ")
        buscadorElemento()
    elif opcion == "13":
        print("\nEjecutar ejercicio 13: ")
        simuladorInv()
    elif opcion == "14":
        print("\nEjecutar ejercicio 14: ")
        listaCompras()
    elif opcion == "15":
        print("\nEjecutar ejercicio 15: ")
        analisisTemp()
    elif opcion == "0":
        print("Saliendo...")
        continuar = False
    else:
        print("Opción no válido. Intenta otra vez.")