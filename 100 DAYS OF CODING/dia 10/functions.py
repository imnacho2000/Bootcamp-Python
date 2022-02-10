import art
import os

# def format_name(f,s):
#     name = f.title() + " " + s.title()
#     return name

# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
        
# def days_in_month(y,m):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
#     if(is_leap(y)): 
#         month_days[1] = 29 
#         return(month_days[m - 1])
#     return(month_days[m - 1])

def bienvenida():
    print(art.logo)
    
def division(n1,n2):
    return n1 / n2

def suma(n1,n2):
    return n1 + n2

def resta(n1,n2):
    return n1 - n2

def multi(n1,n2):
    return n1 * n2
    

operacions = {
    '/': division,
    '+': suma,
    '-': resta,
    '*': multi,
}

def op():
    for i in operacions:
        print(i)
  
    
def operaciones(n1,operacion,n2):
    if(operacion in operacions):
        operacionARealizar = operacions[operacion]
        return operacionARealizar(n1,n2)
    return (f"Operacion invalida.")
    
def limpiarPantalla():
    os.system('cls')


def calculator():
    bienvenida()
    n1 = int(input("Cual es el primer numero?: "))
    op()
    operacion = input("Ingrese operacion a realizar: ") 
    n2 = int(input("Cual es el segundo numero?: "))
    result =  operaciones(n1 = n1, operacion = operacion, n2 = n2)
    print(f"Resultado de {n1} {operacion} {n2} = {result}")
    seleccion = input(f"Ingrese Y para continuar calculando con el resultado {result} o N para realizar una nueva operacion: ")
    while(seleccion == "Y"):
        n1 = result
        op()
        operacion = input("Ingrese operacion a realizar: ") 
        n2 = int(input("Cual es el segundo numero?: "))
        result = operaciones(n1 = n1,operacion = operacion,n2 = n2)
        print(f"Resultado de {n1} {operacion} {n2} = {result}")
        seleccion = input(f"Ingrese Y para continuar calculando con el resultado {result} o N para realizar una nueva operacion: ")
    else:
        limpiarPantalla()
        calculator()

