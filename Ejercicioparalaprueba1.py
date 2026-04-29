#solicitar datos
#definir constantes
#validaro datos en el rango
#calcular promedio
#usar variable para acumular suma
#determminar estado
import os
os.system("cls")
PUNTAJE_MINIMO_APROBACION = 4.0
PUNTAJE_MAXIMO = 7.0
PUNTAJE_MINIMO = 1.0
suma_pruebas = 0
promedio_pruebas = 0




nombre = input("ingrese su nombre")
try:
    prueba_resistencia = float(input("escriba del 1.0 al 7.0 como decimal su rendimiento en la prueba de resistencia"))
    prueba_fuerza = float(input("escriba su rendmiento en la prueba de fuerza"))
    prueba_velocidad = float(input("escriba su rendimiento de la prueba de velocidad"))
    if prueba_velocidad >= PUNTAJE_MINIMO and prueba_velocidad <= PUNTAJE_MAXIMO and prueba_resistencia >= PUNTAJE_MINIMO and prueba_resistencia <= PUNTAJE_MAXIMO and prueba_fuerza >= PUNTAJE_MINIMO and prueba_fuerza <= PUNTAJE_MAXIMO:
        suma_pruebas = prueba_velocidad + prueba_resistencia + prueba_fuerza
        promedio_pruebas = suma_pruebas / 3
        if promedio_pruebas >= PUNTAJE_MINIMO_APROBACION:
            estado = "seleccionado"
        elif promedio_pruebas >= 3.5 and promedio_pruebas <= 3.9:
            estado = "en observacion"
        else:
            estado = "no seleccionado"
        print("-------------FICHA DEL DEPORTISTA ------------")
        print(f"nombre : {nombre}")
        print(f"Resistencia : {prueba_resistencia}")
        print(f"Fuerza : {prueba_fuerza}")
        print(f"Velocidad :{prueba_velocidad}")
        print(f"Promedio : {promedio_pruebas}")
        print(f"Estado : {estado}")
    else:
        print("datos invalidos")
except:
    print("datos invalidos")

