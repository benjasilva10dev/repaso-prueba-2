# un hotel necesita un siistema para registrar resevas de habitacioens y generar un comrpobantee de reserva
# #poner variables
# validacion del huesped
# mostrar menu
# validar las opciones del menu
#agregar las habitaciones
#pedir numero de noches
# guardar la resrva
#mostrar resumen
import os
os.system("cls")
habitacion_simple = 45000
habitacion_doble = 75000
suite = 120000
precio = 0
cantidad = 0
habitacion_escogida = ""
acumulador_habitaciones = 0
#usar una flag para entrar al bucle del nombre 
nombre_valido = True
while nombre_valido:
    nombre_huesped = input("escriba el nombre del huesped, entre 3 y 25 caracteres: ")
    if len(nombre_huesped) >= 3 and len(nombre_huesped) <= 25:
        print("nombre valido")
        nombre_valido = False
    else:
        print("datos invalidos, intente nuevamente")
email_valido = True
while email_valido:
    email_huesped = input("escriba el email del huesped, tiene que tener un @ y un punto")
    if "@" in email_huesped and "." in email_huesped:
        print("email valido")
        email_valido = False
    else:
        print("datos invalidos")

#generar menú
menu_huesped = True
while menu_huesped:
    print("escoja una opcion en el menú, siguiendo los numeros \n 1.- Agregar habitación \n 2.- Ver resumen \n 3.- Salir")
    try:
        opcion_huesped = int(input("escriba su opcion"))
        if opcion_huesped == 1:
            tipo_habitacion = int(input("escriba el tipo de habitacion que quiere, 1 habitacion individual, 2. habitacion doble , 3. suite"))
            if tipo_habitacion == 1:
                noches = int(input("escriba las noches que quiere, entre 1 y 30"))
                if noches >= 1 and noches <= 30:
                    precio = noches * habitacion_simple
                    acumulador_habitaciones += precio
                    habitacion_escogida = "habitacion simple"
                    print(f"usted ha escogido estar {noches} noches")
                else:
                    print("formato de ncohes incorrecto")
            elif tipo_habitacion == 2:
                noches = int(input("escriba las noches que quiere, entre 1 y 30"))
                if noches >= 1 and noches <= 30:
                    precio = noches * habitacion_doble
                    acumulador_habitaciones += precio
                    habitacion_escogida = "habitacion doble"
                    print(f"ustes ha escogido {noches} noches ")
            elif tipo_habitacion == 3:
                noches = int(input("escriba las noches que quiere, entre 1 y 30"))
                if noches >= 1 and noches <= 30:
                    precio = noches * suite
                    acumulador_habitaciones += precio
                    habitacion_escogida = "suite"
                    print(f"usted ha escogido estar {noches} noches")
            else:
                print("formato del tipo de habitación invalido")
        elif opcion_huesped == 2:
            print("----------Comprobante Hotel Boutique------")
            print(f"Nombre huesped : {nombre_huesped} ")
            print(f"email: {email_huesped}")
            print(f"habitación : {habitacion_escogida}")
            print(f"total : {acumulador_habitaciones}")
        elif opcion_huesped == 3:
            print("hasta luego")
            menu_huesped = False
        else:
            print("opcion incorrecta")
    except:
        print("datos invalidos")
                
    
