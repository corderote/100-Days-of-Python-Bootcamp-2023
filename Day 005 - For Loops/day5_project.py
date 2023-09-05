# ----------------------------------------------------------------------------- #
# Password Generator.
import random

# We could also import the string module and use the alphabet variable or list  
# (string.ascii_letters) to get this variable as a list.
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '?', '#', '$', '%', '&', '/', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator: ")
num_letters = int(input("How many letters would you like in your password?\n"))
num_numbers = int(input("How many numbers would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like in your password?\n"))

random_letters = []
random_numbers = []
random_symbols = []

for n in range(num_letters):
    random_letters.append(letters[random.randint(0, len(letters) - 1)])
    # random_letters.append(random.choice(letters)) could also work. 
    # The random.choice() can also be used to extract letters/numbers/symbols.

for n in range(num_numbers):
    random_numbers.append(numbers[random.randint(0, len(numbers) - 1)])

for n in range(num_symbols):
    random_symbols.append(symbols[random.randint(0, len(symbols) - 1)])

ordered_password_list = random_letters + random_numbers + random_symbols
total_password_characters = len(ordered_password_list)
password_list = []
for n in range(0, total_password_characters):
    op_index = random.randint(0, len(ordered_password_list)-1)
    op_character = ordered_password_list.pop(op_index)
    password_list.append(op_character)
# You can also use the random.shuffle(ordered_password_list) 
# This function randomizes the order of the items from an 'organized' list.

password = ""
for password_character in password_list:
    password += password_character

# Another option could be: password = "".join(password_list) 
# This is used to concatenate all the characters from the list to a string.
# In such case the string "" represents an empty one, But we could make use 
# of another string if we needed to.

print(f"Your password is : {password}")
# ----------------------------------------------------------------------------- #
