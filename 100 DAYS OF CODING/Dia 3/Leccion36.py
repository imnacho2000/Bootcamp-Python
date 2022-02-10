altura = float(input("Ingrese altura en CM: "))
edad = int(input("Ingrese edad: "))
ticket = 0
if(altura > 120):
    print("Puedes subir!")
    if((edad >= 45) and (edad <= 55)):
        ticket = 0
    elif(edad < 12):
        ticket += 5
    elif((edad >= 12) and (edad <= 18)):
        ticket += 7
    else:
        ticket += 12
    resp = input("Quieres fotos? S o N")
    if(resp == "S"):
        ticket += 3
    print("Ticket: " + str(ticket))
else:
    print("No puedes subir")