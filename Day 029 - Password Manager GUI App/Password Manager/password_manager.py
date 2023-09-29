# ----------------------------------------------------------------------------- #
from tkinter import *
from tkinter import messagebox
import os
import pandas
import random
import pyperclip

default_email = "polito@things.com"
default_filepath = "./pm_data.csv"


# ---------------------------- FILE MANAGEMENT -------------------------------- #
def check_filepath_exists(filepath):
    return os.path.isfile(filepath)


def check_filepath_empty(filepath):
    if os.path.getsize(filepath) > 0:
        return False
    else:
        return True


def create_file(filepath):
    file = open(filepath, mode="w")
    file.close()


def save_to_clipboard():
    pyperclip.copy(password_input.get())


# ---------------------------- PASSWORD GENERATOR ----------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '?', '#', '$', '%', '&', '/', '(', ')', '*', '+']

    num_letters = random.randint(5, 10)
    num_numbers = random.randint(5, 10)
    num_symbols = random.randint(5, 10)

    letter_list = [random.choice(letters) for _ in range(num_letters)]
    number_list = [random.choice(numbers) for _ in range(num_numbers)]
    symbol_list = [random.choice(symbols) for _ in range(num_symbols)]

    password_list = letter_list + number_list + symbol_list
    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.delete(0, END)
    password_input.insert(0, password)


# ---------------------------- PASSWORD SAVING -------------------------------- #
def save_password():
    user_website = website_input.get()
    user_email = email_input.get()
    user_password = password_input.get()

    if (user_website == "") or (user_email == "") or (user_password == ""):
        messagebox.showinfo(title="Invalid Values",
                            message="Please do not leave any field empty.")
    else:
        is_ok = messagebox.askokcancel(title="Confirmation Window",
                                       message="These are the details entered:\n" +
                                               f"Site: {user_website}\n" +
                                               f"Email: {user_email}\n" +
                                               f"Password: {user_password}\n\n" +
                                               "Is it OK to save?")
        if is_ok:
            save_data_to_file(user_website, user_email, user_password)


def save_data_to_file(u_web, u_email, u_pass):
    if check_filepath_exists(default_filepath) is False:
        create_file(default_filepath)

    new_data = pandas.DataFrame({"Site": [u_web],
                                 "Email": [u_email],
                                 "Password": [u_pass]})

    if check_filepath_empty(default_filepath) is False:
        file_data = pandas.read_csv(default_filepath)
        dataframes = [file_data, new_data]
        final_data = pandas.concat(dataframes)
    else:
        final_data = new_data

    final_data.to_csv(default_filepath, index=False)
    website_input.delete(0, END)
    password_input.delete(0, END)
    website_input.focus()


# ---------------------------- UI SETUP --------------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
window.resizable(False, False)

logo_canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="./Password Manager/pm_logo.png")
logo_canvas.create_image(100, 100, image=logo_img)
logo_canvas.grid(column=0, row=0, columnspan=5)

website_title = Label(text="Website:")
website_title.grid(column=0, row=1, padx=5, pady=5)
website_input = Entry(width=60)
website_input.grid(column=1, row=1, columnspan=3, padx=5, pady=5)
website_input.focus()

email_title = Label(text="Email:")
email_title.grid(column=0, row=2, padx=5, pady=5)
email_input = Entry(width=60)
email_input.grid(column=1, row=2, columnspan=3, padx=5, pady=5)
email_input.insert(0, default_email)


password_title = Label(text="Password:")
password_title.grid(column=0, row=3, padx=5, pady=5)
password_input = Entry(width=30)
password_input.grid(column=1, row=3, padx=5, pady=5)
password_generate_button = Button(text="Generate", width=10)
password_generate_button.grid(column=2, row=3, padx=5, pady=5)
password_generate_button.config(command=generate_password)
password_clipboard_button = Button(text="Copy Text", width=10)
password_clipboard_button.grid(column=3, row=3, padx=5, pady=5)
password_clipboard_button.config(command=save_to_clipboard)

add_button = Button(text="Add to Password Manager", width=36)
add_button.grid(column=0, row=4, columnspan=5, pady=20)
add_button.config(command=save_password)


window.mainloop()
# ----------------------------------------------------------------------------- #
