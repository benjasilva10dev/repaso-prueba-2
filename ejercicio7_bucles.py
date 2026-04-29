import os
os.system ("cls")
acumulador = 0
try:
    cantidad_productos_vendidos = int(input("cuantos productos vendiste"))
    for x in range(cantidad_productos_vendidos):
        precio_produdcto = int(input("cual es el precio del producto?"))
        acumulador = acumulador + precio_produdcto
        print(f"el total de la venta de los productos es {acumulador}")
except:
    print("datos invalidos")
