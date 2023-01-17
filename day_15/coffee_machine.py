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

profit = 0
resource = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    # is_enough = True or(1)
    for item in order_ingredients:
        if order_ingredients[item] >= resource[item]:
            print(f"Sorry there is not enough {item}")
            # is_enough = False or(1)
            return False
    # return is_enough or(1)
    return True


def process_coins():
    """Return the calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters: ")) * 0.25
    total += int(input("how many dimes: ")) * 0.10
    total += int(input("how many nickles: ")) * 0.05
    total += int(input("how many pennies: ")) * 0.01
    return total


def is_transaction_sucessful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is {change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resource[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} . Enjoy!")


on = True

while on:
    choice = input("What would you like? (expresso/latte/cappuccino): ")
    if choice == "off":
        on = False
    elif choice == "report":
        print(f"Water: {resource['water']}ml")
        print(f"Milk: {resource['milk']}ml")
        print(f"Coffee: {resource['coffee']}ml")
        print(f"Money: {profit}$")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_sucessful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
