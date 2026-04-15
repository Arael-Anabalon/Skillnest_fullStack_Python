# 1. Generador de niveles
def generadorNiveles():
    for i in range(101):
        print(i)


# 2. Potenciadores de energía (Múltiplos)
def potenciadoresEnergia():
    for i in range(2, 501, 2):
        print(i)


# 3. Trampa de emojis
def trampaEmojis():
    for i in range(1, 101):
        if i % 10 == 0:
            print("😃")
        elif i % 5 == 0:
            print("😆")


# 4. Suma colosal
def sumaColosal():
    print("WIP")


# 5. Retroceso temporal
def retrocesoTemporal():
    for anio in range(2024, -2, -3):
        print(f"Año: {anio}")


# 6. Contador dinámico
def contadorDinamico():
    inicio = 3
    fin = 10
    salto = 2
    for nivel in range(inicio, fin + 1):
        if nivel % salto == 0:
            print(nivel)

continuar = True
while continuar:
    print("\n---Ejercicios Python---")
    print("---Ejercicio 1---")
    print("---Ejercicio 2---")
    print("---Ejercicio 3---")
    print("---Ejercicio 4---")
    print("---Ejercicio 5---")
    print("---Ejercicio 6---")
    opcion = input("\n---Elije una opción: (1-6) (0 para salir)")
    if opcion == "1":
        print("\nEjecutar ejercicio 1: ")
        generadorNiveles()
    elif opcion == "2":
        print("\nEjecutar ejercicio 2: ")
        potenciadoresEnergia()
    elif opcion == "3":
        print("\nEjecutar ejercicio 3: ")
        trampaEmojis()
    elif opcion == "4":
        print("\nEjecutar ejercicio 4: ")
        sumaColosal()
    elif opcion == "5":
        print("\nEjecutar ejercicio 5: ")
        retrocesoTemporal()
    elif opcion == "6":
        print("\nEjecutar ejercicio 6: ")
        contadorDinamico()
    elif opcion == "0":
        print("Saliendo...")
        continuar = False
    else:
        print("Opción no válido. Intenta otra vez.")