# ----------------------------------------------------------------------------- #
# Scope.
# Scope in programming refers to the part of our code where our variable and 
# its value binding is valid.
# If a variable is out of scope calling for that entity will not reference 
# anything or will be considered another entity.

# Try to guess what´s going on the next piece of code. What will be printed?
my_variable = 1


def increase_variable():
    my_variable = 2
    print(f"My variable inside function value: {my_variable}")  
    # This will print 2.


increase_variable()
print(f"My variable outside function value: {my_variable}")     
# This will print 1. 
# Maybe you guessed 2, but everything here has to do with the scope.

# ----------------------------------------------------------------------------- #
# Global Scope vs Local Scope
# The most basic modular scope differentiates the Global scope and the Local
# Scope. Where the global scope can affect anywhere and a local scope that just
# affects within a defined function.


# ----------------------------------------------------------------------------- #
# Local Scope: Is the scope that just exists within functions. 
#########################################
def my_function():                      # 
    local_scope_variable = 0            # 
    print(f"{local_scope_variable}")    #
#########################################
# This Block defines the local scope of our function.  nd the variables that 
# we define inside of it will just exist within the function space. 
# 'local_scope_variable' here is a LOCAL variable inside the function scope.


my_function()
# print(local_scope_variable) 
# If we try to print the local_scope_variable outside the function, it will 
# result in a NameError as we do not have that variable defined inside the 
# program scope, that variable just exists within the limits of the function. 

# ----------------------------------------------------------------------------- #
# Global Scope: 
# The scope that just exists in all our document. The variables that we define 
# at the top level of our file are considered global variables. 
# These variables just need to not be inside other scopes, but can be accessed
# by them, no matter how deep they are nested.
global_scope_variable = 10


# global_scope_variable here is a GLOBAL variable in our document scope.
def my_other_function():
    print(global_scope_variable)


my_other_function()
print(global_scope_variable)

# The scope affects everything, variables, functions... every piece of code 
# belongs to a scope. And things have to be called inside that scope to work
# properly.
# In our first case, the variable was defined twice, once in global and the 
# second in local space. And when we wanted to print it inside the local scope, 
# it was this scope which override the namespace definition and took its value
# and printed it, without taking into account the global one.
# That´s why when we printed the second time in the global scope, it printed
# the global variable value, without modifications. 
# Because the computer worked as if we had two different variables with the 
# same name and different scopes. 

# ----------------------------------------------------------------------------- #
# Block Scopes in Python:
# Block scopes refer to the block of code and the scope that it occurs every 
# time we have an if statement or something similar. 
# In Python, this kind of scopes do not exist. 
variable = 10
item_list = [1, 2, 3]

if variable > 5:
    new_item = item_list[2]

print(new_item)

# Here, new_item does not cause any trouble, as Python treats everything as 
# global scope territory.

# Modify a global scope variable in a local scope:
# We can implicitly say that we have a global variable that we want to modify 
# in our local scope by typing the keyword 'global' and adding the global 
# variable name that we want to modify.
# Otherwise, we can not alter thing from one scope in other scopes. And this is
# made difficult in programming because usually you will not want to do that
# kind of modification between scopes.
my_variable = 10


def increase_variable():
    global my_variable
    my_variable += 1
    print(f"My variable inside function value: {my_variable}")  


increase_variable()
print(f"My variable outside function value: {my_variable}") 


# Other option is to use the return option from the function.
def increase_my_variable():
    return my_variable + 1


print(f"My variable value: {my_variable}")
# ----------------------------------------------------------------------------- #
# Global Constants
# Constants are variables that you define once, and you do not plan on modifying
# them ever again. 
# In Python, this type of variables are named all uppercase.

PI = 3.14159
GOOGLE_URL = "https://www.google.com"
TWITTER_HANDLE = "@username"
# ----------------------------------------------------------------------------- #
