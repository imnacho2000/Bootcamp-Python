print("Bienvenido a Nacho's Pizza!")
tamanio = input("Cual es el tamanio que quieres para la pizza? C, M o G")
pP = input("Queres pepperoni? S o N")
exQ = input("Queres extra queso? S o N")

total = 0
if(tamanio == "C"):
    total = 15;
elif(tamanio == "M"):
    total = 20
elif(tamanio == "G"):
    total = 25
if(pP == "S"):
    if(tamanio == "C"):
        total += 2
    else:
        total += 3
if(exQ == "S"):
    total += 1
print("Precio final: " + str(total))
