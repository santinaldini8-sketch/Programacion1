import math

# ejercicio 1
def imprimir_hola_mundo():
    print("hola mundo!")

imprimir_hola_mundo()


# ejercicio 2
def saludar_usuario(nombre):
    return f"hola {nombre}!"

nombre_usuario = input("ingresa tu nombre: ")
print(saludar_usuario(nombre_usuario))


# ejercicio 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"soy {nombre} {apellido}, tengo {edad} anos y vivo en {residencia}.")

nombre = input("nombre: ")
apellido = input("apellido: ")
edad = input("edad: ")
residencia = input("lugar de residencia: ")
informacion_personal(nombre, apellido, edad, residencia)


# ejercicio 4
def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("ingresa el radio del circulo: "))
print("area:", calcular_area_circulo(radio))
print("perimetro:", calcular_perimetro_circulo(radio))


# ejercicio 5
def segundos_a_horas(segundos):
    return segundos / 3600

seg = int(input("ingresa la cantidad de segundos: "))
print("equivale a", segundos_a_horas(seg), "horas")


# ejercicio 6
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

num = int(input("ingresa un numero: "))
tabla_multiplicar(num)


# ejercicio 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multi = a * b
    if b != 0:
        div = a / b
    else:
        div = None
    return suma, resta, multi, div

x = float(input("primer numero: "))
y = float(input("segundo numero: "))
suma, resta, multi, div = operaciones_basicas(x, y)
print("suma:", suma)
print("resta:", resta)
print("multiplicacion:", multi)
print("division:", div if div is not None else "error: division por cero")


# ejercicio 8
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("peso (kg): "))
altura = float(input("altura (m): "))
imc = calcular_imc(peso, altura)
print("tu imc es:", round(imc, 2))


# ejercicio 9
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temp_c = float(input("temperatura en celsius: "))
print("equivale a", round(celsius_a_fahrenheit(temp_c), 2), "fahrenheit")


# ejercicio 10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

n1 = float(input("primer numero: "))
n2 = float(input("segundo numero: "))
n3 = float(input("tercer numero: "))
print("el promedio es:", calcular_promedio(n1, n2, n3))
