import os 
os.system("cls")

edad_tributar = 16
ingresos_tributar = 1000
edad_usuario = int(input("que edad tiene?"))
ingresos_usuario = int(input("que ingresos tiene?"))
if edad_usuario >= edad_tributar and ingresos_usuario >= ingresos_tributar:
    print("tienes que tributar")
else:
    print("no tienes que tributar")