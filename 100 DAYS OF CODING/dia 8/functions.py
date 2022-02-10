alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def greet(name):
#     print(f"Hola {name}")
#     print("adios!")
#     print("saludos!")

# def greet_with(name,ubicacion):
#     print(f"{name} se encuentra en {ubicacion}")

def calcularLatas(altura,ancho,baldeCobertura):
    print(f"Se necesita {round((altura * ancho) / 5)} baldes")

def esPrimo(number):
    aux = 0
    for n in range(1,number):
        if(number % n == 0):
            aux += 1
    if(aux > 2): 
        return False
    return True

def cesar(text,shift,descrp):
    textCifrado = ""
    for n in text:
        if ((n in alphabet)  and (descrp == "codear")):
            textCifrado += str(alphabet[alphabet.index(n) + shift])
        elif((n in alphabet)  and (descrp == "decoodear")):
            textCifrado += str(alphabet[alphabet.index(n) - shift])
        else:
            textCifrado += text
    print(f"Aqui esta su mensaje = {textCifrado}")
    
def vovlerAEjecutar():
    decision = input("Quieres volver a ejecutar?, Y o N: ")
    if(decision == "Y"):
        return True
    elif(decision == "N"):
        return False
    print("Comando desconocido")

    
         
    