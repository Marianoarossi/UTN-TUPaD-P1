"""1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range."""
lista = [] #creo una lista vacia
for i in range(1, 101): #recorro los elementos de 1 a 100
    if i % 4 == 0: # si son multuplos de 4 seran agregados a la lista en al siguiente instrucción
        lista.append(i) #agrego el num a la lista
print(lista) #imprimo la lista


"""2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. 
¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!"""
lista = ["Programación", "UTN", "Tecnico", "Carrera", "Aprobada"] #se crea la lista de 5 elementos
print(lista[-2])# Se muesta el penultimo elemento de la lista



"""3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla. 
Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por ejemplo: lista_vacia = []"""
lista=[] # se crea una lista vacia
lista.append("Programación") #Se agrega un elemento a la lista en las siguientes 3 instrucciones
lista.append("UTN") 
lista.append("Tecnico")
print(lista) #muestro la lista. 

"""4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente. 
Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona 
el indexing con números negativos! animales = ["perro", "gato", "conejo", "pez"]"""
animales = ["perro", "gato", "conejo", "pez"] #creo una lista de animales
animales[1] = "loro"  #Reemplazo el animal de la posicion 1
animales[-1] = "oso" #reemplazo el animal de la ultima posicion de la lista.
print(animales) #muestro la lista completa actualizada.

"""5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza."""
numeros=[8,15,3,22,7] #creo una lista de 5 numeros.
numeros.remove(max(numeros)) #busco con la funcion max() el mayor de los numeros de la lista, luego los elimino con remove()
print(numeros) #muestro la lista resultante.

"""
En la primer linea se crea una lista con 5 elementos, en este caso 5 números enteros. 
En la segunda linea se aplica la funcion max() sobre la lista, esto hace que busque el mayor número ,
luego será eliminado por la función remove.
La tercer linea imprime la lista sin el número mayor."""

"""6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros."""

numeros = list(range(10, 31, 5))
#Creo la lista  iniciando en 10, en el segundo dato del range hasta que número se creara y  en el ultimo los saltos de a 5
print(numeros[:2])
#muestro los dos primeros elementos de la lista


"""7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera. 
autos = ["sedan", "polo", "suran", "gol"]"""

autos = ["sedan", "polo", "suran", "gol"] #Creo la lista de 5 elementos
autos[1:3]= ["Captur","Clio"] #reemplazo  los valores de los indices 1 y 2, ya que el 3 queda excluido.
print(autos) #muestro la lista actualizada. 

"""8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente.
Imprimir la lista resultante por pantalla."""
dobles= [] #creo una lista vacia
dobles.append(5*2) #agrego con la funcion append() el doble de 5
dobles.append(10*2)#agrego con la funcion append() el doble de 10
dobles.append(15*2)#agrego con la funcion append() el doble de 15
print(dobles) #muestro la lista c



"""9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
a) Agregar "jugo" a la lista del tercer cliente usando append.
b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
c) Eliminar "pan" de la lista del primer cliente.
d) Imprimir la lista resultante por pantalla"""

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]] #Creamos la lista compras con 3 sublistas.
compras[2].append("jugo") #Agrego "jugo" a la lista del tercer cliente usando append
compras[1][1] = "tallarines" #Reemplazar "fideos" por "tallarines" en la lista del segundo cliente
compras[0].remove("pan")#Eliminar "pan" de la lista del primer cliente
print(compras)#Muestro la lista actualizada

"""10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
● Posición lista_anidada[0]: 15
● Posición lista_anidada[1]: True
● Posición lista_anidada[2][0]: 25.5
● Posición lista_anidada[2][1]: 57.9
● Posición lista_anidada[2][2]: 30.6
● Posición lista_anidada[3]: False
Imprimir la lista resultante por pantalla."""
lista_anidada=[] #creo la lista vacia
lista_anidada.append(15) #Agrego 15 a la lista vacia, Queda de un elemento en la posicion 0
lista_anidada.append(True) # agrego el segundo elemento a la lista en la posicion 1 
lista_anidada.append([25.5,57.9,30.6])#agrego una lista de numeros de tres elementos a la lista_anidada en la posicion 2
lista_anidada.append(False)#agrego un True en la tercer posicion de la lista. Quedando así una lista de 4 elementos(en la 3 una lista)
print(lista_anidada)#muestro la lista. 
