# ----------------------------------------------------------------------------- #
# Coffee Machine Project. Object-Oriented Programming version.
import menu
import coffee_maker
import money_machine

COFFEE_MACHINE_COMMANDS = ["report", "refill", "off"]

menu_object = menu.Menu()
coffee_maker_object = coffee_maker.CoffeeMaker()
money_machine_object = money_machine.MoneyMachine()


def ask_user_for_command():
    user_input_valid = False
    user_answer = input(f"What would you like? /{menu_object.get_items()}\n")
    if user_answer.lower() in COFFEE_MACHINE_COMMANDS:
        user_input_valid = True
    elif menu_object.find_drink(user_answer) is not None:
        user_input_valid = True
    else:
        user_input_valid = False
    if not user_input_valid:
        print(f"ERROR: Invalid command - '{user_answer}'. Please try again.")
        user_answer = ask_user_for_command()

    return user_answer.lower()


def oop_coffee_machine():
    user_command = ask_user_for_command()
    if user_command in COFFEE_MACHINE_COMMANDS:
        if user_command == "report":
            coffee_maker_object.report()
            money_machine_object.report()
        elif user_command == "refill":
            coffee_maker_object.refill()
        elif user_command == "off":
            return 0
    else:
        user_coffee = menu_object.find_drink(user_command)
        if coffee_maker_object.is_resource_sufficient(user_coffee):
            if money_machine_object.make_payment(user_coffee.cost):
                coffee_maker_object.make_coffee(user_coffee)
    oop_coffee_machine()


oop_coffee_machine()
# ----------------------------------------------------------------------------- #
