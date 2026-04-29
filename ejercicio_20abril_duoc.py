nombre = ""
rut = ""
flag = True
hamburguesa = 5000
pizza = 8000
ensalada = 4000
acumulador_comida = 0
cantidad = 0
precio = 0
while len(nombre) < 3 or len(nombre) > 20:
    nombre = input("escriba su nombre")
while len(rut) < 8:
    rut = input("escriba su rut")
while flag:
    
    try:
        opcion= int(input("escoja una opción del menú \n 1. agregar pedido \n 2. ver resumen \n 3. descargar boleta 4. \n salir"))
        if opcion == 1:
            opcion_comida = int(input("escriba que pedido quiere agregar, 1.- hamburguesa, 2.- pizza, 3.- ensalada"))
            if opcion_comida == 1:
                cantidad = int(input("cuantos quiere?"))
                precio = cantidad * hamburguesa
                acumulador_comida = acumulador_comida + precio
            elif opcion_comida == 2:
                 cantidad = int(input("cuantos quiere?"))
                 precio = cantidad * pizza
                 acumulador_comida = acumulador_comida + precio
            elif opcion_comida == 3:
                cantidad = int(input("cuantos quiere?"))
                precio = cantidad * ensalada
                acumulador_comida =acumulador_comida + precio
        elif opcion == 4:
            flag = False
        elif opcion == 2:
            print(f"el resumen es el precio total es {acumulador_comida}, la canmtidad es {cantidad}, el nombre es {nombre} y el rut es {rut} ")
    except:
        print("datos invalidos")
            
                

            
