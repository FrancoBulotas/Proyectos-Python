
lista = []
eleccion = None

while eleccion != "Q":
    eleccion = input("Que desea comprar? (´Q´ para salir): ")

    if eleccion == "Q":
        break

    if eleccion in lista:
        print("{} ya esta en la lista".format(eleccion))
    otra_eleccion = eleccion
    otra_eleccion = input("Seguro que desea comprar {}? S/N: ".format(eleccion))

    if otra_eleccion == "S":
        lista.append(eleccion)
        print("Se añadio {} a tu lista de compra!\n".format(eleccion))
    else:
        print("No se añadio {} a tu lista\n".format(eleccion))

print("Su lista de compra contiene " + lista)