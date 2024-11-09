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
def order():
    global tot
    global profit
    drink = input("What would you like? (espresso/latte/cappuccino):").lower()
    repo = True
    while repo:
        if drink == "report":
            for key, value in resources.items():
                print(key, value)
            print()
            print(f'Total money earned is : {profit}')
            repo=False
            order()
        else:
            for ingredient in MENU[drink]["ingredients"]:
                resources[ingredient] = resources[ingredient] - (MENU[drink]["ingredients"].get(ingredient))
            stock_name = []
            stock = []
            for key, value in resources.items():
                if value < 0:
                    stock_name.append(key)
                    stock.append(value)
                else:
                    pass
            if len(stock) > 0:
                for i in stock_name:
                    print(f'Sorry, there is not enough {i}')
                    for ingredient in MENU[drink]["ingredients"]:
                        resources[ingredient] = resources[ingredient] + (MENU[drink]["ingredients"].get(ingredient))
                    repo=False
                    order()
            else:
                quarters = 0.25
                dimes = 0.10
                nickles = 0.05
                pennies = 0.01
                qrt = int(input("How many quarters? "))
                dms = int(input("How many dimes? "))
                nicl = int(input("How many nickels? "))
                pen = int(input("How many pennies? "))
                tot = (qrt * 0.25) + (dms * 0.10) + (nicl * 0.05) + (pen * 0.01)
                if tot >= MENU[drink]["cost"]:
                    print(f'Here is your change: {(tot - MENU[drink]["cost"]):.2f}')
                    print(f'Enjoy your {drink}')
                    profit += MENU[drink]["cost"]
                    repo = False
                    order()
                else:
                    print("You dont have enough money")
order()
