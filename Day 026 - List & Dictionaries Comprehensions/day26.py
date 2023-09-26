# -----------------------------------------------------------------------------
# List Comprehension
# It's a case where you create a list from another lists.
# Previously we have used for loops to do that, using append() at each stage of
# the for loop to add things to our new list.
# LIST COMPREHENSION METHOD > new_list = [new_item for item in list]
# We open a new set of squared brackets, denoting that we are creating a new
# list, and then, we have this 'new_item for item in list' pattern
import random
import pandas

numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_n_list = []
for n in numbers_list:
    number = n + 1
    new_n_list.append(number)

new_number_list = [(number + 1) for number in numbers_list]

print(numbers_list)
print(new_n_list)
print(new_number_list)

# You can also work with strings or other python sequences.
# Python Sequences: list, range, string, tuple,
name = "My name"
name_list = [letter for letter in name]
print(name_list)

range_list = [(number * 2) for number in range(0, 10)]
print(range_list)

# Conditional List Comprehension:
# METHOD > new_list = [new_item for item in list if test]

name_list = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Fred", "Gus"]
short_names_list = [name for name in name_list if (len(name) < 5)]
long_names_list = [name.upper() for name in name_list if (len(name) > 4)]
print(short_names_list)
print(long_names_list)

# -----------------------------------------------------------------------------
# Exercise 1 - Squaring Numbers.
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)

# -----------------------------------------------------------------------------
# Exercise 2 - Filter Even Numbers.
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
even_numbers = [num for num in numbers if (num % 2 == 0)]
print(even_numbers)

# -----------------------------------------------------------------------------
# Exercise 3 - Data overlap. Take a look at data_1.txt and data_2.txt, and you
# must create a list that contains just the numbers that are in both data
# files.
with open("data_1.txt") as file_1:
    # Using '.readlines()' here is ok as long as you take into account that the
    # '\n' can cause you troubles reading the last entity from your file.
    file_1_data = file_1.read().splitlines()

with open("data_2.txt") as file_2:
    file_2_data = file_2.read().splitlines()

data_overlap_list = [int(number) for number in file_1_data if (number in file_2_data)]
print(data_overlap_list)

print(f"FILE 1: {file_1_data}\nFILE 2: {file_2_data}\nOverlap: {data_overlap_list}")


# Read the txt file with read_csv from pandas and assigning a header and names.
file_1_data = pandas.read_csv("data_1.txt", header=None, names=["numbers"])
file_2_data = pandas.read_csv("data_2.txt", header=None, names=["numbers"])
file_1_data_list = file_1_data.numbers.to_list()
file_2_data_list = file_2_data.numbers.to_list()
overlap_list = [int(number) for number in file_1_data_list if (number in file_2_data_list)]
print(f"FILE 1: {file_1_data_list}\nFILE 2: {file_2_data_list}\nOverlap: {overlap_list}")

# -----------------------------------------------------------------------------
# Dictionary Comprehension
# Allows us to create a new dictionary from the values in a list or a dictionary.
# METHOD_1 > new_dict = {new_key:new_value for item in list}
# METHOD_1 > new_dict = {new_key:new_value for (key, value) in dict.items()}
# You can also add the 'if test' part to both of the previous methods.

students_list = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Fred", "Gus"]
students_scores = {student: random.randint(0, 100) for student in students_list}
passed_students = {student: score for (student, score) in students_scores.items() if score > 59}
print(passed_students)

# -----------------------------------------------------------------------------
# Exercise 4 - Take each word of a sentence and calculate the number of letters
# in each word.
sentence = "Little Red Riding Hood decided to wear orange today."
words_list = sentence.split(" ")
words_dictionary = {word: len(word) for word in words_list}
print(words_dictionary)

# -----------------------------------------------------------------------------
# Exercise 5 - Take a Celsius degrees dictionary for a weather weekly report
# and convert its degrees into Fahrenheit.
weather_celsius_dict = {
    "Monday": 12,
    "Tuesday": 16,
    "Wednesday": 14,
    "Thursday": 18,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24
}
weather_fahrenheit_dict = {day: int((c_degrees*9/5) + 32) for (day, c_degrees) in weather_celsius_dict.items()}
print(weather_fahrenheit_dict)

# -----------------------------------------------------------------------------
# Iterating with Pandas Dataframes.
#
students_dict = {
    "students": ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Fred", "Gus"],
    "score": [56, 75, 96, 45, 66, 22, 92]
}
# Looping through dictionaries:
# for (key, value) in students_dict.items():
#     print(key)
#     print(value)

students_data_frame = pandas.DataFrame(students_dict)

# Looping through a Data Frame:
for (key, value) in students_data_frame.items():
    print(key)
    print(value)
# Looping through rows of a Data Frame:
for (index, row) in students_data_frame.iterrows():
    print(index)
    print(row)
    print(row.student)
    print(row.score)

# -----------------------------------------------------------------------------
# NATO Alphabet Project. Transcrypt a message that the user inputs as the NATO ç
# alphabet values to be able to spell the message clearly.

nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}

user_input = input("Enter a word: ")
user_input_list = [letter.upper() for letter in user_input]

nato_input_list = [nato_dict[input_letter] for input_letter in user_input_list]
print(f"NATO TRANSCRYPT: {nato_input_list}")
