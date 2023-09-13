# ----------------------------------------------------------------------------- #
# DISCLAIMER: THIS CODE CONTAINS MISTAKES/BUGS ON PURPOSE. 
# THE IDEA IS TO TACKLE EACH EXERCISE ONE BY ONE AND LEARN FROM THEM.
# ----------------------------------------------------------------------------- #
# Debugging:
# Debugging consist in finding the flaws or faults in the design, development 
# or the operations of our code. 
# We need, as developers, to be able to identify and remove this bugs. 

# Thing number one that you need to know: EVERYONE GETS BUGS. So we need to be 
# able to tackle them properly.

# ----------------------------------------------------------------------------- #
# First step: Describe the problem as clear as possible. 
# Try to untangle the problem and try to make sense of what is going on.

# Exercise 1  - Describe A Problem

def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it")


my_function()

# The function loops inside a for loop where 'i' takes the values from 1 to 20 
# and when 'i' reaches 20 (i == 20) it prints the 'You got it message'.
# Your assumption over 'i' reaching 20 is the ERROR here as the range function 
# in this case never sets the value of 'i' in 20 as it stops at 19.
# The range function never reaches the stop mark, in our case the second 
# parameter of the function.
# To fix this, change the stop point of our range function to 'range(1, 21)'.

# ----------------------------------------------------------------------------- #
# Exercise 2 - Reproduce the Bug

from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_images[dice_num])

# ----------------------------------------------------------------------------- #
# Trying to reproduce the bug itself means take the randomness of the problem 
# aside and test the different prints of the dice images.
# By doing this, we will to the conclusion that the bug in our case is when the
# random number introduced in the dice images list is equal to 6.
# We will also see that we never print the number 1 image.
# And applying a bit of logic here we should be able to find our conclusion.
# The problem here is that the index from the list starts at 0, not at 1, and 
# the maximum number that the list will allow us is the value 5, not 6, with 
# these values we cover every image.
# To fix our bug, we must replace the randint values to cover the list index 
# properly. randint(0, 5)

# ----------------------------------------------------------------------------- #
# Exercise 3 - Play Computer
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")

# The problem here is that introducing '1994' causes a bug in our program.
# In  this case, by playing computer, and checking the path that the value 
# '1994' takes in our code we find that the first condition is not valid as it
# just takes into account the values lower than 1994, making us jump to the 
# second one , where neither is valid as it just takes into account the values 
# that are grater than 1994. Taking us out of our program with no valid answer.
# To fix this, add an '=' to any 1994 creating a valid statement in our if 
# conditions.  if year > 1980 and year <= 1994:


# ----------------------------------------------------------------------------- #
# Exercise 4 - Fix the Errors

age = input("How old are you?")
if age > 18:
# print("You can drive at age {age}.")
    # If you uncomment the previous line the editor will show you an error, and
    # this should be as easy as just fixing what the editor is telling you.
    # In this case just indent the code to make it work properly.
    print("You can drive at age {age}.")    
# This line has been duplicated and fixed to help with the purpose of this
# content. Try to find, and debug this error too.

# But if you run the code you will notice another error. And the console will 
# yell about it too (Type Error). If we check what the error says is says that 
# can not compare a string with an int. And if we look closely to our code we
# can spot the bug pretty quickly, we are saving our input() directly to the 
# variable, and then using it as an integer, when the input() function returns 
# a string.
# To fix this, we just need to convert the input() to an int using the int() 
# function.  age = int(input("How old are you?"))

# After that a third bug appears, and it seems that is not printing the age, 
# nor is telling anything the console. In this case we just need to check 
# carefully our code. Seeing the {age} printed should give us a hint, it is not 
# taking the value of our variable. And if we look closely, we will see that we 
# are not using an f-string.
# To fix it convert the print parameter into an f-string parameter. 
# print(f"You can drive at age {age}.")

# ----------------------------------------------------------------------------- #
# Exercise 5 - Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
# print(f"PAGES: {pages}.") 
# print(f"WORDS: {word_per_page}.") 
print(f"TOTAL WORDS: {total_words}.")

# By using print we can check that the value for pages is working as intended, 
# but word per page is not being assigned. Once we know that, we can go to the 
# line of the words per page assignment and if we look closely we will find a 
# comparison instead of an assignation.
# To fix it, is as simply as removing one of the '=' from the operator.  
# word_per_page = int(input("Number of words per page: "))

# ----------------------------------------------------------------------------- #
# Debugger: 
# A debugger allows us to check step by step what is going on in our code, is 
# our stronger tool to find errors and to fix them. It allows us to check the 
# state of everything and also allows us to have breakpoints to pause the 
# program execution and check how is everything behaving. 
# Breakpoints also allows us to know if a point in our code is even reachable.


# #Use a Debugger
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
    b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])

# Visualizing the execution of our program we can reach the conclusion that is 
# giving us a one item list because the for loop is completed before adding 
# anything to the list.
# In this case is as simple as solving the indentation error and append the new
# item to the list in every loop from the for loop. 
# --> --> b_list.append(new_item).

# ----------------------------------------------------------------------------- #
# Other TIPS:
# - Take a break: Sometimes it´s better to take a few minutes to step back and 
#   come fresh to check why the program is misbehaving.
# - Ask other people: Other points of view can be really helpfully with these
#   situations, from developers and non developers.
# - Test your code: Do not wait for it to be completed, check different stages 
#   of the code to see if the steps that you are taking are on the correct path
#   towards your goals.
# ----------------------------------------------------------------------------- #
