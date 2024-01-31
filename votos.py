partido_rojo=" "
partido_azul=" "
eleccion_presidencial=" "
confirmacion=" "
DPI=" "
DPI=(input("ingrese si DPI: "))
if len(DPI)<13:
    print("no valido")
if len(DPI)>13:
    print("no valido")
if len(DPI)==13:
    print("valido")
    print("tus opciones para presidencia son: ")
    print("partido rojo")
    print("partido azul")
    eleccion_presidencial= input("Hacia que partido va su voto: ")
    if eleccion_presidencial== "Rojo":
        print("Su voto ha sido para el partido rojo")

    if eleccion_presidencial== "Azul":
        print("Su voto ha sido para el partido azul")

    elecciones_alcadia=" "
    ultima_confirmacion=" "
    resumen=" "
    print("partido azul")
    print("partido rojo")
    print("partido verde")
    print("partido naranja")
    elecciones_alcadia= input("Tu voto para alcaldia de de la Antigua Guatemla fue para: ")
    if elecciones_alcadia== "Rojo":
        print("Su voto para la alcaldia fue para el partido rojo")

    if elecciones_alcadia== "Azul":
        print("Su voto para la alcaldia fue para el partido azul")

    if elecciones_alcadia== "verde":
        print("Su voto para la alcaldia fue para el partido verde")

    if elecciones_alcadia== "naranja":
        print("Su voto para la alcaldia fue para el partido naranja")

    ultima_confirmacion= print("Desea confirmar sus votos? confirmar?, no confirmar?")
    ultima_confirmacion= input("")
    if ultima_confirmacion== "confirmo":
        print("Sus votos han sido guardados :D ")

    if ultima_confirmacion== "No confirmar":
        print("Sus votos no se han guardado, intente de nuevo :( pipipi )")
    