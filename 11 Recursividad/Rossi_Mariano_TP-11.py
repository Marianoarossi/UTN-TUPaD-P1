"""1) Crea una función recursiva que calcule el factorial de un número. Luego, 
utiliza esa función para calcular y mostrar en pantalla el factorial de todos los
números enteros entre 1 y el número que indique el usuario"""

def factorial(num):
    # caso base
    if num == 0:
        return 1
    else:
        # Si no, multiplico el número por el factorial del número anterior
        return num * factorial(num - 1)

# Pido al usuario que ingrese un número entero
numero = int(input("Ingrese un número entero: "))

# Uso un for para calcular el factorial de cada número desde 1 hasta el ingresado
for i in range(1, numero + 1):
    print(f"El factorial de {i} es {factorial(i)}")



"""
2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada.
Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.
"""
def fibonacci(num):
    #CASO BASE Si el número es 0 o 1, devuelvo el mismo número 
    if num <= 1:
        return num
    else:
        # Por lo contrario sumo los dos valores anteriores (llamadas recursivas)
        return fibonacci(num - 1) + fibonacci(num - 2)

def mostrar_fibonacci(posicion):
    for i in range(posicion + 1):
        # Muestro cada valor de la serie en la misma línea
        print(fibonacci(i), end=" ")

# Pido al usuario que indique hasta qué posición mostrar la serie
posicion = int(input("Ingrese la posición de la serie de Fibonacci que desea mostrar: "))
mostrar_fibonacci(posicion)

"""3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente,
utilizando la fórmula 𝑛𝑚= 𝑛∗𝑛(𝑚−1). Prueba esta función en un algoritmo general."""

def potencia(base, exponente):
    # Caso base: si el exponente es 0, devuelvo 1
    if exponente == 0:
        return 1
    else:
        # Multiplico la base por el resultado de la misma base con un exponente menos
        return base * potencia(base, exponente - 1)

# Pido los datos al usuario
base = int(input("Ingrese la base positiva : "))
exponente = int(input("Ingrese el exponente positivo : "))

# Llamo a la función y muestro el resultado
resultado = potencia(base, exponente)
print(f"{base} elevado a la {exponente} es igual a {resultado}")

""" 4)_Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva 
su representación en binario como una cadena de texto."""
def decimal_a_binario(n):
    #CASO BASE. Si el número es menor que 2, devuelvo el mismo número como string 
    if n < 2:
        return str(n)
    else:
        # Divido el número por 2 y concateno el resto al final
        return decimal_a_binario(n // 2) + str(n % 2)

# Pido un número al usuario
numero = int(input("Ingrese un número entero positivo en base decimal: "))

# Verifico que el número sea válido (positivo)
if numero < 0:
    print("El número ingresado no es válido. Debe ser positivo.")
else:
    # Llamo a la función y muestro el binario
    binario = decimal_a_binario(numero)
    print(f"El número {numero} en binario es: {binario}")