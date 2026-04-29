import os
os.system ("cls")

#constantes
DESCUENTO_NINO = 0.50 # menores de 12 años
DESCUENTO_ADULTO_MAYOR = 0.30 # 60 años o más
DESCUENTO_MARTES = 0.20
RECARGO_FIN_SEMANA = 0.15
IVA = 0.19
datos_validos = True



try:
    #validaciones
    nombre_cliente = input("escriba el nombre del cliente")
    edad_cliente = int(input("escriba su edad"))
    cantidad_entradas = int(input("escriba cantidad de entradas"))
    precio_base_entrada = float(input("Escriba el precio de su entrada"))
    dia_funcion = input("escriba el dia de la funcion, no están disponibles miercoles ni jueves.").lower()

    if edad_cliente < 0:
        print("edad cliente incorrecta, menor a 0")
        datos_validos = False
    if cantidad_entradas < 0:
        print("cantidad de entradas invalidas, menor a 0")
        datos_validos = False
    if precio_base_entrada < 0:
        print("precio invalido, menor a 0")
        datos_validos = False
    if dia_funcion == "miercoles" or dia_funcion == "jueves":
        print("dia de funcion invalido")
        datos_validos = False
    if datos_validos ==True:
        
        
        #calculo descuento por edad
        subtotal = cantidad_entradas * precio_base_entrada
        if edad_cliente < 12:
            valor_dcto_edad = subtotal * DESCUENTO_NINO
            tipo_cliente = "niño"
        elif edad_cliente >= 60:
            valor_dcto_edad = subtotal * DESCUENTO_ADULTO_MAYOR
            tipo_cliente = "adulto mayor"
        else:
            valor_dcto_edad = 0
            tipo_cliente = "adulto"
        valor_provisorio1 = subtotal - valor_dcto_edad
        
        #calculo descuento por dia
        if dia_funcion == "martes":
            valor_dcto_dia = valor_provisorio1 * DESCUENTO_MARTES
            valor_provisorio2 = valor_provisorio1 - valor_dcto_dia
        elif dia_funcion == "sabado" or dia_funcion == "domingo":
            valor_recargo_dia = valor_provisorio1 * RECARGO_FIN_SEMANA
            valor_provisorio2 = valor_provisorio1 + valor_recargo_dia
        else:
            valor_provisorio2 = valor_provisorio1
        
        #calcular iva
        valor_iva = IVA * valor_provisorio1
        total_final = valor_provisorio1 + valor_iva

        #condiciones de compra
        if total_final <= 10000:
            tipo_compra = "compra economica"
        elif total_final > 10000 and total_final <= 30000:
            tipo_compra = "compra normal"
        else:
            tipo_compra = "compra alta"

        #resumen
        print("----------------Resumen---------")
        print(F"nombre : {nombre_cliente.upper()}")
        print(f"edad : {edad_cliente}")
        print(f"tipo cliente : {tipo_cliente}")
        print(F"total a pagar : {total_final:.2f}")
        print(f" clasificación de compra {tipo_compra}")
    else:
        print("no se puede continuar con los calculos")
except:
    print("datos invalidos")