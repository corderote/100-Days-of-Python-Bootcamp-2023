import sys
import os
import blind_aution_art
# ----------------------------------------------------------------------------- #
# Dictionaries & Nesting.

# Dictionaries allow us to group together and tag pieces of information. 
# They give us, in a similar way as a traditional dictionary, a word that we 
# are going call KEY and a description, which  is going to be our VALUE.
# These VALUES do not need to have a type, they can be whatever kind of
# datatype that we want to introduce.
# To write a dictionary, we have, in the form of a table, on the left the KEY, 
# which correspond to the word of a traditional dictionary. And on the right,
# an associated VALUE, that would be the equivalent of the actual definition.

# To write this in python, the syntax would be as follows: 
# A set of curly braces '{}' that delimits the content of our dictionary.
# Whatever we put inside will be the content of our dictionary. 
# To define the content of the dictionary, the KEY goes first on the left side 
# followed by a colon ':' and then we write the VALUE.

key = "Bug"
value = "Error in the program that prevents it to work as intended."

my_dictionary = {key: value}

# If you want to add multiple things to your dictionary, you just need to add 
# a coma ',' at the end of the value and keep writing this key, colon, value 
# structure pairs until you reach the end of your dictionary.

other_dictionary = {
    "key_1": "value 1",
    "key_2": "value 2",
    "key_3": "value 3",
    "key_4": "value 4",
    "key_5": "value 5",
}

# If you want to retrieve a piece of information from a dictionary you have to 
# do in a similar way as with the lists, but in this case, inside the braces 
# you have to insert the key that you want to take the value from. 
# CAREFUL with the typos here. They will create a KEY ERROR MESSAGE.

print(other_dictionary["key_1"])

# Adding new items to the dictionary.
other_dictionary["key_something"] = "value something"
other_dictionary[123] = "value 123" 
# You can work with key or values that are not strictly a string.

print(other_dictionary)

# Creating an empty dictionary or wiping an existing one.
empty_dictionary = {}

# ----------------------------------------------------------------------------- #
# Edit an Item in a dictionary: 
# It works in a similar way than with lists, in the braces '[]' you add the key 
# that you wnt to assign, and then equal all that to the value.
# If it does found an item with the same key already in the dictionary it will
# modify its content, you can not have two items with the same key.
other_dictionary["key_something"] = "New value for something."

# What do you think this will do? 
for thing in other_dictionary:
    print(thing)
# ANSWER: It will print just the key values from the dictionary.

# If ou want to print the values, the proper syntax is as follows:
for key in other_dictionary:
    print(other_dictionary[key])

# ----------------------------------------------------------------------------- #
# Exercise 1 - Grading Program
# Having access to a database of student_scores in the format of a dictionary. 
# The keys in student_scores are the names of the students and the values are 
# their exam scores. 
# Write a program that converts their scores to grades. 

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
# TODO-2: Write your code below to add the grades to student_grades.👇
for student_name in student_scores:
    if student_scores[student_name] > 90:
        student_grades[student_name] = "Outstanding"    
    elif student_scores[student_name] > 80:
        student_grades[student_name] = "Exceeds Expectations"    
    elif student_scores[student_name] > 70:
        student_grades[student_name] = "Acceptable"    
    else:
        student_grades[student_name] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)

# ----------------------------------------------------------------------------- #
# Nesting.

# List & dictionaries are this collection types that we can imagine as folders, 
# where lot of things can be stored inside of them.
# Then nesting is just a matter of putting one inside the other. 

# Notice that on the example we can find a list and a dictionary nested inside 
# another dictionary. 
# The structure becomes more complex, but it gives us a lot of flexibility.
nested_dictionary = {
    "key_1": "value",
    "key_2": [1, 2, 3],
    "key_3": {"subkey_1": "sub value"}
}

capitals_dictionary = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Milan",
    "Spain": "Madrid",
}


# Nesting here allows us to keep track of multiple cities that we have visited 
# in each country.

# Nesting lists inside dictionaries.
travel_log_dictionary = {
    "France": ["Paris", "Lille"],
    "Germany": ["Berlin", "Munich", "Frankfurt"],
    "Italy": ["Milan", "Florence"],
    "Spain": ["Madrid", "Barcelona"],
}

# Nesting lists inside lists.
alphabet_vowels_list = [['a', 'e', 'i', 'o', 'u'], ['A', 'E', 'I', 'O', 'U']]

# Nesting dictionaries inside dictionaries.
travel_log_dictionary_2 = {
    "France": {
        "cities_visited": ["Paris", "Lille"],
        "total_visits": 7
    },
    "Germany": {
        "cities_visited": ["Berlin", "Munich", "Frankfurt"],
        "total_visits": 13
    },
}

# Nesting dictionaries inside lists.
travel_log_list = [
    {
        "country_name": "Italy",
        "cities_visited": ["Milan", "Florence"],
        "total_visits": 15
    },
    {
        "country_name": "Spain",
        "cities_visited": ["Madrid", "Barcelona"],
        "total_visits":7
    }
]

# ----------------------------------------------------------------------------- #
# Exercise 2 - Dictionary in List
# You are going to write a program that adds new countries to a travel_log.

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]
# 🚨 Do NOT change the code above


# TODO: Create a function to add countries to the travel_log.
def add_new_country(c_name, c_times_visited, c_cities_visited):
    new_country_dictionary = {
        "country": c_name,
        "visits": c_times_visited,
        "cities": c_cities_visited
    }
    travel_log.append(new_country_dictionary)


# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log) 

# ----------------------------------------------------------------------------- #
# Exercise 3 - Blind Auction


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


# Secret auction program.
print("Welcome to the secret auction program.")
auction_bids = {}
more_bids = ""
while more_bids != "no":
    new_name = ""
    more_bids = ""
    print(blind_aution_art.logo)
    # Ask for the bidder name.
    # If bidder already exist, tell the user and ask again.
    bidder_already_exists = True
    while bidder_already_exists:
        bidder_already_exists = False
        new_name = input("What is your name? ")
        for bidder_name in auction_bids:
            if bidder_name == new_name:
                bidder_already_exists = True
                print(f"Name '{new_name}' already used in the auction.")
                print("Please use other name.")
    # Ask for the price to bid.
    new_bid = int(input("What is your bid? "))
    # Add the name and bid to a list or a dictionary.
    auction_bids[new_name] = new_bid
    # Asks if there is any other bidder until you answer yes or no. 
    while more_bids != "no" and more_bids != "yes":
        more_bids = input("Are there any other bidders? Type 'yes' or 'no'. ")
        more_bids = more_bids.lower() 
    clear_screen()

# Check for the highest bid inside the auction bids. 
winner_name = "ERROR: No bidders found."
winner_bid = 0
for bidder_name in auction_bids:
    if auction_bids[bidder_name] > winner_bid:
        winner_name = bidder_name
        winner_bid = auction_bids[bidder_name]

# Print the winner of the auction.
print(f"The winner is {winner_name} with a bid of {winner_bid}.")
# ----------------------------------------------------------------------------- #
