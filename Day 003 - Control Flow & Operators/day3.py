# ----------------------------------------------------------------------------- #
# Condition Statements.

# a == b  > Equal
# a != b  > Not equal
# a < b   > Lower
# a > b   > Greater
# a <= b  > Lower or equal
# a >= b  > Grater or equal
 
# if / Else
condition = True
if condition:
    # Do something if condition is true.
    print("Condition is True.\n")
else: 
    # Do other thing if condition is false.
    print("Condition is False.\n")

# ----------------------------------------------------------------------------- #
# Exercise 1 - Odd or Even
# Write a program that works out whether if a given number is an odd or an 
# even number.

# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
decimal_part = number % 2
if decimal_part != 0:
    print("This is an odd number.")
else:
    print("This is an even number.")

# Nested if / Else statements & elif statements
condition_1 = True
condition_2 = True

if condition:
    if condition_2:
        print("Both conditions are True.")
    else:
        print("Just condition 1 is True.")
else:
    if condition_2:
        print("Just condition 2 is True.")
    else:
        print("Both conditions are False.")

# elif -> Multiple condition states. 
value = 100
if value <= 50:
    print("Value is under 50")
elif value <= 150:
    print("Value is under 150")
else: 
    print("Value is over 150")

# ----------------------------------------------------------------------------- #
# Exercise 2 - BMI Calculator 2.0
# Write a program that interprets the Body Mass Index (BMI) based on a user's 
# weight and height.

# It should tell them the interpretation of their BMI based on the BMI value.

# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bmi = float("{:.1f}".format(weight / height**2))

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30: 
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")

# ----------------------------------------------------------------------------- #
# Exercise 3 - Leap Year
# Write a program that works out whether if a given year is a leap year. 
# A normal year has 365 days, leap years have 366, with an extra day 
# in February. 
# This is how you work out whether if a particular year is a leap year.
#   on every year that is evenly divisible by 4 
#   **except** every year that is evenly divisible by 100 
#   **unless** the year is also evenly divisible by 400

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
leap = False

decimal_part_4 = year % 4
decimal_part_100 = year % 100
decimal_part_400 = year % 400

if decimal_part_4 == 0:
    if decimal_part_100 == 0:
        if decimal_part_400 == 0:
            leap = True
        else: 
            leap = False
    else:
        leap = True
else: 
    leap = False

if leap:
    print("Leap year.")
else: 
    print("Not leap year.")

# ----------------------------------------------------------------------------- #
# Exercise 4 - Pizza Order Practice

# Congratulations, you've got a job at Python Pizza. 
# Your first job is to build an automatic pizza order program.
# Based on a user's order, work out their final bill.

# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else: 
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: {bill}.")

# ----------------------------------------------------------------------------- #
# Logical Operators:
# Allow us to use multiple conditions on the same line of code. 
#  A and B both conditions have to be true in order to proceed.
#  A or B at least one of the conditions have to be truth in order to proceed.
#  not A inverts the value of the condition.

# ----------------------------------------------------------------------------- #
# Exercise 5 - Love Calculator.
# You are going to write a program that tests the compatibility between two 
# people. 
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in 
# the word TRUE occurs. 
# Then check for the number of times the letters in the word LOVE occurs. 
# Then combine these numbers to make a two digits number.

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
score_first_digit = 0
score_second_digit = 0

names_string = name1 + name2
names_string = names_string.lower()

score_first_digit += names_string.count('t')
score_first_digit += names_string.count('r')
score_first_digit += names_string.count('u')
score_first_digit += names_string.count('e')

score_second_digit += names_string.count('l')
score_second_digit += names_string.count('o')
score_second_digit += names_string.count('v')
score_second_digit += names_string.count('e')

print(score_first_digit)
print(score_second_digit)

score = int(str(score_first_digit) + str(score_second_digit))

print(score)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
# You can use a condition variable between '<' and '>' as one single 'between'
# condition.
elif 40 < score < 50:
    print(f"Your score is {score}, you are alright together.")
else: 
    print(f"Your score is {score}.")
# ----------------------------------------------------------------------------- #
