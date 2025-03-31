# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

age = int(input("Ingrese su edad: "))
if age >= 18:
    print("Es mayor de edad")

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.

qualification = int(input("Ingrese su nota: "))
if qualification >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.

number = int(input("Ingrese un número: "))
if number % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:

age = int(input("Ingrese su edad: "))
if age < 0:
    print("La edad no puede ser negativa")
elif age < 12:
    print("Es un niño")
elif age >= 12 and age < 18:
    print("Es un adolescente")
elif age >= 18 and age < 30:
    print("Es un adulto joven")
elif age >= 30 and age < 60:
    print("Es un adulto")

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.

password = input("Ingrese una contraseña (8 a 14 caracteres): ")
if len(password) >= 8 and len(password) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6)  # Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# Definir la lista numeros_aleatorios de la siguiente forma:

from statistics import mode, median, mean
from random import randint
rand_numbers = []
for i in range(100):
    rand_numbers.append(randint(1, 100))

print(rand_numbers)

md = mode(rand_numbers)
mn = median(rand_numbers)
m = mean(rand_numbers)
if m > mn and mn > md:
    print("Sesgo positivo o a la derecha")
elif m < mn and mn < md:
    print("Sesgo negativo o a la izquierda")
elif m == mn and mn == md:
    print("Sin sesgo")
else:
    print("No se puede determinar el sesgo")

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla

word = input("Ingrese una palabra o frase: ")
if word[-1].lower() in "aeiou":
    word += "!"
    print(word)
else:
    print(word)

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1.​ Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2.​ Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3.​ Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

name = input("Ingrese su nombre: ")
option = int(input("Ingrese 1 para mayúsculas, 2 para minúsculas o 3 para capitalizar: "))
if option == 1:
    print(name.upper())
elif option == 2:
    print(name.lower())
elif option == 3:
    print(name.title())
else:
    print("Opción no válida")

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# ●​ Menor que 3: "Muy leve" (imperceptible).
# ●​ Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ●​ Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# ●​ Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# ●​ Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ●​ Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitude = float(input("Ingrese la magnitud del terremoto: "))
if magnitude < 3:
    print("Muy leve (imperceptible)")
elif 3 <= magnitude < 4:
    print("Leve (ligeramente perceptible)")
elif 4 <= magnitude < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitude < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif 6 <= magnitude < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisphere = input("Ingrese su hemisferio (N/S): ").upper()
month = int(input("Ingrese el mes (1-12): "))
day = int(input("Ingrese el día (1-31): "))
if hemisphere == "N":
    if (month == 12 and day >= 21) or (month <= 2) or (month == 3 and day <= 20):
        print("Invierno")
    elif (month == 3 and day >= 21) or (month <= 5) or (month == 6 and day <= 20):
        print("Primavera")
    elif (month == 6 and day >= 21) or (month <= 8) or (month == 9 and day <= 20):
        print("Verano")
    elif (month == 9 and day >= 21) or (month <= 11) or (month == 12 and day <= 20):
        print("Otoño")
elif hemisphere == "S":
    if (month == 12 and day >= 21) or (month <= 2) or (month == 3 and day <= 20):
        print("Verano")
    elif (month == 3 and day >= 21) or (month <= 5) or (month == 6 and day <= 20):
        print("Otoño")
    elif (month == 6 and day >= 21) or (month <= 8) or (month == 9 and day <= 20):
        print("Invierno")
    elif (month == 9 and day >= 21) or (month <= 11) or (month == 12 and day <= 20):
        print("Primavera")