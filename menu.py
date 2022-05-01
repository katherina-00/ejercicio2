def muestraMenu():
    op: int=0

    while op!=4:
        print("----------Eliga una opcion----------\n")
        print("1. consultar cantidad de millas\n")
        print("2. acumular millas\n")
        print("3. canjear millas\n")
        print("4.salir\n")
        op=int(input("Ingrese su opcion: "))

        return op
