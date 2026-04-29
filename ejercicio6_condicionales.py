tipo_pizza = int(input("diga que tipo de pizza quiere, 1 vegetariana 2 no vegetariana"))
if tipo_pizza == 1:
    ingredientes = int(input("escoja uno de los dos ingredientes disponibkle : 1 pimiento, 2 tofu"))
    if ingredientes == 1:
        print("tu pizza es vegetariana y queda compuesta con mozzarella, tomate y piimiento")
    elif ingredientes == 2:
        print("tu pizza es vegetariana y queda compuesta con mozzarella tomate y tofu")
    else:
        print("opcion no corresponde a los ingredientes")
elif tipo_pizza == 2:
    ingredientes = int(input("escoja los ingredientes que quiere para su pizza no vegetariana 1 peperoni 2 jamon, 3 salmon")) 
    if ingredientes == 1:
        print("tu pizza no es vegetariana y  queda compuesta por mozarella tomate y peperoni") 
    elif ingredientes == 2:
        print("tu pizza no es vegetariana y  queda compuesta por mozarella, tomate y jamon")
    elif ingredientes == 3:
        print("tu pizza no es vegetariana queda compuesta por mozarella, tomate y salmon")
    else:
        print("opcion no corresponde a los ingredientes")
else:
    print("opcion no valida, escoja 1 o 2")