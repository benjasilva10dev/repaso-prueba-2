pokebola = 1000
pocion = 1500
revivir = 3000
baya = 500
precio = 0
dcto_total_compra = 0
dcto_cantidad = 0
cantidad = 0
dcto_revivir  = 0
dcto_acumulado = 0
flag = True
total_bruto = 0
total_final = 0

while flag:
    try:
        opcion = int(input("escoge segun el numero el producto que quieres comprar, pokebola :1 , pocion :2, revivir : 3, baya : 4.. todo como numero entero y positivo: "))
        cantidad = int(input("cuanta cantidad quieres"))