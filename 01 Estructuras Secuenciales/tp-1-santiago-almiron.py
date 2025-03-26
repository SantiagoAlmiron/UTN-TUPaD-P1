# Ejercicio 1
print('Hello World!')

# Ejercicio 2
name = input('ingresa tu nombre: ')
print(f'Hola, {name}!')

# Ejercicio 3
name = input('Por favor, ingresa tu nombre: ')
surename = input('Por favor, ingresa tu apellido: ')
age = input('Por favor, ingresa tu edad: ')
residency = input('Por favor, ingresa tu lugar de residencia: ')

print(f'Soy {name} {surename}, tengo {age} años y vivo en {residency}.')

# Ejercicio 4
import math

radius = float(input('Ingrese el radio del círculo: '))

area = math.pi * radius ** 2

perimeter = 2 * math.pi * radius

print(f'El área del círculo es: {area}')
print(f'El perímetro del círculo es: {perimeter}')

# Ejercicio 5
seconds = int(input('Ingrese una cantidad de segundos: '))

hours = seconds / 3600

print(f'{seconds} segundos equivalen a {hours} horas.')

# Ejercicio 6
number = int(input('Ingrese un número: '))

print(f'Tabla de multiplicar del {number}:')
for i in range(1, 11):
  print(f'{number} x {i} = {number * i}')

# Ejercicio 7
num1 = int(input('Ingrese el primer número entero distinto de 0: '))
num2 = int(input('Ingrese el segundo número entero distinto de 0: '))

if num1 == 0 or num2 == 0:
  print('Los números deben ser distintos de 0.')
else:
  sum_result = num1 + num2
  subtraction = num1 - num2
  multiplication = num1 * num2
  division = num1 / num2

  print(f'La suma de {num1} y {num2} es: {sum_result}')
  print(f'La resta de {num1} y {num2} es: {subtraction}')
  print(f'La multiplicación de {num1} y {num2} es: {multiplication}')
  print(f'La división de {num1} y {num2} es: {division}')

# Ejercicio 8
height = float(input('Ingrese su altura en metros: '))

weight = float(input('Ingrese su peso en kilogramos: '))

bmi = weight / (height ** 2)

print(f'Su índice de masa corporal (IMC) es: {bmi}')

# Ejercicio 9
celsius = float(input('Ingrese la temperatura en grados Celsius: '))

fahrenheit = (9/5) * celsius + 32

print(f'La temperatura en grados Fahrenheit es: {fahrenheit}')

# Ejercicio 10
n1 = float(input('Ingrese el primer número: '))
n2 = float(input('Ingrese el segundo número: '))
n3 = float(input('Ingrese el tercer número: '))

average = (n1 + n2 + n3) / 3

print('El promedio de los tres números es:', average)
