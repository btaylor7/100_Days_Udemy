MENU = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0},
}

resources = {
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
}


def process_coins():
    """Simulates the process where a user inserts coins and calculates the total."""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))  # 0.25
    dimes = int(input("How many dimes?: "))  # 0.10
    nickels = int(input("How many nickels?: "))  # 0.05
    pennies = int(input("How many pennies?: "))  # 0.01
    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return total


def check_resources(selection):
    """
    Checks if the machine has enough resources to make the selected drink.
    Returns True if the drink can be made, otherwise False.
    """
    for ingredient, required_amount in MENU[selection]["ingredients"].items():
        if resources.get(ingredient, 0) < required_amount:
            print(f"Sorry, there is not enough {ingredient}; order denied.")
            return False
    return True


def check_transaction(selection):
    """
    Checks if the user has inserted enough money for the selected drink.
    Returns True if the transaction is successful; False otherwise.
    """
    cost = MENU[selection]["cost"]  # The cost of the selected drink
    money_inserted = process_coins()

    if money_inserted >= cost:
        change = round(money_inserted - cost, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        return True

    print("Sorry, that's not enough money. Money refunded.")
    return False


def make_coffee(selection):
    """
    Makes the selected coffee if there are enough resources and the transaction is successful.
    Deducts the ingredients used from the resources.
    """
    if check_resources(selection) and check_transaction(selection):
        # Deduct ingredients from resources
        for ingredient, used_amount in MENU[selection]["ingredients"].items():
            resources[ingredient] -= used_amount

        print(f"Here is your {selection}. Enjoy!")
    else:
        print("Order could not be completed.")

def coffee_machine():
    """
    The main loop for the coffee machine.
    Lets the user order drinks or quit the machine.
    """
    machine_running = True

    while machine_running:
        # Prompt the user for an action
        choice = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()

        # Handle user input
        if choice == "off":
            print("Turning off the coffee machine. Goodbye!")
            machine_running = False
        elif choice == "report":
            print(f"Coffee levels are at {resources["coffee"]}.\nMilk levels are at {resources["milk"]}.\nWater levels are at {resources["water"]}.")
        elif choice in MENU:
            # Process drink order
            make_coffee(choice)
        else:
            print("Invalid choice. Please choose espresso, latte, cappuccino, or 'report'/'off'.")

coffee_machine()




