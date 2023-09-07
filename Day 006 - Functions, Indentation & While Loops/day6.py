import random
# ----------------------------------------------------------------------------- #
# Functions
# Blocks of code that allows it to perform a piece of functionality.
# We have already used a lot of functions, e.g. len(), print(), range(), ...
# They identify themselves with a name followed by a pair of parenthesis. 


# ----------------------------------------------------------------------------- #
# To make or own functions we need to create them before using them. 
# To create a function we use the 'def' keyword that symbolizes the definition.
# After the 'def' we add the name we want to assign to our function, setting
# how we are going to be calling it later in our code.
# We finish the function declaration adding a pair of parenthesis and a colon.
# Once the function is defined, the code we add below belongs to our function,
# we just need to make sure that the code is indented appropriately.
def my_function():
    print("This")
    print("Is")
    print("My")
    print("Function")


# Defining a function does not call it. To trigger them we need to use them
# the same way we have been using the other ones.
my_function()


# ----------------------------------------------------------------------------- #
# Indentation
# Indentation allows us to define different blocks of code. This divides our 
# code in different areas, such areas tend to be independent and have
# different behaviours.
# It seems similar to the folder system that we can find on the file explorer. 
# Generating a sort of dependency on the 'folder' our code sits in, and the 
# other levels of indentation our code is affected by. 

def my_second_function():
    print("This code belongs to my_second_function.")
    print("This code is indented and belongs to my_second_function.")


print("This code doesnt belong to my_second_function. Check indentation.")
print("This code is independent from my_second_function.")

# Indentation also affects 'if' statements and the loops that we create.
for n in range(3):
    print("This code belongs to the for loop.")    
    print("This code IS indented.")
    if n == 1:
        print("This code belongs to the if statement inside the for loop.")
        print("This code IS indented multiple times.") 
print("This code IS NOT indented as it does not belong to the for statement.")

# ----------------------------------------------------------------------------- #
# While Loop:
# In contrast to for loops, that are set to repeat themselves a certain number
# of times. 
# While loops are set to keep happening as long as a condition is met.

condition = True
condition_counter = random.randint(1, 10)
print(f"While Start. Counter = {condition_counter}.")
while condition:
    if condition_counter <= 0:
        condition = False    
    print(f"Iteration: {condition_counter}")
    print(f"Condition: {condition}")
    condition_counter -= 1

print("While End.")
# CAUTION: while loops can set an infinite loop causing our program to repeat 
# itself forever. Make sure to have a reachable end condition.

# PRACTISE: https://reeborg.ca/index_en.html
# Exercises: 
# - Loop practise.
# - Jumps until goal.
# - Jumps with different jumps placed.
# - Jumps with different jump height.
# - Escape a random maze.
# ----------------------------------------------------------------------------- #
# TODO: Make something not REEBORG dependant to practise this day/content.
# ----------------------------------------------------------------------------- #
