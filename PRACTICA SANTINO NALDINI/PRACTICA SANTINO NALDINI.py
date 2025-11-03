
# ejercicio 1
with open("productos.txt", "w") as archivo:
    archivo.write("lapicera,120.5,30\n")
    archivo.write("cuaderno,450.0,15\n")
    archivo.write("goma,80.0,50\n")

# ejercicio 2
print("lista de productos:")
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        print("producto:", nombre, "| precio: $", precio, "| cantidad:", cantidad)

# ejercicio 3
nombre_nuevo = input("ingresa nombre del producto nuevo: ")
precio_nuevo = input("ingresa precio: ")
cantidad_nueva = input("ingresa cantidad: ")
with open("productos.txt", "a") as archivo:
    archivo.write(f"{nombre_nuevo},{precio_nuevo},{cantidad_nueva}\n")

# ejercicio 4
productos = []
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        producto = {"nombre": nombre, "precio": float(precio), "cantidad": int(cantidad)}
        productos.append(producto)
print("\nlista de productos en memoria:")
for p in productos:
    print(p)

# ejercicio 5
buscar = input("\ningresa nombre de producto a buscar: ")
encontrado = False
for p in productos:
    if p["nombre"].lower() == buscar.lower():
        print("producto encontrado:", p)
        encontrado = True
        break
if not encontrado:
    print("producto no encontrado")

# ejercicio 6
with open("productos.txt", "w") as archivo:
    for p in productos:
        archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")
print("\narchivo actualizado correctamente")
