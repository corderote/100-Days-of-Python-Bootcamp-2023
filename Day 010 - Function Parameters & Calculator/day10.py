import sys
import os
import calculator_art
# ----------------------------------------------------------------------------- #
# Functions Part 3

# We have already seen what functions are, and how to define and trigger them.
# After that, we learned how to use the input parameters inside the parenthesis
# of our functions to give them more utility and flexibility.
# Now we are going to put the cherry on top of the functions learning curve by 
# giving our functions something to output from them.

# Functions with Outputs
# Sometimes we will need to keep working with a variable from inside a function
# ----------------------------------------------------------------------------- #
# once we leave its scope or space. In such cases, we use the keyword 'return'.
# return allows us to add an output to our functions, we just need to add the 
# variable that we want to return after that keyword.
# This means, whatever we put as the result, replaces the point of the program 
# where we make the function call, allowing to save that data into a variable.
# The return keyword sets the end of a function or a block of code, all code 
# belonging to the same block that stays after that statement does not execute.


def my_function_with_output():
    function_output = 25
    return function_output
    print("This code will never be reached.")   # Warning expected here.


my_variable = my_function_with_output()
print(my_variable)


# Exercise 0 - Format Names:
def format_name(f_name, l_name):
    # We use .title() to convert our name variables into title case.
    formatted_name = f"{f_name} {l_name}".title()
    return formatted_name


my_name = format_name("name", "SURNAME")


# ----------------------------------------------------------------------------- #
# Exercise 1 - Days in Month 
# Create a function called days_in_month() which will take a year and a month 
# as inputs, it will use this information to work out the number of days in
# the month, then return that as the output.
def is_leap(year_to_check):
    if year_to_check % 4 == 0:
        if year_to_check % 100 == 0:
            if year_to_check % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year_to_check, month_to_check):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days = month_days[month_to_check-1]
    if is_leap(year_to_check) and month_to_check == 2:
        total_days += 1
    return total_days 


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

# ----------------------------------------------------------------------------- #
# Docstrings
# Docstrings are pieces of code documentation that we attach to our functions 
# or code to give more information to possible other users.
# Whe we add them to our functions, they come below the function declaration.
# The docstring documentation goes between triple quotation marks (""")


def my_function_documented(f_name, f_surname):
    """
    This function prints a name and a surname titled format case.
    It has the name and the surname as inputs.
    """
    print(f"{f_name} {f_surname}".title())


my_function_documented("NAME", "surname")
# ----------------------------------------------------------------------------- #
# Docstring documentation can also be used as a normal code documentation 
# allowing multiple lines of documentation in one single block.
""" 
Here we can write as much as we want and it will still be considered a comment 
in our code. With this we do not have to worry about really long comments being 
cut with the sliders inside our code. 

WARNING: This works as long as we do not assign our triple quotation mark to a 
variable.

Python documentation tries to avoid docstring documentation as it may lead to 
confusion between code and documentation and for this reason is easy to miss.
"""
# This type of comment is way easier to differentiate from the code itself.

# ----------------------------------------------------------------------------- #
# Return vs Print
# What return allows us to do is to work with the variables that we manipulate 
# inside our functions, giving us more flexibility to use them.
# Just printing them will not save that data inside a variable and once the
# function is done with the block of code from that function we can no longer 
# work or get any information from inside of it. 


# ----------------------------------------------------------------------------- #
# Recursion
# Recursion is a method to 'restart' our function at any point of from our own 
# function by making it call itself.
# As with other looping options like 'while' and 'for' loops, we have to be 
# careful and not create an infinite loop with recursive functions.
# Make sure to always create an exit or end to your functions or programs.
def recursive_function(counter_value):
    given_condition = input(f"Counter: {counter_value}. " 
                            "Type 'yes' to add to the counter, " 
                            "or 'no' to exit the program.\n")
    given_condition = given_condition.lower()
    if given_condition == "yes":
        counter_value += 1
        recursive_function(counter_value)
    else:
        print("Bye!")

# ----------------------------------------------------------------------------- #
# Exercise 2 - Calculator


def clear_screen():
    """ 
    A function that clears our terminal screen.
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
