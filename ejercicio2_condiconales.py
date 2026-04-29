import os
os.system ("cls")
sexo = int(input("escriba su sexo, 1 si es hombre o 2 si es mujer"))
nombre = str(input("escriba su nombre, todo con minuscula"))
if sexo == 1 and nombre > "n" or sexo == 2 and nombre < "m":
    print("estas en el grupo 1")
else:
    print("estas en el grupo 2")