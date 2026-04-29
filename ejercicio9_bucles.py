import os
os.system ("cls")
x= True
acumulador_calorias = 0
while x:
    try:
        calorias_quemadas = (int(input("digite cuantas calorias ha quemado, si digita 0 el programa finaliza")))
        if calorias_quemadas == 0:
            print("dejaste de quemar calorias, finalizado")
            print(f"haz quemado : {acumulador_calorias} calorias")
            break
        acumulador_calorias = calorias_quemadas + acumulador_calorias
    except:
        print("datos invalidos")
