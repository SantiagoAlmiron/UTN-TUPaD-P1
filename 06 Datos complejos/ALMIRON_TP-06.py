# 1) Dado el diccionario precios_frutas
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
# 1450}
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios.
lista_frutas = list(precios_frutas.keys())

# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.
contactos = {}
for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número de teléfono: ")
    contactos[nombre] = numero
print("Contactos guardados:", contactos)

# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra
frase = input("Ingrese una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)
conteo_palabras = {}
for palabra in palabras:
    conteo_palabras[palabra] = conteo_palabras.get(palabra, 0) + 1
print("Conteo de palabras:", conteo_palabras)

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno
alumnos = {}
for i in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    notas = tuple(float(input(f"Ingrese la nota {j+1} de {nombre}: ")) for j in range(3))
    alumnos[nombre] = notas
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es: {promedio:.2f}")

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
parcial1 = {9, 10, 7, 8}
parcial2 = {10, 6, 8, 5}
aprobados_ambos = {nota for nota in parcial1 if nota >= 7}.intersection({nota for nota in parcial2 if nota >= 7})
aprobados_uno = {nota for nota in parcial1 if nota >= 7}.symmetric_difference({nota for nota in parcial2 if nota >= 7})
aprobados_total = {nota for nota in parcial1 if nota >= 7}.union({nota for nota in parcial2 if nota >= 7})
print("Aprobados en ambos parciales:", aprobados_ambos)
print("Aprobados en solo uno de los parciales:", aprobados_uno)
print("Total de aprobados al menos un parcial:", aprobados_total)

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.
productos_stock = {}
def consultar_stock(producto):
    return productos_stock.get(producto, "Producto no encontrado")

def agregar_stock(producto, unidades):
    if producto in productos_stock:
        productos_stock[producto] += unidades
    else:
        productos_stock[producto] = unidades

def agregar_producto(producto, unidades):
    if producto not in productos_stock:
        productos_stock[producto] = unidades
    else:
        print("El producto ya existe. Use agregar_stock para aumentar el stock.")

running = True
while running:
    print("\nOpciones:")
    print("1. Consultar stock de un producto")
    print("2. Agregar unidades al stock de un producto existente")
    print("3. Agregar un nuevo producto")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        producto = input("Ingrese el nombre del producto: ")
        print(f"Stock de {producto}: {consultar_stock(producto)}")
    elif opcion == '2':
        producto = input("Ingrese el nombre del producto: ")
        unidades = int(input("Ingrese la cantidad de unidades a agregar: "))
        agregar_stock(producto, unidades)
        print(f"Stock actualizado de {producto}: {productos_stock[producto]}")
    elif opcion == '3':
        producto = input("Ingrese el nombre del nuevo producto: ")
        unidades = int(input("Ingrese la cantidad inicial de unidades: "))
        agregar_producto(producto, unidades)
        print(f"Producto {producto} agregado con stock inicial de {unidades}.")
    elif opcion == '4':
        running = False
    else:
        print("Opción no válida, intente nuevamente.")

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora
agenda = {
  ("lunes", "10:00"): "Reunión con el equipo",
  ("martes", "14:00"): "Clase de Python",
  ("miércoles", "09:00"): "Revisión de proyecto",
  ("jueves", "16:00"): "Llamada con cliente",
  ("viernes", "11:00"): "Presentación de resultados"
}

def consultar_evento(dia, hora):
    return agenda.get((dia, hora), "No hay eventos programados para este día y hora.")

running = True
while running:
    dia = input("Ingrese el día de la semana (o 'salir' para terminar): ").strip().lower()
    if dia == 'salir':
        break
    hora = input("Ingrese la hora (formato HH:MM): ").strip()
    evento = consultar_evento(dia, hora)
    print(f"Evento programado para {dia} a las {hora}: {evento}")

# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.
paises_capitales = {
    'Argentina': 'Buenos Aires',
    'Francia': 'París',
    'Japón': 'Tokio',
    'España': 'Madrid'
}
capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}
print("Diccionario de capitales y países:", capitales_paises)
