altura = float(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso: "))
IMC =  round((peso / pow(altura,2)))
if ((IMC >= 18.5) and (IMC <= 24.9)):
    print("Su IMC es: " + str(IMC) + " Usted es normal")
elif ((IMC >= 25) and (IMC <= 29.9)):
    print("Su IMC es: " + str(IMC) + " Usted tiene sobrepeso")
elif ((IMC >= 30) and (IMC <= 34.9)):
    print("Su IMC es: " + str(IMC) + " Usted tiene sobrepeso grado 1")
elif ((IMC >= 35) and (IMC <= 39.9)):
    print("Su IMC es: " + str(IMC) + " Usted tiene sobrepeso grado 2")
else:
    print("Su IMC es: " + str(IMC) + " Usted tiene sobrepeso grado 3")
