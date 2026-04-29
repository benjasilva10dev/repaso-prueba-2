#solicitar nombre
##solicitar notas
#definir constantes
#validar las notas
#calcular promedio
#poner estado
#determinar el estado
#resumen
import os
os.system("cls")
NOTA_MINIMA_APROBACION = 4.0
NOTA_MAXIMA = 7.0
NOTA_MINIMA = 1.0
promedio = 0
try:
    nombre = input("escriba su nombre")
    nota1 = float(input("escribir primera nota como decimal"))
    nota2= float(input("escribir segunda nota como decimal"))
    nota3 = float(input("escribir tercera nota como decimal"))
    promedio = (nota1 + nota2 +nota3) / 3
    if nota1 >= NOTA_MINIMA and nota1 <= NOTA_MAXIMA and nota2 >= NOTA_MINIMA and nota2 <= NOTA_MAXIMA and nota3 >= NOTA_MINIMA and nota3 <= NOTA_MAXIMA:
        if promedio >= NOTA_MINIMA_APROBACION:
            estado = "aprobado"
        elif promedio >= 3.5 and promedio <= 3.9:
            estado = "en recuperación"
        else:
            estado = "reprobado"
        promedio_final = round(promedio,2)
        print("----------------RESUMEN--------")
        print(f"nombre del estudiante {nombre}")
        print(f"promedio : {promedio_final}")
        print(f"estado :{estado}")
except:
    print("Datos invalidos")