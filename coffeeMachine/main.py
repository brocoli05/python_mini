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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0

# Coins
QUARTERS = 0.25
DIMES = 0.10
NICKELS = 0.05
PENNIES = 0.01


# TODO 3: Print report.
def print_report(resources, money):
    # for ingredient in resources:
    #     quantity = resources[ingredient]
    #     print(f"{ingredient.capitalize()}: {quantity}")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


# TODO 4: Check resources sufficient?
def check_resources(order_ingredients):
    """ Returns True shen order can be made, False if ingredients are insufficient. """
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True
    # not_sufficient = False
    # ingredients = MENU[order_ingredients]["ingredients"]
    # if order_ingredients == "espresso":
    #     if ingredients["water"] < 50 or ingredients["coffee"] < 18:
    #         not_sufficient = True
    # elif order_ingredients == "latte":
    #     if ingredients["water"] < 200 or ingredients["milk"] < 150 or ingredients["coffee"] < 24:
    #         not_sufficient = True
    # elif order_ingredients == "cappuccino":
    #     if ingredients["water"] < 250 or ingredients["milk"] < 100 or ingredients["coffee"] < 24:
    #         not_sufficient = True
    #
    # if not_sufficient:
    #     print("Sorry there is not enough water.")


# TODO 5: Process coins.
def calculate_coins():
    """ Returns the total calculated from coins inserted. """
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * QUARTERS
    total += int(input("How many dimes?: ")) * DIMES
    total += int(input("How many nickles?: ")) * NICKELS
    total += int(input("How many pennies?: ")) * PENNIES

    return total
    # coin_quarters = int(input("How many quarters?: "))
    # coin_dimes = int(input("How many dimes?: "))
    # coin_nickles = int(input("How many nickles?: "))
    # coin_pennies = int(input("How many pennies?: "))
    #
    # total = coin_quarters * QUARTERS + coin_dimes * DIMES + coin_nickles * NICKELS + coin_pennies * PENNIES
    #
    # return total


# TODO 6: Check transaction successful?
def is_transaction_successful(money_received, drink_cost):
    """ Returns True when the payment is accepted, or False if money is insufficient. """
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} dollars in change.")
        global profit  # call the global variable
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
    # drink_cost = MENU[user_choice]["cost"]
    # if drink_cost < calculate_coins():
    #     print("Sorry that's not enough money. Money refunded.")
    # elif drink_cost == calculate_coins():
    #     print_report(resources, money)
    #     return money + drink_cost
    # else:
    #     change = calculate_coins() - drink_cost
    #     print(f"Here is ${round(change, 2)} dollars in change.")
    #     return money + drink_cost


# TODO 7: Make coffee
def make_coffe(drink_name, order_ingredients):
    """ Deduct the required ingredients from the resources. """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")


# TODO 1: Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
machine_off = False
while not machine_off:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    # money = 0

    # TODO 2: Turn off the Coffee Machine by entering “off” to the prompt.
    if user_choice == "off":
        machine_off = True
    elif user_choice == "report":
        print_report(resources, profit)
    else:
        user_menu = MENU[user_choice]
        if check_resources(user_menu["ingredients"]):
            user_paid = calculate_coins()
            if is_transaction_successful(user_paid, user_menu["cost"]):
                make_coffe(user_choice, user_menu["ingredients"])

        # user_menu_ingredients = user_menu["ingredients"]
        # print_report(user_menu_ingredients, money)
        # print(f"Here is your {user_choice}. Enjoy!")



