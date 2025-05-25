""" 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”."""

edad= int(input("Ingrese su edad: "))
if edad >= 18: # Inicio una condicional para realizar la comparación de la edad 
    print("Es mayor de edad") 
else: #si la edad es mayor o igual mostrara esta opción
    print("No es mayor de edad")

""" 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
mensaje “Desaprobado”."""

nota = int(input("Ingrese su nota: ")) #convierto la nota en entero y la guardo en una variable
if nota >=6: #abro un condicional y evaluo si la nota es mayor o igual a 6
    print("Aprobado")
else:
    print("Desaprobado")

"""3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
operador de módulo (%) en Python para evaluar si un número es par o impar."""
numero = int(input("Ingrese un numero par: "))
if numero % 2 == 0: #evaluo si el nro es dibisible por 2 quiere decir que es par
    print(f"Ha ingresado el numero {numero}, que es par")
else:
    print(f"El número {numero}, no es par")

"""4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
siguientes categorías pertenece:
● Niño/a: menor de 12 años.
● Adolescente: mayor o igual que 12 años y menor que 18 años.
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
● Adulto/a: mayor o igual que 30 años."""
edad= int(input("Ingrese su edad:"))
if edad <=12 : #comparo si la edad es menor o igual a 12
    print("Niño/a")
elif edad >= 12 and edad < 18: #comparo si la edad mayor o igual  a 12 ademas si eso es correcto y la edad es menor a 18, imprimo la opción
    print("Adolescente")
elif edad >=18 and edad <30:#comparo edad sea mayor o igual a 18 y que sea menor a 30 
    print("Adulto/a joven")
else:
    edad >= 30 #comparo si es mayor o igual a 30 
    print("Adulto/a")


"""5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
como una lista o un string."""
contraseña = input("Ingrese una contraseña de entre 8 y 14 caracteres: ")
if len(contraseña) >=8 and len(contraseña)<=14: #utilizo la funcion len para que me devuelva la cantidad de letras almacenadas en el string, además de
    #comparar si es mayor o igual a 8 y menor o igual a 14.
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")


"""6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el
siguiente:
from statistics import mode, median, mean
mi_lista = [1,2,5,5,3]
mean(mi_lista)
En la documentación oficial se puede encontrar más información sobre este paquete:
https://docs.python.org/es/3.8/library/statistics.html.
La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
mediana es mayor que la moda.
● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
la mediana es menor que la moda.
● Sin sesgo: cuando la media, la mediana y la moda son iguales.
Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
Definir la lista numeros_aleatorios de la siguiente forma:
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de
forma aleatoria. """
import random #importo la libreria random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)] #creo una lista con nros random que contenga 50 digitos entre el 1 y 100 
from statistics import mode, median, mean #importo de statics para calcular el valor más frecuente, la media ingresada , el valor central y el promedio
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)
if media > mediana and mediana > moda:
    print("Sesgo positivo o a la derecha")
    print(f"Media: {media}, Mediana: {mediana}, Moda: {moda}")
    print("La media es mayor que la mediana y, a su vez, la mediana es mayor que la moda.")
    print("La distribución normal tiene sesgo positivo.")
else:
    if media < mediana and mediana < moda:
        print("Sesgo negativo o a la izquierda")
        print(f"Media: {media}, Mediana: {mediana}, Moda: {moda}")
        print("La media es menor que la mediana y, a su vez, la mediana es menor que la moda.")
        print("La distribución normal tiene sesgo negativo.")
    else:
        if media == mediana == moda:
            print("Sin sesgo")
            print(f"Media: {media}, Mediana: {mediana}, Moda: {moda}")
            print("La media, la mediana y la moda son iguales.")
            print("La distribución normal no tiene sesgo.")
            print("No hay sesgo positivo ni negativo.")

        else:
            print("No hay sesgo positivo ni negativo.")
            print(f"Media: {media}, Mediana: {mediana}, Moda: {moda}")
            print("La distribución normal no tiene sesgo.")
			
			
			
"""7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
pantalla."""
frase = input("Ingrese una frase o palabra: ")
if frase[-1] in "aeiouAEIOU": #verifico si el ultimo caracter esta o no entre las vocales en mayusculas o minusculas.
    print(frase + "!")
else:
    print(frase)


"""8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
dependiendo de la opción que desee:
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
lower() y title() de Python para convertir entre mayúsculas y minúsculas."""
nombre= input("Ingrese su nombre: ")
opcion= int(input("Ingrese 1 para mayusculas, 2 para minusculas y 3 para primera letra mayuscula: "))
if opcion == 1:
    print("Su nombre en mayusculas es: ", nombre.upper()) #aplico funciones para mayusculas
if opcion == 2:
    print("Su nombre en minusculas es: ", nombre.lower()) #aplico funciones para minusculas 
if opcion == 3:
    print("Su nombre con la primera letra mayuscula es: ", nombre.title()) #aplico funciones para convertir la primer letra en mayusculas
	
	
"""9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
por pantalla:
● Menor que 3: "Muy leve" (imperceptible).
● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
generalmente no causa daños).
● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
débiles).
● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala)."""
magnitud = float(input("Ingrese la magnitud del terremoto: ")) #convierto lo el string a decimal
if magnitud < 3: #abro un condicional y realizo las comparacion para saber que imprimir. 
    print("Muy leve, Imperceptible")
elif magnitud >= 3 and magnitud < 4:
    print("Leve, Ligeramente perceptible")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado, Sentido por personas, pero generalmente no causa daños")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte, Puede causar daños en estructuras débiles")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte, Puede causar daños significativos")
elif magnitud >= 7:
    print("Extremo, Puede causar graves daños a gran escala")




"""Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
si el usuario se encuentra en otoño, invierno, primavera o verano.

Periodo del año

Desde el 21 de diciembre hasta el 20 de marzo (incluidos)  Estación en el hemisferio norte Invierno, Estación en el hemisferio sur Verano

Desde el 21 de marzo hasta el 20 de junio (incluidos), hemisferio norte Primavera, hemisferio sur Otoño

Desde el 21 de junio hasta el 20 de septiembre (incluidos), hemisferio norte Verano, hemisferio sur Invierno

Desde el 21 de septiembre hasta el 20 de diciembre (incluidos), hemisferio norte Otoño, hemisferio sur Primavera
"""
#convierto los string a nros enteros)
mes = int(input("Ingrese el mes del año en número: "))
dia = int(input("Ingrese el día del mes: "))
hemisferio = input("Ingrese el hemisferio en el que se encuentra (Norte/Sur): ")
if (mes == 12 and dia >= 21) or (mes == 1 or mes == 2) or (mes == 3 and dia <= 20): 
    if hemisferio == "Norte":
        print("Está en verano")
    else:
        print("Está en otoño")
elif (mes == 3 and dia >= 21) or (mes == 4 or mes == 5) or (mes == 6 and dia <= 20):
    if hemisferio == "Norte":
        print("Está en primavera")
    else:
        print("Está en invierno")
elif (mes == 6 and dia >= 21) or (mes == 7 or mes == 8) or (mes == 9 and dia <= 20):
    if hemisferio == "Norte":
        print("Está en verano")
    else:
        print("Está en otoño")
elif (mes == 9 and dia >= 21) or (mes == 10 or mes == 11) or (mes == 12 and dia <= 20):
    if hemisferio == "Norte":
        print("Está en otoño")
    else:
        print("Está en primavera")
else:
    print("Datos incorrectos")
    
    
    
    