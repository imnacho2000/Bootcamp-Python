import os

palabra = input(f"ingrese palabra a adivinar: ")
os.system("cls")
palabra_guardada = []

for n in palabra:
    palabra_guardada.append("_")



intentos = 3
game_on = True
cont = 0

print(f"palabra/s a adivinar: {palabra_guardada}")
while game_on:
    l = input("Ingrese una letra: ")
    for n in range(len(palabra)):
        letraC = palabra[n]
        if l == letraC:
            palabra_guardada[n] = letraC
    print(f"palabra/s a adivinar: {palabra_guardada}")
    if l not in palabra:
        print(f"la letra {l} no se encuentra!")
        intentos -= 1
    if(intentos == 0):
        print(f"GAME OVER!")
        game_on = False
    elif "_" not in palabra_guardada:
        print(f"Ganaste!\nLa palabar es: {palabra}")
        game_on = False
    
