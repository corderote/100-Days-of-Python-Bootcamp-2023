# ----------------------------------------------------------------------------- #
# Create a Class in Python
# This is achieved by using the 'class' keyword. And to follow it we use the
# name that we want to associate our class with. We finish the declaration by
# adding a colon ':'.
# All the content that belongs to the class has to be indented.
# Classes must be PascalCase named.

# NAMING TYPES:
# PascalCase : Every word goes together and the first letter of each word has
#              to be Uppercase, the rest of the word lowercase
# camelCase: Every word goes together, the first word goes full lowercase and
#            after that one, the first letter of the rest of words have to go
#            Uppercase.
# snake_case: Every word has to be lowercase, and words go separated with an
#             underscore '_'.

class PassiveClass:
    pass


# The 'pass' keyword allows us to create functions or classes that have no
# content without calling a warning on our editor.
# This can come handy when we are just building the skeleton for our programs
# or applications.

# To create an object from our class we just need to call our class name
# followed by braces '()'
passive_object = PassiveClass()


# Constructor: A part of our blueprint that allows us to specify what should
# happen when our object is being constructed or initialized.
# When we initialize our objects we set their attributes to their starting
# values.
# In Python to do this we use the '__init__' function. To add this to our class
# we declare this '__init__' function/method inside our Class scope.
# The '__init__' function gets called every time a Class is created.
# We can also add parameters to our __init__ function and pass that parameters
# when we create our object to initialize the values of the attributes inside
# our class.
# If we wanted to add a method to our Class, we simply add a function inside
# the scope of our Class, these methods add functionality to what our class
# can do.
# To make use of the Attributes or the Methods we simply take our object and
# add the dot notation to it, to call the method we need to add the braces
# and the parameters if needed.
class User:
    def __init__(self):
        # You don't need to always add the parameter if you want to add an
        # attribute. You can simply add an attribute by default the same way
        # as with functions. or just add its initialization here.
        self.id = 0
        self.username = "Default Username"
        print(f"User Class > New user created. {self.username}. ID: {self.id}")
        self.followers = 0
        self.following = 0

    def print_user_data(self):
        print(f"User ID: [{self.id}] Name > {self.username}. Followers "
              f"{self.followers}")

    def follow(self, user):
        print(f"User {self.username} started following {user.username}.")
        self.following += 1
        user.followers += 1


class UserWithParameters:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.username = user_name
        print(f"UserWithParameters Class > New user created. {self.username}. "
              f"ID: {self.id}")
        self.followers = 0
        self.following = 0

    def print_user_data(self):
        print(f"User ID: [{self.id}] Name > {self.username}. Followers "
              f"{self.followers}")

    def follow(self, user):
        print(f"User {self.username} started following {user.username}.")
        self.following += 1
        user.followers += 1


user_1 = User()
user_2 = UserWithParameters(2, "Jack")
print(f"{user_2.username} has {user_2.followers} followers.")
user_1.follow(user_2)
user_1.print_user_data()
user_2.print_user_data()
# ----------------------------------------------------------------------------- #
