
cajero_encendido = True
contrasenia = 1234
contador = 0
while cajero_encendido:
    contrasenia_seleccionada = (int(input("digite su contraseña")))
    if contrasenia_seleccionada == contrasenia:
        print("acceso correcto")
        break
    elif contrasenia_seleccionada != contrasenia:
        print("acceso incorrecto")
        contador = contador + 1
        if contador > 2:
            print("acceso bloqueado")
            break
