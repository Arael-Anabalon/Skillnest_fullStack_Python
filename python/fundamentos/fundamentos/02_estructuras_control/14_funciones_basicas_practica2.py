"""
Funciones básicas 2
"""

# 1. Calcula experiencia
def multiplica_por_2(numLimite):
    pares = []
    for i in range(numLimite + 1):
        pares.append(i * 2)
    return pares
# Debe retornar: [0, 2, 4, 6, 8, 10]





# 2. Analiza publicaciones
def suma_y_resta(nums):
    print(nums[0] + nums[1])
    return nums[0] - nums[1]
# Imprime: 235 y retorna: 5





# 3. Puntaje ajustado
def sumatoria_menos_longitud(valores):
    sumaTotal = 0
    for i in range(len(valores)):
        sumaTotal += valores[i]
    longitud = len(valores)
    return sumaTotal - longitud
# Suma total = 25, longitud = 4, debe retornar: 21





# 4. Ajusta visualizaciones
def valores_multiplicados_segundo(valores):
    retorno = []
    cantidadValores = len(valores)
    print(cantidadValores)
    for i in range(cantidadValores):
        if cantidadValores <= 1:
            retorno = []
        else:
            retorno.append(valores[i] * 3)
    return retorno 
# Imprime: 4 y retorna: [300, 9, 150, 60]
# Imprime: 1 y retorna: []





# 5. Genera precio fijo
def valor_multiplicado_longitud(num1, num2):
    retorno = num1 * num2
    return [retorno] * num2
# Debe retornar: [10, 10]
# Debe retornar: [35, 35, 35, 35, 35]





continuar = True
while continuar:
    print("\n---Ejercicios Python---")
    print("---Ejercicio 1---")
    print("---Ejercicio 2---")
    print("---Ejercicio 3---")
    print("---Ejercicio 4---")
    print("---Ejercicio 5---")
    opcion = input("\n---Elije una opción: (1-5) (0 para salir)")
    if opcion == "1":
        print("\nEjecutar ejercicio 1: ")
        print(multiplica_por_2(5))
    elif opcion == "2":
        print("\nEjecutar ejercicio 2: ")
        print(suma_y_resta([120, 115]))
    elif opcion == "3":
        print("\nEjecutar ejercicio 3: ")
        print(sumatoria_menos_longitud([10, 5, 3, 7]))
    elif opcion == "4":
        print("\nEjecutar ejercicio 4: ")
        print(valores_multiplicados_segundo([100, 3, 50, 20]))
        print(valores_multiplicados_segundo([100]))
    elif opcion == "5":
        print("\nEjecutar ejercicio 5: ")
        print(valor_multiplicado_longitud(5, 2))
        print(valor_multiplicado_longitud(7, 5))
    elif opcion == "0":
        print("Saliendo...")
        continuar = False
    else:
        print("Opción no válido. Intenta otra vez.")