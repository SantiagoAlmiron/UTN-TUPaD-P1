# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for i in range(101):
    print(i)


# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.
num = int(input("Ingrese un número: "))
digits = 0
while num > 0:
    num = num // 10
    digits += 1
print(f"El número tiene {digits} dígitos.")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))
sum = 0
for i in range(num1 +1 , num2):
    sum += i
print(f"La suma de los números entre {num1} y {num2} es: {sum}")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.
user_input = ''
sum = 0
while user_input != 0:
  user_input = int(input("Ingrese un número: "))
  sum += user_input
print(f"La suma total es: {sum}")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
from random import randint
print ("Adivine el número entre 0 y 9:")
rand_number = randint(0,9)
count = 0
flag = True
while flag:
  count += 1
  user_input = int(input("Por favor ingrese un número: "))
  if user_input == rand_number:
    flag = False
print(f"Usted adivinó en {count} intentos")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.
for i in range(100, -1, -2):
  print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.
user_input = int(input("Por favor ingrese un número: "))
sum = 0
for i in range(0, user_input + 1):
  sum += i
print(f"La suma desde 0 hasta {user_input} es {sum}")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).
inputs_count = 0
odd = 0
even = 0
positive = 0
negative = 0
while inputs_count <= 100:
  user_input = int(input("Ingrese un número: "))
  inputs_count += 1
  if user_input%2 != 0:
    odd += 1
  else:
    even += 1
  if user_input > 0:
    positive += 1
  elif user_input < 0:
    negative += 1

print(
  f"El usuario ingresó {odd} números impares",
  f"El usuario ingresó {even} números pares",
  f"El usuario ingresó {positive} números positivos",
  f"El usuario ingresó {negative} números negativos",
  sep='\n'
)

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).
from statistics import mean
numbers = []
input_count = 0
while input_count < 100:
  user_input = int(input("Ingrese un número: "))
  numbers.append(user_input)
  input_count += 1

average = mean(numbers)

print(f"El promedio de los 100 números ingresados es: {average}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
user_input = input("Por favor ingrese un número:")
reverse_number = user_input[::-1]
print(f"El número invertido es {reverse_number}")
