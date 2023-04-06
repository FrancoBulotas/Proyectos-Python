

# Cantidad de letras en un texto
def letras_en_texto(frase):
    letra = input("Queres saber que cantidad de veces se repite una letra en un texto? Elegí una: ")
    cantidad_letra = 0
    for n in frase:
        if n == letra:
            cantidad_letra += 1
    return cantidad_letra


# Potencia de un numero
def potencia(num, *args):
    if args == ():
        return num * num

    resultado = num
    i = 0
    for a in range(1, args[i]):
        resultado *= num
        i += 1
    return resultado


# Fibonacci
def fibonacci(f):
    fibo_anterior = 1
    fibo_siguiente = 1
    i = 0

    if f == 1:
        return 1

    while i < f - 1:
        fibo_actual = fibo_siguiente + fibo_anterior
        fibo_anterior = fibo_siguiente
        fibo_siguiente = fibo_actual
        i += 1
    return fibo_actual


# Dice que string es mas larga
def string_mas_larga(a, b, c):
    if len(a) > len(c) and len(a) > len(b):
        return a
    elif len(b) > len(a) and len(b) > len(c):
        return b
    elif len(c) > len(a) and c > len(b):
        return c
    elif len(a) == len(b) and len(a) == len(c):
        return print("Todas tienen el mismo largo")


# Es par o impar?
def es_impar(num):
    if num % 2 == 0:
        return False
    else:
        return True


# Esta seguro el usuario?
def esta_seguro():
    preg = input("Esta seguro? SI o NO \n")

    if preg == "SI":
        return True
    elif preg == "NO":
        return False


# Convierte a mayuscula
def to_upper(palabra):
    mayus = ("ABCDEFGHIJKLMNOPQRSTUVXYZ")
    minus = ("abcdefghijklmnopqrstuvxyz")
    i = 0
    t = 0
    palabra_mayus = ""
    for caracter_palabra in palabra:
        for caracter_minus in minus:
            if caracter_palabra == caracter_minus:
                palabra_mayus += mayus[i]
            i += 1
        for caracter_mayus in mayus:
            if caracter_palabra == caracter_mayus:
                palabra_mayus += mayus[t]
            t += 1
        if caracter_palabra == " ":
            palabra_mayus += " "
        i = 0
        t = 0
    return palabra_mayus


# Intenta adivinar un numero
def adivinar_num(num):
    num_usuario = int(input("Intente adivinar el numero del 1 al 100: "))

    if num == num_usuario:
        return print("Adivinaste el numero")
    elif num != num_usuario:
        print("Numero equivocado")
        adivinar_num(num)


# Agrega items a una lista
def add_item(lista):
    agregar = input("Que desea agregar a la lista? ")

    if agregar in lista:
        print("Ya esta en la lista")
        add_item(lista)
    elif agregar not in lista:
        lista.append(agregar)
        preg = input("Desea agregar algo mas? (S/N)")
        if preg == "S":
            add_item(lista)
        elif preg == "N":
            return lista


# Suma numeros de una lista
def suma(numeros):
    sumas = 0
    for a in numeros:
        sumas += a
    return sumas


SALIDA = "SALIR"
ARCHIVO_LISTA = "lista compra.txt"


def preguntar_producto_usuario():
    return input("Introduce un producto [{} para salir] ".format(SALIDA))


def main():
    lista_compra = ["leche", "pan", "agua", "peras", "Bananas", "coca", "queso", "jamon", "nesquik"]
    lista_compra_usuario = []

    input_usuario = preguntar_producto_usuario()
    while input_usuario != SALIDA:
        if input_usuario == "LISTA":
            print("Lo que puedes agregar a tu lista de compras son los sig productos: ")
            print("\n".join([a.lower() for a in lista_compra]))
            input_usuario = preguntar_producto_usuario()

        if input_usuario.lower() not in [a.lower() for a in lista_compra]:
            print("Ese producto no esta disponible en este momento ")
            input_usuario = preguntar_producto_usuario()

        if input_usuario.lower() in  [a.lower() for a in lista_compra_usuario]:
            print("Ese producto ya esta en la lista!! ")
            input_usuario = preguntar_producto_usuario()

        if input_usuario.lower() in [a.lower() for a in lista_compra]:
            lista_compra_usuario.append(input_usuario.lower())
            print("\n".join(lista_compra_usuario))
            input_usuario = preguntar_producto_usuario()

    guardar_archivo(lista_compra_usuario)


def guardar_archivo(archivo_a_guardar):
    with open(ARCHIVO_LISTA, "w") as mi_archivo:
        mi_archivo.write("\n".join(archivo_a_guardar))


if __name__ == '__main__':
    main()
