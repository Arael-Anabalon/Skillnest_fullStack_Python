"""
Funciones básicas 2
"""

# Calcula experiencia
def multiplica_por_2(numLimite):
    pares = []
    for i in range(numLimite):
        pares.append(i * 2)
    return pares
        

multiplica_por_2(5)
# Debe retornar: [0, 2, 4, 6, 8, 10]





# Analiza publicaciones
def suma_y_resta(num1, num2):
    print(num1 + num2)
    return num1 - num2

suma_y_resta([120, 115])
# Imprime: 235 y retorna: 5





# Puntaje ajustado
def sumatoria_menos_longitud(valores):
    for i in range(len(valores)):
        sumaTotal += valores[i]
    longitud = valores[i]
    return sumaTotal - longitud

sumatoria_menos_longitud([10, 5, 3, 7])
# Suma total = 25, longitud = 4, debe retornar: 21





# Ajusta visualizaciones
def valores_multiplicados_segundo(valores):
    for i in range(len(valores)):
        por3 = valores[i] * 3
    cantidadValores = len(valores)
    print(cantidadValores)
    return por3

valores_multiplicados_segundo([100, 3, 50, 20])
# Imprime: 4 y retorna: [300, 9, 150, 60]

valores_multiplicados_segundo([100])
# Imprime: 1 y retorna: []





# Genera precio fijo
def valor_multiplicado_logitud(num1, num2):
    

valor_multiplicado_longitud(5, 2)
# Debe retornar: [10, 10]

valor_multiplicado_longitud(7, 5)
# Debe retornar: [35, 35, 35, 35, 35]
