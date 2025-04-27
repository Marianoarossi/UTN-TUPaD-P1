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
#defino funciones. 
def calcular_area_circulo(radio):
    area=3.14*radio**2
    return area
def calcular_perimetro_circulo(radio):
    perimetro=2*3.14*radio
    return perimetro
#programa principal
radio=float(input("Ingrese el radio del circulo: "))
area=calcular_area_circulo(radio)
perimetro=calcular_perimetro_circulo(radio)
print(f'El area del circulo es: {area}')
print(f'El perimetro del circulo es: {perimetro}')


"""5. Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mostrar
el resultado usando esta función."""
#Definó las funciones.
def validar_segundos(): #Valido caracteres números y que sean positivos. 
    while True:
        entrada = input("Ingrese la cantidad de segundos: ")
        es_entero_positivo = True #utilizo banderas, asigno verdadero para permanecer en el while
        for caracter in entrada:
            if caracter < '0' or caracter > '9':
                es_entero_positivo = False #utilizo banderas para salir del bucle
        if es_entero_positivo and entrada and int(entrada) >= 0:
            return int(entrada)
        else:
            print("Error: Debe ingresar un número entero positivo.")

def segundos_a_horas(segundos):
    horas = segundos // 3600
    return horas

# Solicitó la cantidad de segundos al usuario y valido la entrada
segundos = validar_segundos()

# Programa principal ----> Calculó y muestro el resultado
horas = segundos_a_horas(segundos)
print(f"{segundos} segundos son {horas} horas")

"""6. Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la función."""

# Definición de funciones
def tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# Programa principal

    # Solicito el número al usuario y valido la entrada
def programa():
    numero_valido = False
    while not numero_valido:
        entrada_numero = input("Ingrese un número y se imprimira su tabla de multiplicar: ")
        es_numero = True
        for char in entrada_numero:
            if char < '0' or char > '9':
                es_numero = False
        if es_numero and entrada_numero:
            numero_valido = True
        else:
            print("Error: Debe ingresar un número entero válido.")
    numero = int(entrada_numero)

    # Llamo a la función para imprimir la tabla de multiplicar pasandole como parametro el nro ingresado.
    tabla_multiplicar(numero)

programa() #inicio el programa principal.



"""7. Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resultado
de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados
de forma clara."""
#Definicion de funciones 

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Indefinido (división por cero)"
    return (suma, resta, multiplicacion, division)

#programa principal
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
resultados = operaciones_basicas(a, b)
print(f"Resultados de las operaciones básicas entre {a} y {b}:")
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")


"""8. Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la función
para mostrar el resultado con dos decimales."""
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
imc = calcular_imc(peso, altura)
print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")


"""10.Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función."""
#Definicion de funciones
def calcular_promedio(a,b,c):
    promedio = (a+b+c)/3 #calculo el promedio de los tres digitos ingresados.
    return promedio


def validar_numero(mensaje):
    numero_valido = False
    while not numero_valido: #inicio un bucle para forzar al usuario a que ingrese un dato valido.
        entrada_numero = input(mensaje)
        es_numero = True
        if entrada_numero:
            if entrada_numero == '-': # valido que no ingrese solamente el signo negativo. 
                es_numero = False
            elif entrada_numero[0] == '-':
                entrada_numero = entrada_numero[1:] 
                """Comparo los caracteres desde el segundo caracter sin el signo negativo. Con esto consigo
                poder validar los siguientes caracteres"""                
            if entrada_numero == '0': 
                es_numero = True
            else:
                for caracter in entrada_numero: #recorro cada caracter ingresado.
                    if caracter < '0' or caracter > '9': #Valido si no está entre el rango de numeros validos.
                        es_numero = False
        else:
            es_numero = False
        if es_numero:
            numero_valido = True
        else:
            print("Error: Debe ingresar un número válido.")
    return float(entrada_numero) #devuelvo el nro validado. 



#progrmaa principal y ejecucion
def programa():
    a = validar_numero("Ingrese el primer número: ")
    b = validar_numero("Ingrese el segundo número: ")
    c = validar_numero("Ingrese el tercer número: ")
    promedio = calcular_promedio(a,b,c)
    print(f"El promedio de los tres números es: {promedio}")

programa()