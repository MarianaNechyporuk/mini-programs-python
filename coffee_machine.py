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
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resources_enough(order_ingredients):
    for item in order_ingredients:
      if order_ingredients[item] >= resources[item]:
        print(f"Sorry there is not enough {item}")
        return False
    return True

def coins():
    print("Please insect coins.")
    total = int(input("Hor many quarters?: ")) * 0.25
    total += int(input("Hor many dimes?: ")) * 0.1
    total += int(input("Hor many nickles?: ")) * 0.05
    total += int(input("Hor many pennies?: ")) * 0.01
    return total

def is_money_enough(money_recieved, drink_cost):
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry. Not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print('\n'.join("{}: {}".format(k, v) for k, v in resources.items()))
        print(f"money :${profit}")
    else:
        drink = MENU[choice]
        if is_resources_enough(drink["ingredients"]):
            payment = coins()
            if is_money_enough(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
