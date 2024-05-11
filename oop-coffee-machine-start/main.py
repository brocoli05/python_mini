from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# create related objects
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

machine_off = False
while not machine_off:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ").lower()
    if choice == "off":
        machine_off = True
    # TODO 1: Print report.
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        # TODO 2: Check resources sufficient?
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            # TODO 3: Process coins
            if money_machine.make_payment(drink.cost):
            # TODO 4: Check transaction successful?
                # TODO 5: Make coffee.
                coffee_maker.make_coffee(drink)
