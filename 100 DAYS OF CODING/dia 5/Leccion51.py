estudiantes = input("Escriba altura de estudiantes en cm: ")
nE = estudiantes.split(", ")
total = 0
for n in nE:
    total+=int(n)
print("Promedio: " + str(round(total/len(nE))))