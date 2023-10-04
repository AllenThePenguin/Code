# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

money = 0
off = False

while not off:
    successful_purchase = True
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    elif user_choice == "off":
        off = True
    else:
        for ingredient in MENU[user_choice]['ingredients']:
            if MENU[user_choice]['ingredients'][ingredient] > resources[ingredient]:
                print(f"There is not enough of {ingredient}.")
                successful_purchase = False

        if successful_purchase:
            quarters = int(input("How many quarters? "))
            dimes = int(input("How many dimes? "))
            nickels = int(input("How many nickels? "))
            pennies = int(input("How many pennies? "))
            inserted_money = 0.25 * quarters + 0.1 * dimes + 0.05 * nickels + 0.01 * pennies
            if inserted_money < MENU[user_choice]['cost']:
                print("That's not enough money. Money refunded.")
                successful_purchase = False

        if successful_purchase:
            for ingredient in resources:
                resources[ingredient] -= MENU[user_choice]['ingredients'][ingredient]
            change = round(inserted_money - MENU[user_choice]['cost'], 2)
            money += MENU[user_choice]['cost']
            print(f"Your change is ${change}. Enjoy your {user_choice}!")