#Trabajo Practico 3

# Ejercicio 1: Mayor o Menor de Edad
edad = int(input("Ingrese su edad: "))

if edad > 18:
    print("Es mayor de edad")
else:
    print("No es mayor de edad")

    # Ejercicio 2: Aprobado o Desaprobado
nota = int(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# Ejercicio 3: Solo Numero Par
numero = int(input("Ingrese un numero par: "))

if numero % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par")

    # Ejercicio 4: Clasificacion por edad
edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Niño/a")
elif edad < 18:
    print("Adolescente")
elif edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# Ejercicio 5: Validar contraseña
contraseña = input("Ingrese una contraseña (8 a 14 caracteres): ")

if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# Ejercicio 6: Media, mediana y moda
import random
from statistics import mean, median, mode

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

print("Lista:", numeros_aleatorios)
print(f"Media: {media}, Mediana: {mediana}, Moda: {moda}")

if media > mediana > moda:
    print("Sesgo positivo (a la derecha)")
elif media < mediana < moda:
    print("Sesgo negativo (a la izquierda)")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("Distribucion no coincide exactamente con los casos anteriores")

# Ejercicio 7: Agregar "!" si termina en vocal
frase = input("Ingrese una palabra o frase: ")

if frase[-1].lower() in "aeiou":
    frase += "!"
print(frase)

# Ejercicio 8: Transformar Nombre
nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese 1 (mayusculas), 2 (minusculas) o 3 (primera letra mayuscula): "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opcion invalida")

# Ejercicio 9: Clasificar Magnitud de Terremoto
magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud < 5:
    print("Moderado (sentido por personas, pero no causa daños)")
elif magnitud < 6:
    print("Fuerte (puede causar daños en estructuras debiles)")
elif magnitud < 7:
    print("Muy fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

# Ejercicio 10: Estacion del año
hemisferio = input("Ingrese su hemisferio (N/S): ").upper()
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el daa: "))

if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
    estacion_norte, estacion_sur = "Invierno", "Verano"
elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
    estacion_norte, estacion_sur = "Primavera", "Otoño"
elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
    estacion_norte, estacion_sur = "Verano", "Invierno"
else:
    estacion_norte, estacion_sur = "Otoño", "Primavera"

if hemisferio == "N":
    print("Estacion:", estacion_norte)
elif hemisferio == "S":
    print("Estacion:", estacion_sur)
else:
    print("Hemisferio invalido")
