# Punto 1
lista_mult4 = list(range(4, 101, 4))
print(lista_mult4)

# Punto 2
gustos = ["pizza", "helado", "fútbol", "música", "películas"]
print(gustos[-2])

# Punto 3
lista_vacia = []
lista_vacia.append("casa")
lista_vacia.append("árbol")
lista_vacia.append("perro")
print(lista_vacia)

# Punto 4
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)

# Punto 5
#Se inicializa una lista de numeros, despues se elimina el numero mas grande de esa lista, por ultimo se imprime una lista con los numeros restantes (quedaria [8, 15,3,7])

# Punto 6
lista_numeros = list(range(10, 31, 5))
print(lista_numeros[:2])

# Punto 7
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["ford", "chevrolet"]
print(autos)

# Punto 8
dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)

# Punto 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)

# Punto 10
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)
