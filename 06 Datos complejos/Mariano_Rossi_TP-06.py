"""1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range."""
lista = []
for i in range(1, 101):
    if i % 4 == 0:
        lista.append(i)
print(lista)


"""2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. 
¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!"""
lista = ["Programación", "UTN", "Tecnico", "Carrera", "Aprobada"]
print(lista[-2])



