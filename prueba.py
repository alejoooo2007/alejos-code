import mymath

while True:
    print("SELECCIONE LA CONVERSION QUE DESEA HACER")
    print("1 = VELOCIDAD")
    print("2 = DISTANCIA")
    print("3 = TIEMPO")
    print("4 = VOLUMEN DEL CUBO").
    print("5 = FUERZA")
    print("6 = AREA")
    print("7 = TRABAJO")
    print("8 = VELOCIDAD FINAL")
    print("9 = VELOCIDAD INICIAL")
    print("10 = ACELERACION")

    opcion =  input("iNGRESE LA OPCION QUE QUIERA REALIZAR: ")

    if opcion == "fin":
        mymath.calcular(opcion)
        break
    elif opcion in ("1, 2, 3, 4, 5, 6, 7, 8, 9, 10"):
        mymath.calcular(opcion)
    else:
        print("ERROR")

