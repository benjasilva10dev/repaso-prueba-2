import os
os.system("cls")
acumulador = 0
total_ingresos = 0
try:
    cantidad_pasajes = int(input("cuantos pasajes quiere comprar"))
    for x in range(cantidad_pasajes):
        try:
            precio_pasaje = int(input("escriba el precio de cada pasaje"))
            acumulador = precio_pasaje + acumulador
        except:
            print("datos invalidos")
            break
    print(f"el total es : {acumulador}")
except:
    print("Datos invalidos")
