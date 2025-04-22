"""1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea."""
for i in range(101):
    print(i) #imprimo los numeros del 0 al 100


"""2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene."""

num= int(input("Ingrese un número entero: "))
cantidadDigitos= len(str(num)) #utilizo la funcion len para que me devuelva la cantidad de digitos almacenados en el string
print(f"La cantidad de digitos de {num} es {cantidadDigitos}.")

"""3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores."""

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
suma = 0
for i in range(num1 + 1, num2):
    suma += i
#imprimo la suma de los numeros comprendidos entre los dos numeros dados por el usuario
print(f"La suma de los números comprendidos entre {num1} y {num2} es {suma}.") 




"""4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0."""
suma=0 #Inicializo la variable suma en 0
#almaceno el valor ingresado por el usuario en la variable num , convirtiendola en un número entero
num= int(input("Ingrese un número entero (0 para salir): ")) 
while num>0:  #Bucle con validacion, solo ingresara si el número es mayor a 0
    suma += num #sumo el valor de num
    #vuelvo a pedir un nuevo numero para la siguiente vuelta
    num = int(input("Ingrese un número entero (0 para salir): "))
#Imprimo el resultado de la suma de números ingresados.
print("El total acumulado es:", suma)


"""5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número."""

import random  # Importa el módulo random para generar números aleatorios

numero_aleatorio = random.randint(0, 9)  # Genera un número entero aleatorio entre 0 y 9, ambos incluidos
cont = 0  # Inicializó el contador de intentos en 0
num = -1  # Inicializó num con un valor fuera del rango para asegurarse de que el bucle se ejecute al menos una vez

while num != numero_aleatorio:  # Inicio un bucle que se ejecute mientras num no sea igual a numero_aleatorio
    num = int(input("Adivina el número (entre 0 y 9): "))  # Solicito al usuario que ingrese un número y lo convierto a entero
    cont += 1  # Incremento el contador de intentos en 1

    if num < 0 or num > 9:  # Verifico si el número ingresado está fuera del rango de 0 a 9
        print("Por favor, ingresa un número entre 0 y 9.")  # Muestro un mensaje si el número está fuera del rango
    elif num == numero_aleatorio:  # Verifico si el número ingresado es igual al número aleatorio
        print(f"¡Felicidades! Adivinaste el número en {cont} intentos.")
        
        
"""6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente."""
for i in range(100,0,-1):
    if i%2==0:
        print(i)

"""7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario."""
num = int(input("Introduce un número entero positivo: "))
suma = 0
for i in range(0, num + 1):
    suma += i
print("La suma de todos los números comprendidos entre 0 y", num, "es:", suma)

"""7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario. Comenta luego de cada instrucción que hace el codigo"""
numero = int(input("Introduce un numero: ")) #solicito un número al usuario y lo convierto a entero
suma = 0 
for i in range(0, numero + 1):  # Inicio un bucle que va desde 0 hasta numero inclusive
    suma = suma + i  # Sumo el valor de i a la variable suma en cada vuelta del bucle
print("La suma de todos los numeros comprendidos entre 0 y ", numero, " es: ", suma) 
# Imprimo el resultado de la suma de todos los números desde 0 hasta numero

"""8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio)."""
pares = 0
impares = 0
negativos = 0
positivos = 0
for i in range(100):
    numero = int(input("Ingrese un número: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero < 0:
        negativos += 1
    else:
        positivos += 1
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
print("Cantidad de números negativos:", negativos)
print("Cantidad de números positivos:", positivos)


"""9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor)."""
suma = 0
for i in range(100):
    num = int(input("Ingrese un numero: "))
    suma += num
print("La media de los 100 numeros es: ", suma/100)

"""10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. sin usar funciones"""
# Solicito al usuario que ingrese un número
numero = input("Ingrese un número: ")
# Inicializo variable para almacenar el número invertido
invertido = ""
#Uso len para contar los caracteres y recorrer la cadena desde el último hasta el primero
for i in range(len(numero) - 1, -1, -1): 
    invertido += numero[i]
# Muestro el número invertido
print("El número invertido es:", invertido)