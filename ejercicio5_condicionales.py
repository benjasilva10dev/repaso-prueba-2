import os
os.system
edad_cliente = int(input("que edad tienes?"))
if edad_cliente < 4:
    costo_entrada = 0
    print(f"tu entrada tiene el valor de ${costo_entrada}")
elif edad_cliente >= 4 and edad_cliente < 18:
    costo_entrada = 5
    print(f"tu entrada tiene el valor de ${costo_entrada}")
else:
    costo_entrada = 10
    print(f"tu entrada tiene el valor de ${costo_entrada}")
