"""#Dado el diccionario de precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 
Añadir las siguientes frutas con sus respectivos precios:
● Naranja = 1200
● Manzana = 1500
● Pera = 2300 """

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Manzana'] = 1500
precios_frutas['Naranja'] = 1200
precios_frutas['Pera'] = 2300

"""2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
● Banana = 1330
● Manzana = 1700
● Melón = 2800"""

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melon'] = 2800


"""3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado 
en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios."""
lista_frutas = list(precios_frutas.keys())
print(lista_frutas)

"""4) Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe.
contactos= {"Juan": "123456", "Ana": "987654"}
Consultar: "Juan" -> muestra "123456" """


########
#Definición de funciones
########
import os
def limpiar_pantalla():
    if os.name == 'nt':  # Si estás en Windows
        os.system('cls')
    else:  # Si estás en Linux o Mac
        os.system('clear')

##Validador de nros-
def pedir_numero_telefono():
    valido = False  # Esta variable me dice si el número que ingresó el usuario es válido
    while not valido:  # Mientras el número no sea válido, sigo pidiéndolo
        numero = input("Ingrese su teléfono (solo números): ")  # Acá debe ir input, no volver a llamar la función
        if numero.isnumeric() and int(numero) >= 0:  # Me fijo que sean solo números y que no sea negativo
            valido = True  # Si está todo bien, salgo del bucle
        else:
            print("Por favor, ingrese un número válido (entero y mayor o igual a 0).")  # Si no cumple, le aviso
    return numero  # Devuelvo el número que ingresó correctamente

# Función para la carga de contactos
def agregar_contactos():
    contactos = {}  # Creo un diccionario vacío donde voy a guardar los contactos
    for i in range(5):  # Bucle para cargar 5 personas
        nombre = input("Ingrese el nombre del contacto: ").upper()  # Pido el nombre y lo paso a mayúsculas para que quede todo igual
        numero = pedir_numero_telefono()  # Llamo a la función que me asegura que el número esté bien escrito
        contactos[nombre] = numero  # Guardo el nombre y el número en el diccionario
        print("Contacto agregado correctamente.")  # Aviso que lo agregué bien
    return contactos  # Devuelvo la agenda con todos los contactos cargados

# Función para buscar un contacto por nombre
def buscar_contacto(contactos):
    print("Consultar un contacto:")  # Le aviso al usuario que vamos a buscar un contacto
    buscar_nom = input("Ingrese el nombre del contacto a consultar: ").upper()  # Pido el nombre a buscar y lo paso a mayúsculas para comparar igual
    if buscar_nom in contactos:  # Si ese nombre está en el diccionario...
        print("El número de", buscar_nom, "es:", contactos[buscar_nom])  # ...muestro el número que le corresponde
    else:
        print("El contacto", buscar_nom, "no existe.")  # Si no está, le aviso que no existe ese contacto

# Función principal que maneja todo

    

def main(): #Función principal que llama a agendar y buscar
    print("Administración de contactos")
    agenda = agregar_contactos()  # Llamo a la función que carga los contactos y los guardo en una variable
    limpiar_pantalla()
    print("\nLista de contactos cargados:")  # Aviso que voy a mostrar los contactos
    for nombre in agenda:  # Recorro el diccionario para mostrar los nombres
        print("-", nombre)    
        
    buscar_contacto(agenda)  # Llamo a la función para buscar y mostrar un contacto

main() #lanzo el programa

####################################################
#5_ Solicita al usuario una frase e imprime:

def palabras_unicas(frase):
    palabras = frase.split()  # Corto la frase y separo las palabras en una lista
    palabras_unicas = set(palabras)  # Uso un set para quedarme solo con las palabras sin repetir
    recuento = {palabra: palabras.count(palabra) for palabra in palabras_unicas}  # Armo un diccionario que cuenta cuántas veces aparece cada palabra
    return palabras_unicas, recuento  # Devuelvo el set y el diccionario

frase = input("Ingrese una frase: ")  # Pido al usuario que escriba una frase
palabras, recuento = palabras_unicas(frase)  # Llamo a la función y guardo lo que me devuelve
print("Palabras únicas:", palabras)  # Muestro el set con las palabras sin repetir
print("Recuento:", recuento)  # Muestro cuántas veces apareció cada palabra

##########################################
"""6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
Luego, mostrá el promedio de cada alumno. Ejemplo: alumnos = {
    "Sofía": (10, 9, 8),
    "Luis": (6, 7, 7)
}"""

