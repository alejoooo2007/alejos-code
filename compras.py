lista_compras = []
while True:
    item= input("Ingrese un item: ")
    if item == "fin":
        break 
    else: 
        lista_compras.append(item)


print(lista_compras)

while True:
    elim=input("Desea eliminar algún item?" )
    if elim == "si":
        item_elim = input("Cual desea eliminar?" )
        lista_compras.remove(item_elim)
    else:
        print(lista_compras)
        break
