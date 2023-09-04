# ----------------------------------------------------------------------------- #
# Randomization and Python lists. 

# ----------------------------------------------------------------------------- #
# Random Function. 

# To add randomness to our programs python has its own module that uses the
# Mersenne Twister method to generate pseudorandom numbers.
# To use this module/lib, we need to add 'import random' at the beginning of
# our code.
# The 'import' keyword allows us to add different modules/dependencies to our 
# program. 
import random

# To call a function of the module we need to specify first the module. 
random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random()
print(random_float)

# ----------------------------------------------------------------------------- #
# Exercise 1 - Heads or Tails
# You are going to write a virtual coin toss program. 
# It will randomly tell the user "Heads" or "Tails".
# Remember to use the random module

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
# 🚨 Don't change the code above 👆 It's only for testing your code.

# Write the rest of your code below this line 👇
heads_or_tails = random.random()

if heads_or_tails > 0.5:
    print("Heads")
else: 
    print("Tails")

# ----------------------------------------------------------------------------- #
# Item Lists

# Data structures: Lists -> Allows us to store multiple pieces of data. 
# Lists syntax: Start with open and closes with square brackets '[]'
#               and in between the items separated by comas ','.

item_1 = "Item 1"
item_2 = "Item 2"
item_list = [item_1, item_2]

countries_from_europe = ["Spain", "Germany", "Italy", "France"]
# Here Spain is the first item of the list. 
# It will be associated with the index 0 if we want to use it from the list.
print(countries_from_europe[0])
# We can use a negative index to count from the end of the list. 
# In this case "France" is the last item of our list.
# We can access it by typing the index equal to -1.
print(countries_from_europe[-1])

# Also we can alter the items inside the list pretty easy accessing them.
countries_from_europe[3] = "Portugal"

# And using the append function we can add items to our list. 
countries_from_europe.append("France")

print(countries_from_europe)
# ----------------------------------------------------------------------------- #
# To add multiple items to a list we need to use 'extend()'.
# This function takes another list as an input nd add all its items to our own
# list.
countries_from_europe.extend(["Russia", "United Kingdom", "Ukraine", "Poland"])
print(countries_from_europe)

# Read the documentation for more information on how you can use and manipulate 
# lists. 
# https://docs.python.org/3/tutorial/datastructures.html

# ----------------------------------------------------------------------------- #
# Exercise 2 - London Banker Roulette.
# The high society from London is known from sometimes make this little game 
# where once they attend a reunion meal, they do not split the bill, all of 
# them put their credit card inside the bill box and the waiter is the fair 
# hand that chooses who pais that day. 
# Our objective is to recreate that little game. 
# We will introduce a string as an input, and our program will split the string
# into the list items. After, the program will split one random item from the 
# list.
# TIP: The function split() gives us a list from a given string. 
# "string.split(separator)"

# 🚨 Don't change the code below 👇
names_string = input("Give me everybody's names, separated by a coma: ")
names_list = names_string.split(", ")
# 🚨 Don't change the code above 👆
random_index = random.randint(0, len(names_list) - 1)
# Here we put -1 to avoid the Index error caused by the offset between the list 
# length and the list index count method that starts at 0.
print(names_list[random_index] + " is going to buy the meal today!")
# We also have the option of using random.choice(names_list) but with the 
# method from before we understand how index and lists work.

# ----------------------------------------------------------------------------- #
# Index Error & Nested Lists.

# Index error: Is a common error when we work with the index of the lists and 
# the length of things, usually it will be an "off by one" thing, but this
# error appears every time we move out from the memory allocated for the list.

# Nested Lists: It is common for programmers to use lists within lists.
# When so, we can say we are working with nested lists. In such cases is 
# important to keep track of the lengths and indexes we are working with to
# avoid errors.

item_list_1 = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
item_list_2 = ["Item 6", "Item 7", "Item 8", "Item 9"]
item_list_3 = ["Item 10", "Item 11", "Item 12"]

list_of_lists = [item_list_1, item_list_2, item_list_3]

print(list_of_lists[1])
print(list_of_lists[2][1])
print(list_of_lists)
print(len(list_of_lists))

# ----------------------------------------------------------------------------- #
# Exercise 3 - Treasure Map.
# Given a Map created using nested lists.
# You are going to write a program that will mark a spot with an X using the 
# coordinates and the lists index.

# 🚨 Don't change the code below 👇
row1 = ["⬜️", "️⬜️", "️⬜️"]
row2 = ["⬜️", "⬜️", "️⬜️"]
row3 = ["⬜️️", "⬜️️", "⬜️️"]
treasure_map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? [Column, Row]: ")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
column = int(position.split(",")[0])
row = int(position.split(",")[1])

treasure_map[row-1][column-1] = "X"
# Using the -1 to avoid the error between the coordinates and the list index.

# Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
# ----------------------------------------------------------------------------- #
