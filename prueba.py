# Ejercicio 15 WHILE
def numeros_primos_hasta(numero):
    cont = 1
    cont_divisor = 1
    cont_dividendo = 1
    cont_divisibles = 0
    lista_primos = [1]
    while cont <= numero:
        while cont_divisor <= cont_dividendo:
            if cont_dividendo % cont_divisor == 0:
                cont_divisibles += 1
            cont_divisor += 1

        if cont_divisibles == 2:
            lista_primos.append(cont_dividendo)
        cont += 1
        cont_dividendo += 1
        cont_divisor = 1
        cont_divisibles = 0

    return lista_primos


print(numeros_primos_hasta(15))
