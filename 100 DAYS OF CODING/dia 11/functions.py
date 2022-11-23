import art 
import random
import os 

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]




def bienvenido():
    print(art.logo)
    
def calculador(list):
    if (sum(list) == 21):
        return 0
    elif ((sum(list) > 21) & (11 in list)):
        list.remove(11)
        list.append(1)
    return sum(list)

def limpiarPantalla():
    os.system('cls')
    cartas() 

def deal_card():
    return random.choice(cards)

# def obtenerCarta(user,cpu,game_over):
#     si = input("Presione 'Y' para obtener otra carta o 'N' para dejar: ")
#     if(si == "Y"):
#         user.append(random.choice(cards))
#     elif(si == "N"):
#         game_over = True
#         if(sum(cpu) < 17):
#             cpu.append(random.choice(cards))
#         elif (calculador(user) == 0):
#             print(f"Tu ganas con: {user}, total {sum(user)}")
#             print(f"Computadora pierde con; {cpu}, total {sum(cpu)}")
#         elif(calculador(cpu) == 0):
#             print(f"Computadora gana con: {cpu}, total {sum(cpu)}")
#             print(f"Tu pierdes con; {user}, total {sum(user)}")
#         elif(calculador(cpu) > 21):
#             print(f"Tu ganas con: {user}, total {sum(user)}")
#             print(f"Computadora pierde con; {cpu}, total {sum(cpu)}")
#         elif(calculador(user) > 21):
#             print(f"Computadora gana con: {cpu}, total {sum(cpu)}")
#             print(f"Tu pierdes con; {user}, total {sum(user)}")
#         elif(calculador(user) > calculador(cpu)):
#             print(f"Tu ganas con: {user}, total {sum(user)}")
#             print(f"Computadora pierde con; {cpu}, total {sum(cpu)}")
#         elif(calculador(user) < calculador(cpu)):
#             print(f"Computadora gana con: {cpu}, total {sum(cpu)}")
#             print(f"Tu pierdes con; {user}, total {sum(user)}")
#         else:
#             print(f"Empataron con:  Computadora {cpu}, computadora total {sum(cpu)}\nTu {user}, total: {sum(user)}")

#     else:
#         print(f"Opcion invalida.")
 
def compare(user_score, computer_score):
    if(user_score == computer_score):
        return(f"Empate!")
    if (user_score == 0):
        return(f"Tu ganas!")
    elif(computer_score == 0):
        return(f"Computadora gana!")
    elif(computer_score > 21):
        return(f"Tu ganas!")
    elif(user_score > 21):
        return(f"Computadora gana" )
    elif(user_score > computer_score):
        return(f"Tu ganas!")
    else:
        return(f"Computadora gana!")
    
def cartas():
    bienvenido() 
    seleccion = input("Presione 'Y' para jugar o 'N' para no jugar: ")
    if (seleccion == "Y"):
        cpu_cards = []
        user_cards = []
        game_over = False
        for i in range(2):
            cpu_cards.append(deal_card())
            user_cards.append(deal_card())
        while(game_over != True):
            print(f"Primera carta de la computadora: {cpu_cards[0]}")
            total_user = calculador(user_cards)
            total_cpu = calculador(cpu_cards)
            if ((total_user == 0) | (total_cpu == 0) | (total_user > 21)):
                game_over = True
            else:
                print(f"Tus cartas: {user_cards}, valor parcial: {sum(user_cards)}") 
                si = input("Presione 'Y' para obtener otra carta o 'N' para dejar: ")
                if(si == "Y"):
                    user_cards.append(deal_card())
                elif(si == "N"):
                    game_over = True
                else:
                    print("Opcion invalida.")
        while((total_cpu != 0) and (total_cpu < 17)):
            cpu_cards.append(deal_card())
            total_cpu = calculador(cpu_cards)
        print(f"Cartas de compudatora: {cpu_cards}\nTus cartas: {user_cards}")
        print(compare(user_score = total_user, computer_score = total_cpu))
        print(f"Valor total de las cartas de la computadora: {sum(cpu_cards)}\nValor total de las cartas tuyas: {sum(user_cards)}")
        eleccion = input("Quieres reiniciar el juego?: Y o N: ")
        if(eleccion == "Y"):
            limpiarPantalla()
        else:
            print("Hasta luego!.")
    elif (seleccion == "N"):
        return("Juego finalizado!.")
    else:
        return("Opcion invalida.")
    
    
