import os
os.system("cls")
x = True
acumulador_notas = 0
cantidad_notas = 0
promedio = 0
while x:
    try:
        nota = float(input("digite su nota"))
        if nota == -1:
            print("haz finalizado el programa")
            break
        acumulador_notas = nota + acumulador_notas
        cantidad_notas = cantidad_notas + 1
        promedio = acumulador_notas / cantidad_notas
    except:
        print("datos invalidos, debe ser decimal")
print(f"el promedio final fue : {promedio}")