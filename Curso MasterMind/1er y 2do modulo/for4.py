

numero_introducido = input("Introduzca los numeros separados por comas: ")
numeros_de_usuario = [int(numeros) for numeros in numero_introducido.split(",")]

for num in numeros_de_usuario:
   maximo = max(numeros_de_usuario)
   minimo = min(numeros_de_usuario)

print("El numero mas grande es: {}".format(maximo))
print("El numero mas chico es: {}".format(minimo))