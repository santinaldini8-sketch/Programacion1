# Trabajo Practico de secuenciales
# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”

print("Hola Mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado.

nombre = input("Por favor, ingresa tu nombre: ")
print("Hola " + nombre + "!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados.

Nombre = input("Ingrese su nombre: ")
Apellido = input("Ingrese su apellido: ")
Edad = input("Ingrese su edad: ")
Residencia = input("Ingrese su lugar de residencia: ")

print("Soy " + Nombre + " " + Apellido + ", tengo " + Edad + " años y vivo en " + Residencia)

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

radio = int(input("Ingrese el radio del círculo en CM: "))

area = 3.14 * radio * 2

perimetro = 2 * 3.14 * radio

print("El área del círculo es:", area)
print("El perímetro del círculo es:", perimetro , "CM")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
print("Calculadora de segundos a horas")

segundos = int(input("Ingrese la cantidad de segundos: "))

horas = segundos / 3600

print("Total De Horas:", horas)

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
print("Tablas del 1 al 10")

Numero = int(input("Ingrese un Numero: "))

Tabla = Numero * 1, Numero * 2, Numero * 3, Numero * 4, Numero * 5, Numero * 6, Numero * 7, Numero * 8, Numero * 9, Numero * 10

print("Tabla del 1 al 10:", Tabla)

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
print("Calculadora")

num1 = int(input("Ingresa el primer número entero (que no sea 0): "))

num2 = int(input("Ingresa el segundo número entero (que no sea 0): "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

print("\nResultados de las operaciones:")
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.
print("Calculadora de peso corporal")

altura = int(input("ingresa tu altura en Metros: "))

Peso = int(input("ingresa tu peso en KG: "))

IMC = Peso / altura

print("Su indice de masa corporal es de:", IMC)

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.
print("Calculadora de grados celsius a grados fahrenheit")

celsius = int(input("ingrese temperatura en grados celsius: "))

Fahrenheit = 9 / 5 * celsius + 32

print("La conversión en grados fahrenheit es de:", Fahrenheit)

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números
print("Calculadora de promedios")

N1 = int(input("Escriba un numero: "))
N2 = int(input("Escriba un numero: "))
N3 = int(input("Escriba un numero: "))

Promedio = (N1 + N2 + N3) / 3

print("El promedio entre estos 3 numeros es", Promedio)