def ingresar_alumnos():
    alumnos = {}  # Creo un diccionario vacío para guardar los alumnos y sus notas
    for i in range(3):  # Bucle para los 3 alumnos
        nombre = input("Ingrese el nombre del alumno: ")  # Pido el nombre del alumno
        notas = []  # Creo una lista vacía para guardar las notas
        for j in range(3):  # Bucle para ingresar las 3 notas
            nota = float(input(f"Ingrese la nota {j+1} del alumno {nombre}: "))  # Pido la nota y la convierto a float
            notas.append(nota)  # Agrego la nota a la lista
        alumnos[nombre] = tuple(notas)  # Guardo el nombre y las notas en el diccionario como una tupla
    return alumnos  # Devuelvo el diccionario con los alumnos y sus notas

################################
"""7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir)."""


def ejemplo_conjuntos():
    # Definición de sets de estudiantes que aprobaron cada parcial
    parcial1 = {"Mariano", "Giuliano", "Gustavo", "Ricardo"}
    parcial2 = {"Mariano","Giuliano","Hugo","Cintia","Nadia"}
    #aprobaron ambos
    print("Estudiantes que aprobaron ambos parciales:", parcial1 & parcial2)
    # Aprobaron 1 parcial
    print("Estudiantes que aprobaron solo uno de los dos parciales:", parcial1 ^ parcial2)
    #estudiantes que aprobaron al menos un parcial (sin repetir). 
    print("Lista total de estudiantes que aprobaron al menos un parcial:", parcial1 | parcial2)

################################
"""Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe."""

# Diccionario inicial con algunos productos y la cantidad de unidades que tienen
stock = {
    "pan": 10,
    "leche": 5,
    "azúcar": 8
}

# Esta función se fija si el producto ya existe en el stock
def consultar_stock(producto):
    if producto in stock:  # Si el producto está en el diccionario.
        print(f"Stock actual de {producto}: {stock[producto]} unidades")  # Muestro cuántas unidades tiene
        return True  # Devuelvo True porque el producto sí existe
    else:
        print(f"{producto} no está en el stock.")  # Si no está, aviso
        return False  # Devuelvo False porque no existe

# Esta función suma unidades a un producto que ya está en el stock
def agregar_unidades(producto):
    unidades = int(input("¿Cuántas unidades querés agregar?: "))  # Le pido al usuario cuántas quiere sumar
    stock[producto] += unidades  # Le sumo esas unidades al valor que ya tenía
    print(f"Nuevo stock de {producto}: {stock[producto]} unidades")  # Muestro cómo quedó

# Esta función agrega un producto nuevo al diccionario
def agregar_producto(producto):
    unidades = int(input("¿Cuántas unidades tiene?: "))  # Le pregunto cuántas unidades quiere cargar
    stock[producto] = unidades  # Lo agrego al stock con esa cantidad
    print(f"Producto {producto} agregado con {unidades} unidades.")  # Aviso que fue agregado bien

# Esta función muestra todo lo que hay cargado en el stock
def mostrar_stock():
    print("\nStock actualizado:")  # Aviso que voy a mostrar la lista
    for prod, cant in stock.items():  # Recorro todo el diccionario
        print(f"{prod}: {cant} unidades")  # Imprimo producto por producto con su cantidad

############
#Programa principal

# Le pido al usuario que escriba un producto, y lo paso a minúsculas para evitar errores con mayúsculas
producto = input("Ingrese el nombre del producto: ").lower()

# Llamo a la función para ver si ese producto ya está
if consultar_stock(producto):  # Si ya existe.
    agregar = input("¿Querés agregar unidades? (s/n): ").lower()  # Pregunto si quiere sumarle unidades
    if agregar == "s":
        agregar_unidades(producto)  # Si dijo que sí, llamo a la función para sumar más.


################################
# Creo la agenda con un par de eventos cargados
agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés"
}

# Le pido al usuario que escriba el día y la hora para consultar
dia = input("Ingrese el día: ").lower()  # Paso a minúsculas para que coincida con las claves
hora = input("Ingrese la hora (formato HH:MM): ")

# Armo la tupla con el día y la hora ingresados
eventos = (dia, hora)

# Me fijo si esa clave está en la agenda
if eventos in agenda:
    print(f"En {dia} a las {hora} tenés: {agenda[eventos]}")  # Si existe, muestro el evento
else:
    print(f"No hay eventos para {dia} a las {hora}.")  # Si no existe, aviso


################################
"""Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
• Las capitales sean las claves.
• Los países sean los valores. 
Ejemplo: pais = {"Argentina": "Buenos Aires","Chile": "Santiago","Uruguay": "Montevideo"}"""

paises = {"Argentina": "Buenos Aires", "Chile": "Santiago", "Uruguay": "Montevideo"}
capitales = {capital: pais for pais, capital in paises.items()}  
print(capitales)

