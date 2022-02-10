import functions

n = int(input("Ingrese un numero para saber si es primo: "))
print("Es primo" if functions.esPrimo(number = n) == True else "No es primo")