# ----------------------------------------------------------------------------- #
# Print Function: 
# ----------------------------------------------------------------------------- #
# Exercise 1: Printing Exercise: 
# The print() function prints its content on the console.
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

# This also works.
print("Day 1 - Print Function\nFunction Declaration:\nprint('what to print')")
# This also works.
print("Day 1 - Python Print Function\n"
      + "The function is declared like this:\n"
      + "print('what to print')")

# The last print uses single quotes to allow the sentence inside the print 
# multiple use case scenario to work properly.
# You can enclose the strings inside both single or double quotes.

# ----------------------------------------------------------------------------- #
# Exercise 2: Debugging Practise:
# Fix the code below

# print(Day 1 - String Manipulation)
# print("String Concatenation is done with the "+" sign.")
# print('e.g. print("Hello " + "world")')
# print(("New lines can be created with a backslash and n.")

print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

# ----------------------------------------------------------------------------- #
# Input Function: 
# The input() function prints its content on the console and allows the user to
# introduce something after it uses what the users type as a return value. 
# The return arrives as a string datatype.

# print vs input.
print("What is your name?\n")
print("Execution 1 Ends.")

input("What is your name?\n")
print("Execution 2 Ends.")

# Nested functions:
print("Hello " + input("What is your name?\n"))

# ----------------------------------------------------------------------------- #
# Exercise 3: Input Function:
# Count the letters from the input of a program. 
print(len(input("What is your name? "))) 

# ----------------------------------------------------------------------------- #
# Variables: 

name = input("What is your name? ")
# The len() function returns the length of a string variable.
length = len(name)
print(length)

# ----------------------------------------------------------------------------- #
# Exercise 4: Variable Naming Quiz:

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
# Write your code below this line 👇

# Save the value from 'a' in a 'tmp' variable.
tmp = a
# Then switch the value of 'a' to equal the value of 'b'.
a = b
# Finish by switching the value of 'b' with the original value of 'a' 
# stored in 'tmp'.
b = tmp     

# Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)

# Be consistent with the naming of the variables.
# Rule #1 - Make sure it makes sense to the readers.
# Use underscores to use multiple words as a variable (e.g.: user_name)

# ----------------------------------------------------------------------------- #
# DAY 1 Project. 

# 1. Create a greeting for your program.
print("Welcome to the Band Name Generator.")
# 2. Ask the user for the city that they grew up in.
city = input("What's name of the city you grew up in?\n")
# 3. Ask the user for the name of a pet.
pet = input("What's your pet's name?\n")
# 4. Combine the name of the city and the pet to
print("Your band name could be: " + city + " " + pet)

# 5. Make sure the input cursor shows on a new line. (Using '\n')
# ----------------------------------------------------------------------------- #
