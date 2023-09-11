# ----------------------------------------------------------------------------- #
import sys
import os
import calculator_art


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


# Calculator Functions
def addition(addend_1, addend_2):
    summation = addend_1 + addend_2
    return summation


def subtraction(minuend, subtrahend):
    difference = minuend - subtrahend
    return difference


def multiplication(multiplier, multiplicand):
    product = multiplier * multiplicand
    return product


def division(dividend, divisor):
    fraction = dividend / divisor
    return fraction


# Global Variables.
continue_calculating = ""
result = 0

# Calculator Operations Dictionary. 
# With this should be easier to expand the program if we wanted to.
operations_dictionary = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division,
}

while continue_calculating != "exit":
    clear_screen()
    print(calculator_art.logo)
    # Ask for the first number or use it from the previous operation.
    if continue_calculating != "continue":
        number_1 = float(input("What is the first number? "))
    else:
        number_1 = result
        print(f"The first number is: {number_1}")

    # Ask for the operator
    operator = input("['+' '-', '*', '/'] Pick an operation: ")
    # Check valid operator.
    while (operator != "+" and 
           operator != "-" and 
           operator != "*" and 
           operator != "/"):
        print(f"ERROR: Invalid operator '{operator}'. Try again.")
        operator = input("['+' '-', '*', '/'] Pick an operation: ")

    number_2 = float(input("What is the second number? "))

    # We get the function value from our operations dictionary and use it.
    calculation_function = operations_dictionary[operator]
    result = calculation_function(number_1, number_2)

    print(f"{number_1} {operator} {number_2} = {result}")
    continue_calculating = input("Type 'continue' to continue calculating " 
                                 f"with {result}, type 'new' to start a new " 
                                 "calculation, or type 'exit' to close the "
                                 "program.\n")
    continue_calculating = continue_calculating.lower()

    while (continue_calculating != "continue" 
           and continue_calculating != "new" 
           and continue_calculating != "exit"):
        print(f"ERROR: Invalid command '{continue_calculating}'. Try again.")
        continue_calculating = input("Type 'continue' to continue calculating" 
                                     f" with {result}, type 'new' to start a " 
                                     "new calculation, or type 'exit' to "
                                     "close the program.\n")
        continue_calculating = continue_calculating.lower()
# ----------------------------------------------------------------------------- #
