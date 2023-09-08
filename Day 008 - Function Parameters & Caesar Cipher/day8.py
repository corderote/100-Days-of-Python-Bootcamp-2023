import sys
import os
import caesar_art
import math
# ----------------------------------------------------------------------------- #
# Functions Part 2
# Set of instructions packed together inside a block of code that has a name to
# it, and when we need it we just need to call the name of the function. 
# When we call the function the program will search for the definition of it 
# and will run the block of code inside the definition.


def my_function():
    # Do stuff
    print("This")
    print("Is")
    print("My")
    print("Function")


# ----------------------------------------------------------------------------- #
# Exercise 0 - Greeting Function.
# Create a function that prints a greeting for the user. 
# This is just as a reminder of how functions work in python.
def greet():
    print("Hello fellow user.")
    print("Welcome to this function.")


greet()
# ----------------------------------------------------------------------------- #
# Functions with inputs.
# As we could need to call a function multiple times, it's normal to have the 
# need to use the same piece of code but altering a little its functionality. 
# For that purpose, we have a piece of information that we can add inside the
# parenthesis, these pieces are known as INPUTS.
# Inputs are defined and used in the function definition area. 
# Here we name them PARAMETERS. and they can have predefined values assigned.
# Once we call our function, we pass the INPUTS as ARGUMENTS.


def greet_with_name(name):  # 'name' here is the PARAMETER.
    print(f"Hello {name}.")
    print(f"Welcome to this function.")


greet_with_name("Pablo")    # 'Pablo' here is the ARGUMENT.
greet_with_name("C3PO")
greet_with_name(123)
# Here we have to differentiate a couple pieces of data:
# The PARAMETER, which is the name of the input when we define our function.
# The ARGUMENT, defines the value of the parameter when we call the function.


# ----------------------------------------------------------------------------- #
# Functions with more than one input.
# Taking the input system a step further, we are going to create a function
# that allows to have multiple parameters or inputs.
# To introduce multiple parameters to our function, we add them all together 
# inside the parenthesis separating them using comas ','.
def greet_with(name, location):
    print(f"Hello {name}.")
    print(f"What is it like in {location}?")


greet_with("Charlie", "Nowhere") 
# POSITIONAL ARGUMENTS: 
# ARGUMENTS are assigned to the PARAMETERS based on their calling position.

greet_with(name="Charlie", location="Nowhere") 
# KEYWORD ARGUMENTS: 
# ARGUMENTS bind to the PARAMETERS by assigning them when calling the function. 
# With keyword arguments you can rearrange the arguments, so we do not need to 
# follow the parameters name order that appears in the function definition.
# greet_with(location="Nowhere", name="Charlie") will also be a valid call.

# ----------------------------------------------------------------------------- #
# Exercise 1 - Paint Area Calculator
# You are painting a wall. 
# Instructions: One (1) can of paint covers five (5) square meters of wall.
# If you are given a random height and width of wall, calculate the surface 
# and the cans of paint you will need to buy.


# Write your code below this line 👇
def paint_calc(height, width, cover):
    square_meters_surface = height * width
    # We could use round() here, but math.ceil() is better. 
    # math.ceil() makes sure that even with 0.1 we round up to the next number.
    total_cans = math.ceil(square_meters_surface / cover) 
    print(f"You'll need {total_cans} cans of paint.")
# Write your code above this line 👆


# Define a function called paint_calc() so that the code below works.   
# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

# ----------------------------------------------------------------------------- #
# Exercise 2 - Prime Number Checker.
# Prime numbers can only be cleanly divided by themselves and 1.
# You need to write a function that checks whether if the number passed into it 
# is a prime number or not.


# Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    for n in range(2, number):
        if number % n == 0:
            is_prime = False

    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
# Write your code above this line 👆


# Do NOT change any of the code below👇
user_num = int(input("Check this number: "))
prime_checker(number=user_num)

# ----------------------------------------------------------------------------- #
# Exercise 3 - Caesar Cipher
# ----------------------------------------------------------------------------- #
# STEPS LIST
# 1- Create an 'encrypt()' function that takes a text and the shift as inputs.
# 2- Inside the encrypt function shift each letter of the text forwards in the 
#    alphabet and print the expected text.
# 3- Call the encrypt function and pass the user inputs. Test the code.
# 4- Create the decrypt() function that does the decryption process.
# 5- Can you use a unique function to solve both paths?
# 6- QoL Improvements: 
#    --> What happens with a huge shift number? 
#    --> What happens with numbers or other symbols? 
# ----------------------------------------------------------------------------- #
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
end_program = False


# This function clears our terminal screen. It has dependencies from the system
# and the operating system that we are using, this may cause ERROR. 
# NOTE: If ERROR here, check sys.platform and os.system on the python API.
def clear_screen():
    if sys.platform == 'win32':
        os.system('cls')
    elif sys.platform == 'linux':
        os.system('clear')
    elif sys.platform == 'darwin':
        os.system('clear')


def caesar_encrypt(plain_text, shift_amount, cipher_direction):
    # Handle the decryption shift.
    if cipher_direction == "decode":
        shift_amount *= -1
    # Check every letter in the message.
    end_text = ""
    for letter in plain_text:
        # If is part of the alphabet shift it.
        if letter in alphabet:
            alphabet_position = alphabet.index(letter)
            new_alphabet_pos = alphabet_position + shift_amount
            alphabet_lim = len(alphabet)-1
            # Check that the new alphabet position is always within bounds.
            while (new_alphabet_pos > alphabet_lim) or (new_alphabet_pos < 0):
                if new_alphabet_pos > alphabet_lim:
                    new_alphabet_pos -= len(alphabet)
                if new_alphabet_pos < 0:
                    new_alphabet_pos += len(alphabet)
            # Add the new letter to the now encrypted or decrypted text.
            new_letter = alphabet[new_alphabet_pos]
            end_text += new_letter
        # If is not part of the alphabet just add it to the end text.
        else:
            end_text += letter
    # Print the result.
    print(f"The {cipher_direction}d text is: {end_text}")


while not end_program:
    # Initialize Variables.
    direction = ""
    close_program = ""
    # Print Logo.
    clear_screen()
    print(caesar_art.logo)
    # Check if the user wants to encrypt a message or decrypt one.
    while direction != "encode" and direction != "decode":
        direction = input("Type 'encode' to encrypt,"
                          " type 'decode' to decrypt: ")
        direction = direction.lower()

    # Input the message and the shift that the user wants to apply.
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    # Call to the encrypting function.
    caesar_encrypt(text, shift, direction)
    # Check if the user wants to close the program or keep using it.
    while close_program.lower() != "yes" and close_program.lower() != "no":
        close_program = input("Close the program? Type 'yes' or 'no': ")
        if close_program == "yes":
            end_program = True
# ----------------------------------------------------------------------------- #
