eN = input("Ingrese lista de puntuacion: ").split(", ")
max = 0
for n in eN:
    if(int(n) > max):
        max = int(n)
print(max)