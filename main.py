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

money = 0.0


def report():
    unit = 'ml'
    for item in resources:
        if item == 'coffee':
            unit = 'g'
        print(f"{item:6}: {resources[item]}{unit}.")
    print(f"{'Money':6}: ${money}")


def is_resource_sufficient(order_ingredients):
    for ingredient in order_ingredients:
        if resources[ingredient] < order_ingredients[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def process_coins():
    coins = {'quarters': 0.25, 'dimes': 0.1, 'nickels': 0.05, 'pennies': 0.01}
    total = 0.0
    for coin in coins:
        invalid = True
        while invalid:
            inserted = input(f"How many {coin}: ")
            if inserted.isdigit():
                total += int(inserted)
                invalid = False
            else:
                print("Input only integer!")
                continue
    return round(total, 2)


def is_transaction_successful(paid, price):
    if paid > price:
        return True
    else:
        print("Sorry that's not enough money. Your money is refunded.")
        return False


def make_coffee(order, order_ingredients):
    for ingredient in order_ingredients:
        resources[ingredient] -= order_ingredients[ingredient]
    print(f"Here is your {order}. Enjoy!")


is_on = True
while is_on:
    choice = input(f"What would you like {'/'.join(MENU)}? ")
    if choice == 'off':
        print("Turning off...")
        is_on = False
    elif choice == 'report':
        report()
    elif choice not in MENU:
        continue
    else:
        if is_resource_sufficient(MENU[choice]['ingredients']):
            paid = process_coins()
            if is_transaction_successful(paid, MENU[choice]['cost']):
                change = round(paid - MENU[choice]['cost'], 2)
                # global money
                money += MENU[choice]['cost']
                print(f"Here is ${change} in change.")
                make_coffee(choice, MENU[choice]['ingredients'])
