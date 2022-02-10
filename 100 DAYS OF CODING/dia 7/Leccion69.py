import random
import palabras
import arte

print(arte.logo)
palabra = random.choice(palabras.word_list)
lista = []

for p in palabra:
    lista.append("_")
print("Palabra a adivinar: " + str(lista))
print("La solucion es: " + str(palabra))

final = False
error = 0
nivel = len(arte.stages)
while not final: 
    letra = input("Adivine una letra: ")
    for n in range(len(palabra)):
        letraC = palabra[n]
        if( letra.upper() == letraC):
            lista[n] = letra.upper()
        elif( letra.lower() == letraC):
            lista[n] = letra.lower()
    print("Palabra a adivinar: " + str(lista))
    if "_" not in lista:
        final = True
        print("Ganaste!.")
    elif letra not in lista:
        nivel -= 1
        if(nivel == 0):
            print(arte.stages[nivel])
            print(arte.gameOver)
            final = True
        else:
            print("La letra: " + str(letra) + " no se encuentra.")
            print(arte.stages[nivel])
        

