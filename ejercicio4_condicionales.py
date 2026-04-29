import os
os.system ("cls")
cantidad_dinero = 2400
inaceptable = 0.0
aceptable = 0.4
meritorio = 0.6
puntos = float(input("escoja el puntaje que le dieron en la evaluacion"))
if puntos == inaceptable:
    nivel = "inaceptable"
    bonificacion = cantidad_dinero * puntos
    print(f"tu nivel es {nivel}, tu bonificacion es {bonificacion}")
elif puntos == aceptable:
    nivel = "aceptable"
    bonificacion = cantidad_dinero * puntos
    print(f"tu nivel es {nivel}, tu bonifcacion es {bonificacion}")
elif puntos >= 0.6:
    nivel = "meritorio"
    bonificacion = cantidad_dinero * puntos
    print(f"tu nivel es {nivel}, tu bonficacion es {bonificacion}")
else:
    print("datos invalidos")    