def multiplicacion(num1, num2): #definimos la función multiplación con los parámetros num1 y num2
   resultado = num1 * num2     #instrucciones dentro de la función
   return resultado            #regresamos valor de resultado

resultado_multiplicacion = multiplicacion(5, 5) #Llamado a la función con argumentos 5 y 5
print(resultado_multiplicacion) #Se guarda en la variable el resultado que la función regresó. Imprime: 25



""" Parámetros y argumentos """
# Los parámetros son las entradas que tendremos ante nuestra función.
# Las funciones pueden tener tantos parámetros como se necesite, incluso pueden no tener parámetros de entrada.
# Mira el siguiente ejemplo, en donde definimos una función llamada buenos_dias que recibe el parámetro nombre:
def buenos_dias(nombre):
   print("Buenos días " + nombre)

# Una vez definida la función, podemos invocarla llamándola por su nombre y enviando la cantidad de argumentos requeridos:
buenos_dias("alegría")
buenos_dias("al amor")
buenos_dias("a la vida")
buenos_dias("señor Sol")



""" Devolución de valores """
# En muchas ocasiones para nuestro desarrollo necesitaremos que dicha función nos regrese algún tipo de valor para poder ser utilizado más adelante en nuestro desarrollo.
# Para esto utilizaremos la sentencia return, esta me va a permitir devolver un valor ante la llamada a mi función.

# Esto va a significar que la llamada a una función será igual a lo que dicha función regrese. ¡Veámoslo trabajar!
# Intentemos hacer algunos cambios para la función buenos_dias:
def buenos_dias(nombre):
   return "Buenos días " + nombre

#El valor de retorno de la función es "Buenos días Python", por lo que el valor de mi variable frase será ese
frase = buenos_dias("Python")
print(frase) #Imprime: Buenos días Python

# Almacenar estos valores de retorno en variables nos permite usar los resultados de nuestras funciones en el resto de nuestro programa.
# Las funciones pueden devolver cualquier tipo de datos: cadenas, números, listas, tuplas, diccionarios inclusive otras funciones.



""" Ejercicios """
# 1. Ejercicio de retorno de valor:
def construirFrase(nombre, comida):
   return f"{nombre} come {comida}"

nombre = input("Ingrese un nombre: ")
comida = input("Ingrese una comida: ")
resultado = construirFrase(nombre, comida)
print(resultado)
