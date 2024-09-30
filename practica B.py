lista=[]
while True:
    print("1. Ingrese los items que quiera agregar a su lista: ")
    print("2. Eliminar producto: ")
    print("3. Actualizar cantidad de productos: ")
    print("4. Consultar el inventario completo: ")


    opcion = input()

    if opcion == 1:
         lista=[]
    lista_compras = []
    while True:
        item= input("Ingrese un item: ")
        if item == "fin":
            break 
        else: 
            lista_compras.append(item)


    print(lista_compras)

    if opcion == 2:
            while True:
                elim=input("Desea eliminar algún item?" )
                if elim == "si":
                        item_elim = input("Cual desea eliminar?" )
                        lista_compras.remove(item_elim)
                else:
                    print(lista_compras)
                    break
    
   
    def agregaritem():
            while True:       
                agregar_item=input("desea agregar un item?: ")
                if agregar_item=="si":
                    agregar_item=input("Agregue sus items: ")
                if agregar_item=="Fin":
                    print(lista)
                else:
                    lista.append(agregar_item)
                    print(lista)
 

   