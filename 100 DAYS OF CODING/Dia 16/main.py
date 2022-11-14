from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_Cafe = Menu()
coffe_Machine = CoffeeMaker()
money_machines = MoneyMachine()

seleccion = input(f"Que cafe desea hacer?({menu_Cafe.get_items()}): ")
apagar_maquina = False
while(apagar_maquina != True):
    if seleccion == "report":
        coffe_Machine.report()
        apagar_maquina = True
    else:
        cafe = menu_Cafe.find_drink(seleccion)
        if(coffe_Machine.is_resource_sufficient(cafe)):
            if(money_machines.make_payment(cafe.cost)):
                coffe_Machine.make_coffee(cafe)
            else:
                apagar_maquina = True
        else:
            apagar_maquina = True
    if(apagar_maquina == False):
        seleccion = input(f"Que cafe desea hacer?({menu_Cafe.get_items()}): ")
