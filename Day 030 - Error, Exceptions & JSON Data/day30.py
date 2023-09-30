import pandas
# ----------------------------------------------------------------------------- #
# ERROR TYPES:

# FileNotFoundError:
# with open("a_file.txt") as file:
#    file.read()
# If file does not exist in our folder, this will generate a FileNotFoundError.

# KeyError:
# a_dict = {"key": "value"}
# value = a_dict["non_existent_key"]

# Index Error:
# a_list = ["value_1", "value_2", "value_3"]
# an_item = a_list[5]

# Type Error:
# text = "abcd"
# print(text + 5)

# ----------------------------------------------------------------------------- #
# CATCHING EXCEPTIONS:
# When something goes wrong, and it will, we can catch that Error and act in a
# more appropriate way.

# syntax keywords for catching exceptions:
#   'try': block of code that might cause an exception.
#   'except': do this if there was an exception.
#   'else': do this if there was no exception.
#   'finally': do this no matter what happens.

try:
    file = open("a_file.txt")
    a_dict = {"key": "value"}
    value = a_dict["non_existent_key"]
except FileNotFoundError as error_message:
    # If file does not exist create it.
    file = open("a_file.txt", "w")
except KeyError as error_message:
    print(error_message)
else:
    content = file.read()
    print("File Found.\n Content: " + content)
finally:
    file.close()
    print("File was closed.")

# ----------------------------------------------------------------------------- #
# RAISING EXCEPTIONS:
# 'raise' allows us to create our own error exceptions.

height = float(input("Input Height (m):"))
weight = float(input("Input Weight (Kg):"))

if height > 3 or height < 0.5:
    raise ValueError("Invalid Height Value.")

if weight > 500 or weight < 0.0:
    raise ValueError("Invalid Weight Value.")

bmi = weight/(height**2)
print("BMI Value: " + str(bmi))

# ----------------------------------------------------------------------------- #
# Exercise 1 - IndexError Handling:

fruits = ["Apple", "Pear", "Orange"]


# TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")


make_pie(4)

# ----------------------------------------------------------------------------- #
# Exercise 2 - KeyError Handling:

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]
# TODO: Catch the exception and make sure the code runs without crashing.

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass

print(total_likes)

# ----------------------------------------------------------------------------- #
# Exercise 3 - Handling errors in our NATO Alphabet Project: (Day 26)


def generate_phonetic():
    user_input = input("Enter a word: ")
    input_to_list = [letter.upper() for letter in user_input]
    try:
        nato_input_list = [nato_dict[input_letter] for input_letter in input_to_list]
    except KeyError:
        print("Sorry, only letters from the alphabet are allowed please.")
        generate_phonetic()
    else:
        print(f"NATO TRANSCRYPT: {nato_input_list}")
    return input_to_list


csv_path = "../Day 026 - List & Dictionaries Comprehensions/nato_phonetic_alphabet.csv"
nato_data_frame = pandas.read_csv(csv_path)

nato_dict = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}

generate_phonetic()

# ----------------------------------------------------------------------------- #
# JSON
# JSON stands for JavaScript Object Notation, simple notation adopted for a lot
# of different fields, including python. Great format to transfer data.
# It´s kind of similar to lists and dictionaries, like a structure mixing both.

# To work with json in python: import the json library.
#   json.dump() to write inside the json file.
#   json.load() to take the JSON data as a dictionary to a variable.
#   json.update() to update the dictionary that we have loaded.

# ----------------------------------------------------------------------------- #
