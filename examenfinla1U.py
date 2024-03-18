def main():
    print("Bienvenid@ al programa monitoreo de especies")

    avistamientos = {}

    while True:
        especie = input("Ingrese una de las especies en el ecosistema (Escribe 'fin' para terminar la lista): ").lower()
        if especie == 'fin':
            break
        avistamientos[especie] = avistamientos.get(especie, 0) + 1

    print("\nInforme:")
    if avistamientos:
        for especie, cantidad in avistamientos.items():
            print(f"{especie}: {cantidad}")
        
        especie_mas_comun = max(avistamientos, key=avistamientos.get)
        print(f"\nLa especie con mas avistamientos en el ecosistema es '{especie_mas_comun}' con un total de {avistamientos[especie_mas_comun]} avistamientos.")
    else:
        print("No hay avistamientos o comportamientos.")

    print("\nFin del programa de avistamientos")

if __name__ == "__main__":
    main()