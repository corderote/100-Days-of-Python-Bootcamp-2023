# -----------------------------------------------------------------------------
# Miles to Kilometers converter.
import tkinter
from tkinter import *
from tkinter import ttk

UNITS_DICTIONARY = {
    "Keys": ["Distances", "Weight"],
    "Distances": ["Kilometers", "Meters", "Centimeters", "Millimeters", "Miles"],
    "Weight": ["Kilograms", "Grams", "Milligram", "Pounds[lbs]"],
}

DISTANCES_DICTIONARY = {
    "Kilometers": float(1000),
    "Meters": float(1),
    "Centimeters": float(1/100),
    "Millimeters": float(1/1000),
    "Miles": float(1609),
}

WEIGHT_DICTIONARY = {
    "Kilograms": float(1000),
    "Grams": float(1),
    "Milligram": float(1/1000),
    "Pounds[lbs]": float(453.6),
}


def convert_type_selection(choice):
    type_selection = convert_value.get()
    unit_list_1.config(values=UNITS_DICTIONARY[type_selection])
    unit_list_2.config(values=UNITS_DICTIONARY[type_selection])
    unit_list_1.set(UNITS_DICTIONARY[type_selection][0])
    unit_list_2.set(UNITS_DICTIONARY[type_selection][1])
    unit_value_1.delete(0, END)
    unit_value_1.insert(0, "1")
    unit_value_2.config(text="1000")


def unit_type_selection(event):
    if convert_value.get() == "Distances":
        units_dictionary = DISTANCES_DICTIONARY
    elif convert_value.get() == "Weight":
        units_dictionary = WEIGHT_DICTIONARY
    else:
        return 1

    unit_1 = unit_list_1.get()
    unit_2 = unit_list_2.get()

    value_1 = float(unit_value_1.get())
    value_2 = (units_dictionary[unit_1]/units_dictionary[unit_2])*value_1
    unit_value_2.config(text=str(value_2))


def unit_1_entry_change(var, index, mode):
    try:
        float(unit_1_str.get())
    except ValueError:
        unit_1_str.set("")
        return 0

    if convert_value.get() == "Distances":
        units_dictionary = DISTANCES_DICTIONARY
    elif convert_value.get() == "Weight":
        units_dictionary = WEIGHT_DICTIONARY
    else:
        return 1

    unit_1 = unit_list_1.get()
    unit_2 = unit_list_2.get()

    value_1 = float(unit_value_1.get())
    value_2 = (units_dictionary[unit_1]/units_dictionary[unit_2])*value_1
    unit_value_2.config(text=str(value_2))


# Window Definition.
window = Tk()
window.title("Unit Converter")
# Limit both min and max size of the window, so we just work with the size we want.
window.minsize(width=385, height=100)
window.maxsize(width=385, height=100)

# Option Menu for Convert Types.
convert_value = StringVar()
convert_value.set("Convert Type")
units_listbox = OptionMenu(None, convert_value, *(UNITS_DICTIONARY["Keys"]), command=convert_type_selection)
units_listbox.config(width=57)
units_listbox.place(x=0, y=0)

# Entry Widgets for the units. #1
unit_1_str = StringVar()
unit_1_str.trace_add("write", unit_1_entry_change)
unit_value_1 = Entry(textvariable=unit_1_str)
unit_value_1.config(width=25)
unit_value_1.grid(column=0, row=0, padx=10, pady=(30, 0))

# Label for between unit Widgets.
equal_label = Label(text="=", font=("Arial", 24, "bold"))
equal_label.grid(column=1, row=0, pady=(30, 0))

# Entry Widgets for the units. #2
unit_value_2 = Label()
unit_value_2.config(width=25)
unit_value_2.grid(column=2, row=0, padx=10, pady=(30, 0))

# Combobox Widget for Units Selections.
unit_choices_1 = [""]
unit_list_1 = ttk.Combobox()
unit_list_1.config(state="readonly", values=unit_choices_1)
unit_list_1.config(width=20)
unit_list_1.grid(column=0, row=1, pady=(0, 10))
unit_list_1.bind("<<ComboboxSelected>>", unit_type_selection)

unit_choices_2 = [""]
unit_list_2 = ttk.Combobox()
unit_list_2.config(state="readonly", values=unit_choices_2)
unit_list_2.config(width=20)
unit_list_2.grid(column=2, row=1, pady=(0, 10))
unit_list_2.bind("<<ComboboxSelected>>", unit_type_selection)

window.mainloop()
# -----------------------------------------------------------------------------
