#Un cine necesita un sistema que permita caluclar el total a pagar por la compra de entarda, considerando descuentos.

#Definir constantes
DESCUENTO_NINO = 0.50 #MENOR 12 AÑOS
DESCUENTO_ADULTO_MAYOR = 0.30
DESCUENTO_MARTES = 0.20
RECARG_FIN_SEMANA = 0.15
IVA = 0.19
subtotal = 0
dcto_edad = 0
entrada_dcto_bruto = 0
entrada_recargo_bruto = 0
total_final = 0
iva = 0
estado =""
tipo_cliente = ""
import os
os.system

#pedir nombre
nombre_cliente= input("escriba el nombre del cliente")
#validaciones con los datos
try:
    edad_cliente = int(input("escriba la edad del cliente"))
    cantidad_entradas = int(input("escriba la cantidad de entradas"))
    precio_base = float(input("escriba el precio base de la entrada"))
    dia_funcion = input("escriba el dia de la funcion con mayuscula solo la primera letra, puede ser: lunes, martes, viernes, sábado y domingo ej: L")
    #validaciones requisitos
    if edad_cliente >= 0 and cantidad_entradas > 0 and precio_base > 0:
        if dia_funcion == "L" or dia_funcion == "M" or dia_funcion == "V" or dia_funcion == "S" or dia_funcion == "D":
            print("datos VALIDOS")
            subtotal = precio_base * cantidad_entradas
            if edad_cliente < 12:
                tipo_cliente = "niño"
                dcto_edad = subtotal * DESCUENTO_NINO
                entrada_dcto_bruto = subtotal + dcto_edad
                iva = IVA * entrada_dcto_bruto
                total_final = iva + entrada_dcto_bruto
            elif edad_cliente >= 60:
                tipo_cliente = "adulto mayor"
                dcto_edad = subtotal * DESCUENTO_ADULTO_MAYOR
                entrada_dcto_bruto = subtotal + dcto_edad
                iva =  iva * entrada_dcto_bruto
                total_final = iva + entrada_dcto_bruto
            else:
                tipo_cliente ="adulto"
                dcto_edad = 0
                entrada_dcto_bruto = subtotal + dcto_edad
                iva = IVA * entrada_dcto_bruto
                total_final = iva + entrada_dcto_bruto
                print("no hay descuento por edad")
                if dia_funcion == "M":
                    entrada_dcto_bruto_dia = total_final * DESCUENTO_MARTES
                    total_final = entrada_dcto_bruto_dia + total_final
                elif dia_funcion == "S" or "D":
                    entrada_recargo_bruto = total_final * RECARG_FIN_SEMANA
                    total_final = entrada_recargo_bruto + total_final
                else:
                    entrada_dcto_bruto_dia = 0
                    total_final = total_final
                    print("no hay descuento por dia de semana")
                    if total_final <= 10000:
                        estado = "compra economica"
                    elif total_final > 10000 and total_final <= 30000:
                        estado = "compra normal"
                    else:
                        estado = "compra alta"
                    print("-----------------Resumen--------------------")
                    print(f"el nombre del cliente es {nombre_cliente}")
                    print(f" la edad es : {edad_cliente}")
                    print(F"el tipo cliente es {tipo_cliente}")
                    print(f"el total es : {round(total_final,2)}")
                    print(f"el estado de compra es {estado}")
        else:
            print("Datos del dia invalido")
except:
    print("Datos invalidos")

            
        


