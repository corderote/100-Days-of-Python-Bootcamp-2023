# ----------------------------------------------------------------------------- #
# Coffee Machine Project.
# ----------------------------------------------------------------------------- #
# Requirements:
# 1. Print Report. Prints the resources that the machine currently has.
# 2. Ask for a drink, give drinks and change.
# 3. Give money back if there are no resources available.
# 4. Process coins. Ask for them and check value, refund if not enough money.
# 5. Check transaction successful.

import os
import sys

MAX_MACHINE_COINS = 100

coffee_machine_resources = {
    "current": {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        "money": 0.0,
    },
    "total": {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    },
}

COFFEE_MACHINE_MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
    },
}

COFFEE_MACHINE_COMMANDS = ["report", "refill", "off"]

COINS_VALUE = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
}


def clear_screen():
    """
    This function clears our terminal screen.
    It has dependencies from the system and the operating system that we are
    using, this may cause ERROR.
    NOTE: If ERROR here, check 'sys.platform' and 'os.system' in the API.
    """
    if sys.platform == 'win32':
        os.system('cls')
    elif sys.platform == 'linux':
        os.system('clear')
    elif sys.platform == 'darwin':
        os.system('clear')


def get_full_commands_list():
    full_commands_list = []
    for command in COFFEE_MACHINE_COMMANDS:
        full_commands_list.append(command)
    for coffee_type in COFFEE_MACHINE_MENU:
        full_commands_list.append(coffee_type)
    return full_commands_list


def ask_user_for_command(available_commands_list):
    user_answer = ""
    while user_answer.lower() not in available_commands_list:
        user_answer = input("What would you like?"
                            "(Espresso/Latte/Cappuccino)\n")
        if user_answer.lower() not in available_commands_list:
            print(f"ERROR: Invalid command - '{user_answer}'\n"
                  "Please try again.")
    return user_answer


def ask_user_for_coins():
    monetary_value = 0.0
    for coin_type in COINS_VALUE:
        num_of_coins = -1
        coins_value_str = format(COINS_VALUE[coin_type], '.2f')
        while num_of_coins < 0 or num_of_coins > MAX_MACHINE_COINS:
            try:
                num_of_coins = int(input(f"Insert number of {coin_type} "
                                         f"(${coins_value_str}): "))
                if num_of_coins < 0 or num_of_coins > MAX_MACHINE_COINS:
                    print("Value Error: Expected other value. [0-99]")
            except ValueError:
                print("Value Error: Invalid Input. "
                      "Expected integer value. [0-99]")
                num_of_coins = -1
        monetary_value += COINS_VALUE[coin_type] * num_of_coins
    return monetary_value


def set_user_coffee(coffee_type, users_monetary_value):
    coffee_cost = COFFEE_MACHINE_MENU[coffee_type]["cost"]
    coffee_change = users_monetary_value - coffee_cost
    print(f"Coffee cost: ${format(coffee_cost, '.2f')}.\n"
          f"Money inserted: ${format(users_monetary_value, '.2f')}.")
    if coffee_change < 0.0:
        print("Sorry that's not enough money."
              f"${format(users_monetary_value, '.2f')} refunded.")
    else:
        water_used = COFFEE_MACHINE_MENU[coffee_type]["ingredients"]["water"]
        milk_used = COFFEE_MACHINE_MENU[coffee_type]["ingredients"]["milk"]
        coffee_used = COFFEE_MACHINE_MENU[coffee_type]["ingredients"]["coffee"]
        coffee_machine_resources["current"]["water"] -= water_used
        coffee_machine_resources["current"]["milk"] -= milk_used
        coffee_machine_resources["current"]["coffee"] -= coffee_used
        coffee_machine_resources["current"]["money"] += coffee_cost
        print(f"Enjoy your {coffee_type}! "
              f"Here is ${format(coffee_change, '.2f')} in change.")


def coffee_machine_report():
    current_water = coffee_machine_resources["current"]["water"]
    current_milk = coffee_machine_resources["current"]["milk"]
    current_coffee = coffee_machine_resources["current"]["coffee"]
    current_money = coffee_machine_resources["current"]["money"]
    print("Coffee Machine Resources: ")
    print(f"Water: {current_water}ml.")
    print(f"Milk: {current_milk}ml.")
    print(f"Coffee: {current_coffee}ml.")
    print(f"Money: ${format(current_money, '.2f')} .")


def coffee_machine_refill():
    total_water = coffee_machine_resources["total"]["water"]
    total_milk = coffee_machine_resources["total"]["milk"]
    total_coffee = coffee_machine_resources["total"]["coffee"]
    coffee_machine_resources["current"]["water"] = total_water
    coffee_machine_resources["current"]["milk"] = total_milk
    coffee_machine_resources["current"]["coffee"] = total_coffee


def check_resources(coffee_type):
    resources_needed = []
    current_water = coffee_machine_resources["current"]["water"]
    current_milk = coffee_machine_resources["current"]["milk"]
    current_coffee = coffee_machine_resources["current"]["coffee"]
    needed_water = COFFEE_MACHINE_MENU[coffee_type]["ingredients"]["water"]
    needed_milk = COFFEE_MACHINE_MENU[coffee_type]["ingredients"]["milk"]
    needed_coffee = COFFEE_MACHINE_MENU[coffee_type]["ingredients"]["coffee"]
    if current_water < needed_water:
        resources_needed.append("water")
    if current_milk < needed_milk:
        resources_needed.append("milk")
    if current_coffee < needed_coffee:
        resources_needed.append("coffee")
    if resources_needed:
        return resources_needed
    else:
        return None


def ask_for_another_coffee():
    another_coffee = ""
    while another_coffee != "yes" and another_coffee != "no":
        another_coffee = input("\nDo you want another coffee? "
                               "Type 'yes' or 'no'.\n")
        another_coffee = another_coffee.lower()
    if another_coffee == "yes":
        return True
    else:
        return False


def coffee_machine_program():
    clear_screen()
    commands_list = get_full_commands_list()
    user_command = ask_user_for_command(commands_list)
    if user_command in COFFEE_MACHINE_COMMANDS:
        if user_command == "report":
            coffee_machine_report()
        elif user_command == "refill":
            coffee_machine_refill()
        elif user_command == "off":
            return 0
    elif user_command in COFFEE_MACHINE_MENU:
        insufficient_ingredients = check_resources(user_command)
        if insufficient_ingredients is None:
            user_coins_value = ask_user_for_coins()
            set_user_coffee(user_command, user_coins_value)
        else:
            for thing in insufficient_ingredients:
                print(f"Sorry, there is not enough {thing}.")
            print("Refill is required.")

    if ask_for_another_coffee():
        coffee_machine_program()


coffee_machine_program()

# TIPS:
# 1. format allows you to convert a float into a string with the decimal
# values that you desire.
# 2. check the API for the try and except statements and how can they help
# you ensure that the values that the user inputs are correct.
# ----------------------------------------------------------------------------- #
