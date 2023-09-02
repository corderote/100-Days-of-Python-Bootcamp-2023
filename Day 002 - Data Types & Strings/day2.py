# ----------------------------------------------------------------------------- #
# Data types.

# #1 - Strings
# You can split its content in characters. 
print("Hello"[0])
print("Hello"[3])
print("Hello"[-1])
# Remember, programmers start to count at 0. That's why to get the 'H' we put
# the 0 in the brackets.
# Subscripting. -> Pulling out a particular element from a string. 
# The number between the brackets sets what you are pulling.
print("123" + "345")

# #2 - Integer
integer = 123
print(123 + 345)

# #3 - Float (Floating point number)
float_num = 3.14159

# #4 - Boolean
true_bool = True
false_bool = False

# ----------------------------------------------------------------------------- #
# Type Error
# Type Checking

length = len(input("What is your name? "))
# type() allows us to check types of variables we are working with.
length_type = type(length)
print(length_type)

# Type Casting
# ----------------------------------------------------------------------------- #
# print("Your name has " + length + "characters. ")
# The line of code above returns an TypeError in length. To fix it we use the
# str() function, it returns the variable used as input formatted to a string.
length_string = str(length)
print("Your name has " + length_string + " characters. ")

# To convert to an int datatype we use the int() function.
# To convert to a float datatype we use the float() function.

# Exercise 1 - Data Types
# Write a program that adds the digits in a two digits number.
# e.g. if the input was 35, then the output should be 3 + 5 = 8
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
# Write your code below this line 👇
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
print(first_digit + second_digit)

# ----------------------------------------------------------------------------- #
# Mathematical operations.
add = 3 + 5       # Addition
sub = 7 - 4       # Subtraction
mul = 9 * 2       # Multiplication
div = 6 / 3       # Division > Returns a float.
mod = 7 % 2       # Modulo > Returns the reminder of the division.
f_div = 8 // 3    # Full division. > Returns just the int value of the division.
exp = 2 ** 3      # Exponent

# Order of execution (P.E.M.D.A.S.)
# () Parenthesis
# ** Exponents
#  * Multiplications 
#  / Divisions
#  + Additions
#  - Subtractions
# At the same level of priority the execution will be done from left to right 
# operations. 
print(3*3+3/3-3)    # This prints 7.0
print(3*(3+3/3-3))  # This prints 3.0

# ----------------------------------------------------------------------------- #
# Exercise 2 - BMI Calculator.
# Write a program that calculates the Body Mass Index (BMI) from a user's 
# weight and height.
# The BMI is a measure of someone's weight taking into account their height.
# e.g. If a tall person and a short person both weigh the same amount, 
#      the short person is usually more overweight.
# The BMI is calculated by dividing a person's weight (in kg) by the square 
# of their height (in m)

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bmi = float(weight)/float(height)**2
print(bmi)
print(int(bmi))

# ----------------------------------------------------------------------------- #
# Number manipulation and F-strings
# The round() function allows us to round a decimal value.
# We can use a second input value to specify a precision of such decimal 
# digits. 
print(round(3.14159, 4))    
tmp_value = 3
tmp_value += 5  # value = value + 5
tmp_value -= 2  # value = value - 2
tmp_value /= 3  # value = value / 3
tmp_value *= 4  # value = value * 4

# f-string:
# By using f before the brackets you can convert a string into f-string
# This allows us to handle other datatypes easier inside the strings. 
print(f"Your current value is {tmp_value}")

# Exercise 3 - Life in Weeks
# Create a program using maths and f-Strings that tells us how many days, 
# weeks, months we have left if we live until 90 years old.
# It will take your current age as the input and output a message with our 
# time left in this format: You have x days, y weeks, and z months left.
# Where x, y and z are replaced with the actual calculated numbers.

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
age_as_int = int(age)
years_left = 90 - age_as_int
m_left = years_left * 12
w_left = years_left * 52
d_left = years_left * 365
print(f"You have {d_left} days, {w_left} weeks, and {m_left} months left.")

# ----------------------------------------------------------------------------- #
# DAY 2 Project. Tip Calculator.

# Create a greeting for the program.
print("Welcome to the tip calculator.\n")
# Collect all the data required from the user and set their datatypes.
total_bill = float(input("What was the total bill? "))
tip_percentage = float(input("What percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))

# Calculate the price with the tip and the price that each person has to pay.
bill_with_tip = round(total_bill * (1+(tip_percentage/100)), 2)
price_per_person = round(bill_with_tip / people, 2)
# Here we use format nomenclature to make sure it always displays 2 decimal 
# digits.
price_per_person = "{:.2f}".format(price_per_person) 

# Print the result.
print(f"Each person should pay: {price_per_person}")
# ----------------------------------------------------------------------------- #
