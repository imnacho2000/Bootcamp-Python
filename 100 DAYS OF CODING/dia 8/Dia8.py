import functions
import art

print(art.logo)

direction = input("Escribi 'codear' para cifrar, escribi 'decoodear' para decifrar:\n")
if((direction == "codear") | (direction == "decoodear")):
    text = input("Escribe tu mensaje:\n").lower()
    shift = int(input("Escrbia el shift dek numero a utilizar:\n"))
    shift = shift % 26
    functions.cesar(text = text,shift = shift,descrp = direction)

    valor = functions.vovlerAEjecutar()

    if(valor  == False):
        print("Adios!.")
    else:
        while(valor == True):
            print("Volviendo a Ejecutar..")
            direction = input("Escribi 'codear' para cifrar, escribi 'decoodear' para decifrar:\n")
            text = input("Escribe tu mensaje:\n").lower()
            shift = int(input("Escrbia el shift dek numero a utilizar:\n"))
            shift = shift % 26
            functions.cesar(text = text,shift = shift,descrp = direction)  
            valor = functions.vovlerAEjecutar()
            if(valor == False):
                print("Adios!.")
else:
    print("Comando desconocido.")
