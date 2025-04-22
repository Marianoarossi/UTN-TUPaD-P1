"""1. Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal."""

#Definicición de funciones
def saludar():
    print("Hola Mudno!")

# Programa principal
saludar()

"""2. Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver:
“Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario."""
#Definicición de funciones
def saludar_usuario(nombre):
    print(f"Hola {nombre}")

# Programa principal

saludar_usuario("Marcos")

"""3. Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir
los datos al usuario y llamar a esta función con los valores ingresados."""

#Definicición de funciones
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
    
def validaedad(edad):
    while edad<=0 :
        edad=int(input("Ingrese una edad valida: "))
    return edad
    

# Programa principal
nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
edad=int(input("Ingrese su edad: "))
edad_valida=validaedad(edad)
residencia=input("Ingrese su residencia: ")


informacion_personal(nombre, apellido, edad_valida, residencia)

"""4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio
como parámetro y devuelva el área del círculo. calcular_perimetro_
circulo(radio) que reciba el radio como parámetro y devuelva
el perímetro del círculo. Solicitar el radio al usuario y llamar ambas
funciones para mostrar los resultados."""

"""4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio
como parámetro y devuelva el área del círculo. calcular_perimetro_
circulo(radio) que reciba el radio como parámetro y devuelva
el perímetro del círculo. Solicitar el radio al usuario y llamar ambas
funciones para mostrar los resultados."""
def calcular_area_circulo(radio):
    area=3.14*radio**2
    return area
def calcular_perimetro_circulo(radio):
    perimetro=2*3.14*radio
    return perimetro
radio=float(input("Ingrese el radio del circulo: "))
area=calcular_area_circulo(radio)
perimetro=calcular_perimetro_circulo(radio)
print(f'El area del circulo es: {area}')
print(f'El perimetro del circulo es: {perimetro}')


"""5. Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mostrar
el resultado usando esta función."""
def validar_segundos():
    while True:
        entrada = input("Ingrese la cantidad de segundos: ")
        es_entero_positivo = True
        for caracter in entrada:
            if caracter < '0' or caracter > '9':
                es_entero_positivo = False
        if es_entero_positivo and entrada and int(entrada) >= 0:
            return int(entrada)
        else:
            print("Error: Debe ingresar un número entero positivo.")

def segundos_a_horas(segundos):
    horas = segundos // 3600
    return horas

# Solicitar la cantidad de segundos al usuario y validar la entrada
segundos = validar_segundos()

# Calcular y mostrar el resultado
horas = segundos_a_horas(segundos)
print(f"{segundos} segundos son {horas} horas")


