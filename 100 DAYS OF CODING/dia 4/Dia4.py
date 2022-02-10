import random
papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
tijera = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
piedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
seleccion = int(input("Elegi entre piedra 0, papel 1 o tijera 2 "))
if((seleccion > 2)| (seleccion < 0)):
    print("Seleccion fuera de rango")
else:
    cpu = random.randint(0,2)

    lista = [piedra,papel,tijera]

    seleccion_cpu = lista[cpu]

    seleccion_humano = lista[seleccion]

    if(seleccion_humano == seleccion_cpu):
        print(seleccion_humano)
        print("La computadora eligio: " + seleccion_cpu + "\n EMPATE!")
    elif(seleccion_humano != seleccion_cpu):
        if((seleccion_humano == piedra) and (seleccion_cpu == papel)):
            print(seleccion_humano)
            print("La computadora eligio: " + seleccion_cpu + "\n PERDISTE!")
        elif((seleccion_humano == papel) and (seleccion_cpu == piedra)):
            print(seleccion_humano)
            print("La computadora eligio: " + seleccion_cpu + "\n GANASTE!")
        elif((seleccion_humano == papel) and (seleccion_cpu == tijera)):
            print(seleccion_humano)
            print("La computadora eligio: " + seleccion_cpu + "\n PERDISTE!")
        elif((seleccion_humano == tijera) and (seleccion_cpu == papel)):
            print(seleccion_humano)
            print("La computadora eligio: " + seleccion_cpu + "\n GANASTE!")
        elif((seleccion_humano == tijera) and (seleccion_cpu == piedra)):
            print(seleccion_humano)
            print("La computadora eligio: " + seleccion_cpu + "\n PERDISTE!")
        elif((seleccion_humano == piedra) and (seleccion_cpu == tijera)):
            print(seleccion_humano)
            print("La computadora eligio: " + seleccion_cpu + "\n GANASTE!")