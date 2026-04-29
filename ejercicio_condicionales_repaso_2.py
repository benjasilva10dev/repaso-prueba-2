#definir constantes
#solicitar datos
#validarlos datos segun el formato
#el tipo de desitno, peso y que sea decimal
#calcular el costo base
#preguntar si es fragil o no, si es fragil recargo 20%
#determianar categoria
#mostrar resumen
import os
os.system
#definir constantes
PESO_MINIMO = 0.1
PESO_MAXIMO = 50.0
TARIFA_NACIONAL = 1500
TARIFA_INTERNACIONAL = 4200
RECARGO_FRAGIL = 0.20
peso = 0
costo_base = 0
total_final = 0
cantidad_recargo = 0
categoria_paquete =""
destino = ""
tarifa = 0
#solcitar datos al usuario y validarlos
try:
    nombre = input("escribir el nombre del remitente")
    peso = float(input("escribir el peso en kg, en decimal"))
    tipo_destino = int(input("escriba el tipo de destino, 1 para nacional, 2 para internacional"))
    recargo_fragil_final = int(input("su paquete es fragil, si es fragil debemos sumarle un 20 Porciento adicional"))
    if peso >= PESO_MINIMO and peso <= PESO_MAXIMO:
        print("el peso es permitido")
    else:
        print("datos de peso invalido")
    if peso < 1.0:
        categoria_paquete = "liviano"
    elif peso >= 1.0 and peso <= 10.0:
        categoria_paquete = "estandar"
    else:
        categoria_paquete ="pesado"
    if tipo_destino == 1:
        tarifa = TARIFA_NACIONAL
        destino = "nacional"
        costo_base = peso * tarifa
        if recargo_fragil_final == 1:
            cantidad_recargo = costo_base * 0.20
            total_final = cantidad_recargo + costo_base
        elif recargo_fragil_final == 2:
            print("no hay recargo por paquete no fragil")
        else:
            print("recargo fragil es invalido")  
    elif tipo_destino == 2:
            tarifa = TARIFA_INTERNACIONAL
            destino = "internacional"
            costo_base = peso * tarifa
            if recargo_fragil_final == 1:
                cantidad_recargo =  costo_base * 0.20
                total_final = cantidad_recargo + costo_base
            elif recargo_fragil_final == 2:
                print("no hay recargo por paquete no fragil")
            else:
                print("recargo fragil es invalido")
    else:
        print("tipo de destino invalido") 
    print("----------Resumen-------")
    print(f"Nombre remitente : {nombre}")
    print(f"peso del paquete : {peso}")
    print(f"categoria del paquete :  {categoria_paquete}")
    print(f"destino : {destino}")
    print(f"costo total {round(total_final ,2)}")
except:
    print("datos invalidos")

