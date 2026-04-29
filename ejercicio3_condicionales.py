menos_10000 = 5
entre_10000_y_20000 = 15
entre20000_y350000 = 20
entre35000_y60000 = 30
mas_60000 = 45
renta_anual_usuario = int(input("escriba el numero de su renta anual"))
if renta_anual_usuario < menos_10000:
    print(f"te corresponde un {menos_10000}% de tipo impositivo")
elif renta_anual_usuario > 10000 and renta_anual_usuario < 20000:
    print(f"te corresponde un {entre_10000_y_20000}% de tipo impositivo")
elif renta_anual_usuario > 20000 and renta_anual_usuario < 35000:
    print(f"te corresponde un {entre20000_y350000}% de tipo impositivo")
elif renta_anual_usuario > 35000 and renta_anual_usuario < 60000:
    print(f"te corresponde un {entre35000_y60000}% de tipo impositivo")
else:
    print(f"te corresponde un {mas_60000}% de tipo impositivo")