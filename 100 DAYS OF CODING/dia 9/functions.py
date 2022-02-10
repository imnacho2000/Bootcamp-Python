import os
apostadores = {
}

def clear_console():
    os.system('clear')

def apostar():
    n = input("Desea apostar?, Y o N: ")
    if(n == "N"):
        print("Adios!.")
    elif(n == "Y"):
        while(n != "N"):
            name = input("Ingrese nu nombre: ")
            valor = float(input("Ingrese suma: $"))
            apostadores[name] = valor
            n = input("Hay otro apostador? Y o N: ")
            if(n == "N"):
                print("Ok!\n")
                buscarMax()
                print("\nAdios!")
            else:
                clear_console()
                print("A APOSTAR!")           
    else:
        print("Comando desconocido")

def buscarMax():
    maximo = max(apostadores, key = apostadores.get)
    print(f"El maximo apostador es: {maximo} con ${apostadores[maximo]}")
    
