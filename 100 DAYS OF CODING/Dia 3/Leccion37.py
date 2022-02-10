name = input("Ingrese nombre: \n")
nam2 = input("Ingrese nombre 2: \n")
nameM = name.lower() + nam2.lower()
a = nameM.count("l")
a += nameM.count("o")
a += nameM.count("v")
a += nameM.count("e")

b = nameM.count("t")
b += nameM.count("r")
b += nameM.count("u")
b += nameM.count("e")

print("Porcentaje: " + str(b) + str(a) + "%.")
