# Punto 1
for i in range(0, 101):
    print(i)

# Punto 2
num_str = input("Ingrese un numero entero: ").strip()
if num_str == "" or (num_str == "-" or num_str == "+"):
    print("Entrada invalida.")
else:
    if num_str[0] in "+-":
        digitos = num_str[1:]
    else:
        digitos = num_str
    if digitos.isdigit():
        print("Cantidad de digitos:", len(digitos))
    else:
        print("Entrada invalida. Ingrese un entero.")

# Punto 3
a = int(input("Ingrese primer entero (a): "))
b = int(input("Ingrese segundo entero (b): "))
menor = min(a, b)
mayor = max(a, b)
if mayor - menor <= 1:
    total = 0
else:
    total = sum(range(menor + 1, mayor))
print(f"Suma de enteros entre {a} y {b} (excluyendo extremos): {total}")

# Punto 4
total = 0
while True:
    n = int(input("Ingrese un entero (0 para finalizar): "))
    if n == 0:
        break
    total += n
print("Total acumulado:", total)

# Punto 5
import random
objetivo = random.randint(0, 9)
intentos = 0
while True:
    apuesta = int(input("Adivine el numero entre 0 y 9: "))
    intentos += 1
    if apuesta < 0 or apuesta > 9:
        continue
    if apuesta == objetivo:
        print(f"¡Correcto! Necesito {intentos} intento(s).")
        break

# Punto 6
for i in range(100, -1, -2):
    print(i)

# Punto 7
while True:
    n = int(input("Ingrese un entero positivo n: "))
    if n >= 0:
        break
total = sum(range(0, n + 1))
print(f"Suma de 0 a {n}: {total}")

# Punto 8
N = 100
cont_pares = 0
cont_impares = 0
cont_positivos = 0
cont_negativos = 0
print(f"Ingrese {N} numeros enteros:")
i = 0
while i < N:
    x = int(input(f"{i+1}. "))
    i += 1
    if x % 2 == 0:
        cont_pares += 1
    else:
        cont_impares += 1
    if x > 0:
        cont_positivos += 1
    elif x < 0:
        cont_negativos += 1
print("Pares:", cont_pares)
print("Impares:", cont_impares)
print("Positivos:", cont_positivos)
print("Negativos:", cont_negativos)

# Punto 9
N = 100
suma = 0
i = 0
print(f"Ingrese {N} numeros enteros:")
while i < N:
    x = int(input(f"{i+1}. "))
    suma += x
    i += 1
media = suma / N if N > 0 else 0
print(f"Suma: {suma} | Media: {media}")

# Punto 10
s = input("Ingrese un numero entero: ").strip()
if s == "" or (s == "+" or s == "-"):
    print("Entrada invalida.")
else:
    sign = ""
    if s[0] in "+-":
        sign = s[0]
        s_digits = s[1:]
    else:
        s_digits = s
    if not s_digits.isdigit():
        print("Entrada invalida.")
    else:
        reversed_digits = s_digits[::-1]
        reversed_int = int(reversed_digits) if reversed_digits != "" else 0
        result = f"{sign}{reversed_int}" if sign != "-" else f"-{reversed_int}"
        print("Numero invertido:", result)
