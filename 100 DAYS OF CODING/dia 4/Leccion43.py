import random
nombres = input("Nombres de los participantes: ")
nm = nombres.split(", ")
n = random.randint(0,len(nm))
print("El que le toca pagarrr: " + str(nm[n]))