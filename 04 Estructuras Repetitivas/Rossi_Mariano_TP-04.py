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
    
print(f"La suma de los números comprendidos entre {num1} y {num2} es {suma}.") #imprimo la suma de los numeros comprendidos entre los dos numeros dados por el usuario
