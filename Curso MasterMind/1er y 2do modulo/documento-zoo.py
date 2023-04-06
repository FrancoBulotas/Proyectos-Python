
edad = int(input("Decime tu edad: "))
tipo_de_carnet = input("Digame su tipo de carnet (E para Estudiante / J Jubilado / F Familia numerosa / N Nada): ")

if (25 <= edad <= 35 and tipo_de_carnet == "E") or \
        edad <= 10 or \
        (edad >= 65 and tipo_de_carnet == "P") or \
        (tipo_de_carnet == "F"):
    print("Se aplica el descuento")
else:
    print("No se aplica el descuento")
