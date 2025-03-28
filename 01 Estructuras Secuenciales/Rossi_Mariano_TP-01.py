# Ejercicio 1
print ('Hola Mundo!')


#Ejercicio 2
nombre = input('Ingrese su nombre: ')
print (f'Hola {nombre}' +'!')

#Ejercicio 3
nombre = input('Ingrese su nombre: ')
apellido= input('Ingrese su apellido:')
edad= int(input('Ingrese su edad:  '))
lugar= input('Ingrese su pais: ')
print (f'Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}')

#Ejercicio 4
pi=3.1416
radio = float(input("Ingrese el radio del círculo: "))
area = pi * radio ** 2
perimetro = 2 * pi * radio
print(f'El área del círculo es: {area} y el perímetro del círculo es: {perimetro}')

#Ejercicio 5
segundos = int(input('Ingrese una número de segudos para convertirlos en horas: '))
horas = segundos // 3600
print(f'Los segundos ingresados equivalen a {horas} horas')

#Ejercicio 6 
numero= int(input('Ingrese un número para saber su tabla: '))
for i in range(1,11):
    print(f'{numero} x {i} = {numero*i}')
	
#Ejercicio 7
num1= int(input('Ingrese el primer número distinto de 0: '))
if num1 >0:
    num2= int(input('Ingrese el segundo número distinto de 0: '))
    if num2 >0:
        suma= num1 + num2
        resta= num1 - num2
        multiplicacion= num1 * num2
        divicion= num1 / num2
        aux=True
    else:
        print('El número debe ser mayor a 0')
        aux=False
else:
    print('El número debe ser mayor a 0')
    aux=False       

if aux == True:
    print(f'La suma de los números es: {suma}')
    print(f'La resta de los números es: {resta}')
    print(f'La multiplicación de los números es: {multiplicacion}')
    print(f'La divición de los números es: {division}')
	
#Ejercicio 8
altura= int(input('Ingrese su altura: '))
if altura >0:
    peso= int(input('Ingrese su peso: '))
    if peso >0:
        imc= peso/(altura**2)
        aux=True
    else:
        print('Su peso debe ser mayor a 0kg')
        aux=False
else:
    print('Su altura debe ser mayor a 0m')
    aux=False       
if aux == True:
    print(f'Su masa corporal es: {imc}')
    
	
#Ejercicio 9
celsius= int(input('Ingrese la temperatura: '))
fahrenheit= (9/5)*celsius+32
print(f'La temperatura {celsius} en grados celsius son {fahrenheit} en grados Fahrenheit.')

#Ejercicio 10
num1=int(input('Ingrese el primer número: '))
num2=int(input('Ingrese el segundo número: '))
num3=int(input('Ingrese el tercer número: '))
promerdio = (num1+num2+num3)/3
print(f'El promedio de los numeros ingresado {num1}, {num2}, {num3} es : {promerdio}')