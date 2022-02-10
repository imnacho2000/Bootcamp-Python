import random

def getLista():
    lista = []
    for i in range(1,101):
        lista.append(i)
    return lista

def bienvenido():
    print(f"Bienvendio a 'Adivina el Numero el Juego'\nEstoy pensando en un numero del 1 al 100")

def getNumber():
    return random.choice(numeros)

numeros = []

numeros = getLista()

def adivina():
    intentos = 0
    game_over = False
    bienvenido()
    dificultad = input("Ingrese dificultad 'facil' o 'dificil': ")
    numero_adivinar = getNumber()
    if(dificultad == "facil"):
        intentos = 10
    elif(dificultad == "dificil"):
        intentos = 5
    else:
        print(f"Dificultad inexistente, ingrese una opcion valida.")
    while(intentos > 0 | game_over != True):
        numero_ingresado = int(input("Ingrese un numero: "))
        if(numero_ingresado > numero_adivinar):
            print(f"El numero es menor a: {numero_ingresado}")
        elif(numero_ingresado < numero_adivinar):
            print(f"El numero es mayor a: {numero_ingresado}")
        elif(numero_ingresado == numero_adivinar):
            game_over = False
            print("Ganaste!")
            seleccion = input("Quieres volver a jugar? Y o N: ")
            if(seleccion == "Y"):
                adivina()
            else:
                return("Bay!")
        intentos -= 1
        if(intentos == 0):
            print(f"Te quedaste sin intentos!, el numero a adivinar era: {numero_adivinar}")
            seleccion = input("Quieres volver a jugar? Y o N: ")
            if(seleccion == "Y"):
                adivina()
            else:
                print("Bay!")
                
        


    