from art import logo
from art import vs
from game_data import data
import os
import random

def limpiarPantalla():
    os.system("cls")

def bienvenida():
     print(f"{logo}\nBienvenido a Higher or Lower Game!\nUn juego frustrantemente adictivo de mayor o menor seguidores en instagram.\nLos datos se basan la cantidad de seguidores desde el 2022 .\n")
    
adivina_user = {}
adivina_cpu = {}

def adivinar():
    return random.choice(data)

def nombreDiccionario(diccionario):
    return (f"Nombre: {diccionario['name']}, descripcion: {diccionario['description']}, pais: {diccionario['country']}")

def comparacion(select,AB):
    if(select['follower_count'] < AB['follower_count']):
        return True
    return False

def jugar():
    count = 0
    game_over = False
    A = adivinar()
    B = adivinar()
    bienvenida()
    while(game_over != True):
        select = input(f"A para: {nombreDiccionario(A)}\n{vs}\nB para: {nombreDiccionario(B)}\nEleccion: ")
        if(select == "B"):
            select = B
            B = adivinar()
            game_over = comparacion(select,A)
        elif(select == "A"):
            select = A 
            A = adivinar()
            game_over = comparacion(select,B)
        else:
            print("Opcion invalida!")
            limpiarPantalla()
            game_over = True
        if (game_over == True):
            seleccion = input(f"Elegiste mal!, tu puntuacion: {count}\nQuieres jugar de nuevo? Y o N: ")
            if (seleccion == "Y"):
                limpiarPantalla()
                jugar()
            else:
                print(f"¡Bay!.")
                limpiarPantalla()
                game_over = True
        else:
            count += 1
            print(f"\nCorrecto!, Puntuacion: {count}\n")
                

    