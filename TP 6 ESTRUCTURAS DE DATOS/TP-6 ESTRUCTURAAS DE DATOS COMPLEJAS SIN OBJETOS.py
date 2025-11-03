
# ejercicio 1
precios_frutas = {'banana': 1200, 'anana': 2500, 'melon': 3000, 'uva': 1450}
precios_frutas['naranja'] = 1200
precios_frutas['manzana'] = 1500
precios_frutas['pera'] = 2300
print("ej1:", precios_frutas)

# ejercicio 2
precios_frutas['banana'] = 1330
precios_frutas['manzana'] = 1700
precios_frutas['melon'] = 2800
print("ej2:", precios_frutas)

# ejercicio 3
solo_frutas = list(precios_frutas.keys())
print("ej3:", solo_frutas)

# ejercicio 4
agenda = {}
for i in range(5):
    nombre = input("ingresa nombre del contacto: ")
    numero = input("ingresa numero telefonico: ")
    agenda[nombre] = numero
buscar = input("ingresa nombre a buscar: ")
if buscar in agenda:
    print("el numero es:", agenda[buscar])
else:
    print("contacto no encontrado")

# ejercicio 5
frase = input("ingresa una frase: ")
palabras = frase.lower().split()
unicas = set(palabras)
print("palabras unicas:", unicas)
contador = {}
for palabra in palabras:
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1
print("cantidad de apariciones:", contador)

# ejercicio 6
alumnos = {}
for i in range(3):
    nombre = input("nombre del alumno: ")
    nota1 = float(input("nota 1: "))
    nota2 = float(input("nota 2: "))
    nota3 = float(input("nota 3: "))
    alumnos[nombre] = (nota1, nota2, nota3)
for nombre, notas in alumnos.items():
    promedio = sum(notas) / 3
    print("promedio de", nombre, ":", promedio)

# ejercicio 7
parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7}
ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2
print("ambos parciales:", ambos)
print("solo uno:", solo_uno)
print("al menos uno:", al_menos_uno)

# ejercicio 8
stock = {"lapiz": 10, "cuaderno": 5, "goma": 8}
producto = input("ingresa producto a consultar: ")
if producto in stock:
    print("stock actual:", stock[producto])
    agregar = int(input("cuantas unidades agregar?: "))
    stock[producto] += agregar
else:
    nuevo = int(input("producto no existe, cantidad inicial: "))
    stock[producto] = nuevo
print("stock actualizado:", stock)

# ejercicio 9
agenda_eventos = {}
for i in range(3):
    dia = input("ingresa dia: ")
    hora = input("ingresa hora: ")
    evento = input("ingresa evento: ")
    agenda_eventos[(dia, hora)] = evento
dia_consulta = input("dia a consultar: ")
hora_consulta = input("hora a consultar: ")
clave = (dia_consulta, hora_consulta)
if clave in agenda_eventos:
    print("actividad:", agenda_eventos[clave])
else:
    print("no hay actividad registrada")

# ejercicio 10
paises = {"argentina": "buenos aires", "brasil": "brasilia", "chile": "santiago"}
capitales = {}
for pais, capital in paises.items():
    capitales[capital] = pais
print("diccionario invertido:", capitales)
