montoP = float(input("Bienvendio a la calculadora de cuenta!.\nIngrese monto a pagar: $"))
personasADiv = int(input("Ingrese entre cuantas personas lo va a dividir: "))
propina = float(input("Ingrese propina: "))
if (propina == 0):
    print("Monto a pagar: $" + str((montoP / personasADiv)))
else:
    print("Monto a pagar: $" + str(((montoP / personasADiv) + ((propina/100) * montoP / personasADiv))))
