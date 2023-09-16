# ----------------------------------------------------------------------------- #
# Object Oriented Programming. (OOP)

# Procedural Programming. Is the use of our code in a sequential step-wise
# procedure to develop our applications.
# Is what we have been mostly doing until now.
# This kind of programming tends to get messy with larger files and apps.

# OOP: Sets different modules that are independent of each other module in
# our program allowing them to work by themselves but helping the bigger app
# that we are building work as intended.

# ----------------------------------------------------------------------------- #
# Classes and Objects

# Objects: Can have things (ATTRIBUTES) and can DO THINGS (METHODS). An Object
# is our way of combining some piece of data and some functionality, all
# together in the same thing.
# In OOP the general version of the objects is known as the CLASS and the
# individual objects generated from the blueprint are known as the OBJECTS.

# To create an object from a class, it looks like this in Python:
# object = ObjectBlueprint()
# We have the class constructor, which is written with every first letter of
# each word capitalized (Pascal Case), in our case 'ObjectBlueprint()'
# And the 'object' is the Object that gets created from the car blueprint.

import turtle
# Get a turtle class from the turtle Graphic library we have imported.
my_turtle = turtle.Turtle()
my_screen = turtle.Screen()

# To get an attribute from our object, we need to identify our object and
# then tell the attribute that we want to get from it. This is made by typing
# the name of our object, then a dot '.' and after that the attribute.
# my_object.attribute

# Print a couple of attributes from our object, in this case a screen.
print(f"Width: {my_screen.canvwidth}. Height: {my_screen.canvheight}.")

# Here, my_screen is our object and canvwidth & canvheight are its attributes.
# You can modify them in the same way we have been modifying other variables.
my_screen.canvheight = 500
my_screen.canvwidth = 500
print(f"Width: {my_screen.canvwidth}. Height: {my_screen.canvheight}.")

# Using the same dot notation that we learned with the attributes and our
# previous usage of functions. We are ready to tackle the methods from objects.
# we use the object followed by a dot, followed by our method/function that
# has its own parenthesis.
# my_object.method()

# Call a method from my_screen object.
# exitonclick() allows us to keep the screen up until we click on it.
# my_screen.exitonclick()

# More from Turtle:
# https://docs.python.org/3/library/turtle.html
# Other packages available for download:
# https://pypi.org/

# ----------------------------------------------------------------------------- #
# Exercise 0 - Play with the turtle, try changing its colour.
my_turtle.shape("turtle")
my_turtle.color("DeepPink", "cyan")

# ----------------------------------------------------------------------------- #
# Exercise 1 - Keep playing, try to make the turtle to move froward 100 spaces.
my_turtle.forward(100)

my_screen.exitonclick()
# ----------------------------------------------------------------------------- #
