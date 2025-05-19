# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
#range.
my_list = list(range(4, 101, 4))
print(my_list)

# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
# penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
# indexing con números negativos!
my_list = ["perro", "gato", "conejo", "pez", "loro"]
print(my_list[-2])

# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
# pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por
# ejemplo:
lista_vacia = []
my_list = []
my_list.append("perro")
my_list.append("gato")
my_list.append("loro")
print(my_list)

# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
# respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
# en los videos o bien investigar cómo funciona el indexing con números negativos!
# animales = ["perro", "gato", "conejo", "pez"]
animals = ["perro", "gato", "conejo", "pez"]
animals[1] = "loro"
animals[-1] = "oso"
print(animals)

# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

# Respuesta: remueve el nùmero mayor de la lista y lo imprime por pantalla.

# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
# pantalla los dos primeros.
my_list = list(range(10, 31, 5))
print(my_list[:2])

# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
# cualesquiera.
# autos = ["sedan", "polo", "suran", "gol"]
cars = ["sedan", "polo", "suran", "gol"]
cars[1] = "camioneta"
cars[2] = "pick up"
print(cars)

# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
# directamente. Imprimir la lista resultante por pantalla.
doubles = []
doubles.append(5 * 2)
doubles.append(10 * 2)
doubles.append(15 * 2)
print(doubles)

# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
# diferentes clientes:
# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
# ["agua"]]
purchases = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
# a) Agregar "jugo" a la lista del tercer cliente usando append.
purchases[2].append("jugo")
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
purchases[1][1] = "tallarines"
# c) Eliminar "pan" de la lista del primer cliente.
purchases[0].remove("pan")
# d) Imprimir la lista resultante por pantalla
print(purchases)

# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# ● Posición lista_anidada[0]: 15
# ● Posición lista_anidada[1]: True
# ● Posición lista_anidada[2][0]: 25.5
# ● Posición lista_anidada[2][1]: 57.9
# ● Posición lista_anidada[2][2]: 30.6
# ● Posición lista_anidada[3]: False
nested_list = []
nested_list.append(15)
nested_list.append(True)
nested_list.append([25.5, 57.9, 30.6])
nested_list.append(False)
# Imprimir la lista resultante por pantalla.
print(nested_list)