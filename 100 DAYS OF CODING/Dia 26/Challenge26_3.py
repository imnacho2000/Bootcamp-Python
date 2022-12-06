with open("archivo1.txt",mode="r") as f1:
    lista1 = f1.readlines()
with open("archivo2.txt",mode="r") as f2:
    lista2 = f2.readlines()

lista_final = [int(n) for n in lista1 if n in lista2]

print(f"Lista 1:\n{lista1}")
print(f"Lista 2:\n{lista2}")
print(f"Resultado final:\n {lista_final}")