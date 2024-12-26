from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_running = True

while machine_running:
    options = Menu().get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        machine_running = False
    elif choice == "report":
        CoffeeMaker().report()
        MoneyMachine().report()
    else:
        drink = Menu().find_drink(choice)
        if CoffeeMaker().is_resource_sufficient(drink) and MoneyMachine().make_payment(drink.cost):
            CoffeeMaker().make_coffee(drink)

#TODO 1: Print report.
#Lines 15 and 16.
#TODO 2: Check resources are sufficient.
#Line 19.
#TODO 3: Process coins.
#Line 19.
#TODO 4: Check transaction is successful.
#Line 19.
#TODO 5: Make coffee.
#Line 20.