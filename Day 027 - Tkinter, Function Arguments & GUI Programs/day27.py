# -----------------------------------------------------------------------------
# Tkinter
# More info about tkinter > https://docs.python.org/3/library/tkinter.html
import tkinter

# Creating a Tkinter Window & Modifying some of its attributes.
window = tkinter.Tk()
window.title("TKINTER Window")
window.minsize(width=500, height=300)

# Creating a label to show inside our window. Just creating it will not put it
# inside the window.
my_label = tkinter.Label(text="This is a Label", font=("Arial", 24, "bold"))
# '.pack()' will take our label and put it inside our screen in the center of
# it. We have plenty of attributes that this function can take to alter the way
# our components appear inside our window. CHECK THE DOCUMENTATION.
my_label.pack()


# -----------------------------------------------------------------------------
# Advanced Python Arguments to specify a wide array of inputs.


# Function with arguments. You need to provide the inputs when calling the
# function.
def my_function_1(a, b, c):
    result = a+b+c
    return result


# Function with Default Arguments Value. You provide the inputs just when you
# want to modify them.
def my_function_2(a=2, b=2, c=3):
    result = a+b+c
    return result


# -----------------------------------------------------------------------------
# *args > Many Positional Arguments
# Allows us to add unlimited positional arguments.
def add(n1, n2):
    result = n1 + n2
    return result


def m_add(*sums):
    result = 0
    for n in sums:
        result += n
    return result


# print(add(15, 56))
# print(m_add(13, 42, 23, 84, 35, 96, 77))

# -----------------------------------------------------------------------------
# *kwargs > Many Positional Keyword Arguments
# Allows us to add unlimited keyword arguments.
# *kwargs works as a dictionary, where the names are the keys and the
# assignations are the values.
def calculate(number=0, **kwargs):
    result = number
    result += kwargs["add"]
    result *= kwargs["multiply"]


calculate(13, add=7, multiply=3)


# -----------------------------------------------------------------------------
# Classes with **kwargs
class MyClass:
    # We have to use the .get() function here to make sure that if the key is
    # not introduced by the user our class can still work.
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.version = kw.get("version")


my_object = MyClass(make="Item", version="1.0")

# -----------------------------------------------------------------------------
# Tkinter Buttons settings:
# Tkinter gives us the options to modify items on the item creation moment by
# assigning the kwargs or after the creation using the dict like method with
# our item.

my_button_1 = tkinter.Button(fg="red", bg="blue", text="Button 1")
my_button_2 = tkinter.Button()
my_button_2["fg"] = "green"
my_button_2["bg"] = "grey"

# It also has a .config() method that we can call after the item creation.
my_button_2.config(text="Button 2")


def button_1_clicked():
    my_label.config(text="Button 1 got clicked.")


def button_2_clicked():
    my_label.config(text=user_input.get())


# To use a method when our button is clicked, tkinter has the 'command' property,
# this property adds the same way as the other ones by assigning the name of the ç
# method that we want to call.
my_button_1.config(command=button_1_clicked)
my_button_2.config(command=button_2_clicked)

my_button_1.pack()
my_button_2.pack()

# -----------------------------------------------------------------------------
# Tkinter Entry Class
user_input = tkinter.Entry()
user_input.config(width=30)
user_input.pack()


# -----------------------------------------------------------------------------
# Other Tkinter Widgets

# Text
text = tkinter.Text(height=5, width=30)
# Puts cursor in textbox.
text.focus()
# Adds some text to begin with.
text.insert(tkinter.END, "Example of multi-line text entry.")
# Gets current value in textbox at line 1, character 0
print(text.get("1.0", tkinter.END))
text.pack()


# Spinbox
def spinbox_used():
    # gets the current value in spinbox.
    print(spinbox.get())


spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
# Called with current scale value.
def scale_used(value):
    print(value)


scale = tkinter.Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())


# variable to hold on to checked state, 0 is off, 1 is on.
checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked.
radio_state = tkinter.IntVar()
radiobutton_1 = tkinter.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton_2 = tkinter.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton_1.pack()
radiobutton_2.pack()


# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = tkinter.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

# -----------------------------------------------------------------------------
# Layout Managers from Tkinter.

# Pack() -> Packs each of the Widgets next to each other in a vaguely logical
# format. Default packing from the top to the bottom. You can modify this by
# using the 'side' parameter. It´s hard to use this to specify a position in our
# window.

# Place(x=pos_x, y=pos_y) -> Its all about precise positioning where the (0,0)
# is in the top left corner. Maybe too specific when you have a lot of widgets.

# Grid(column=col_num, row=row_num) -> Divides your window as if it was a grid.
# This system is relative to other Widgets, so you start defining your top left
# item and then work your widget positioning from there.

# You can´t mix grid() and pack() systems.
# You can also modify paddings to the different Widgets or the window to config
# the window.
window.mainloop()
# -----------------------------------------------------------------------------
