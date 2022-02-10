MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

cambio = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def cantidades():
    """Realizo un reporte de lo que queda en la maquina y lo que se ingreso."""
    return(f"Queda: {resources['coffee']}gr cafe,\n{resources['milk']}ml leche,\n{resources['water']}ml agua,\nDinero ingresado ${cambio}.")


def cambio_monedas(dinero_ingresado,valor_cafe):
    """Evaluo el dinero ingresado y le retorno al cliente"""
    cambios = 0
    if(dinero_ingresado > valor_cafe):
        cambios  = dinero_ingresado - valor_cafe
        return (f"Su cambio: ${cambios}")
    elif(dinero_ingresado < valor_cafe):
        return (f"Lo lamento no cuenta con dinero suficiente :(")
    return (f"Cambio: ${cambios}")



def recursos_suficientes(ingredients):
    """Evaluo las cantidades y les realizo las operaciones indicadas por el cliente"""
    for n in ingredients:
        if(ingredients[n] > resources[n]):
            print(f"Lo siento no hay {n} suficiente.")
            return False
    return True

def restaDeIngredientes(ingredients):
    for n in ingredients:
        resources[n] -= ingredients[n]

def ingresar_dinero():
    """Le pido al usuario que ingrese la cantidad de dinero de c/u de las monedas aceptadas."""
    global cambio
    un_centavo = int(input("Cuantos centavos de dolar?: ")) * 0.01 
    decimo_centavo = int(input("Cuantos decimos centavos de dolar?: ")) * 0.10
    medio_dolar = int(input("Cuantos medio de dolar?: ")) * 0.5
    cuarto_dolar = int(input("Cuantos cuarto de dolar?: ")) * 0.25
    cambio = un_centavo + decimo_centavo + medio_dolar + cuarto_dolar

def obtenerItems():
    items = ""
    for n in MENU:
        items += n + "/"  
    return items

def buscarItem(item):
    if(item in MENU):
        return True
    return False

def pedir_cafe():
    global cambio
    apagar_maquina = False
    seleccion = input(f"Que tipo de cafe desea? ({obtenerItems()}): ")
    while(apagar_maquina != True):
        if(buscarItem(seleccion)):
            menu = MENU[seleccion]
            print(f"Si tenemos {seleccion}!")
            if(recursos_suficientes(menu['ingredients'])):
                print("Por favor ingrese el dinero.")
                ingresar_dinero()
                restaDeIngredientes(menu['ingredients'])
                print(cambio_monedas(cambio,menu['cost']))
            else:
                apagar_maquina = True           
        elif(seleccion == "reporte"):
            print(cantidades())
        else:
            apagar_maquina = True
            print(f"Opcion invalida.")
        if(apagar_maquina == False):
            print(f"Aqui esta su {seleccion} ☕.")
            seleccion = input("Que tipo de cafe desea? (espresso/latte/capuccino): ")
            cambio = 0
