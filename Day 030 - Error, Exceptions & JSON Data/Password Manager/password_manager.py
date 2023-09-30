# ----------------------------------------------------------------------------- #
from tkinter import *
from tkinter import messagebox
import os
import json
import random
import pyperclip

default_email = "polito@things.com"
default_filepath = "./pm_data.json"
logo_filepath = "./pm_logo.png"


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

    new_data = {
        u_web: {
            "email": u_email,
            "password": u_pass,
        }
    }

    try:
        data_file = open(default_filepath, "r")
        # Read old data.
        file_data = json.load(data_file)
        data_file.close()
    except FileNotFoundError:
        data_file = open(default_filepath, "w")
        # Save new_data inside the JSON file.
        json.dump(new_data, data_file, indent=4)
        data_file.close()
    else:
        # Update 'file_data' with our new_data (adding it to the file)
        file_data.update(new_data)
        data_file = open(default_filepath, "w")
        # Save updated_data inside the JSON file.
        json.dump(file_data, data_file, indent=4)
        data_file.close()
    finally:
        website_input.delete(0, END)
        password_input.delete(0, END)
        website_input.focus()


# ---------------------------- UI SETUP --------------------------------------- #
def search_website():
    user_website = website_input.get()
    try:
        data_file = open(default_filepath, "r")
    except FileNotFoundError:
        messagebox.showinfo(title="ERROR",
                            message=f"Database not found or empty.")
    else:
        file_data = json.load(data_file)
        if user_website in file_data:
            user_email = file_data[user_website]["email"]
            user_password = file_data[user_website]["password"]
            messagebox.showinfo(title=user_website,
                                message=f"Username: {user_email}\nPassword: {user_password}\n")
        else:
            messagebox.showinfo(title="ERROR",
                                message=f"{user_website} information not found.")


# ---------------------------- UI SETUP --------------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
window.resizable(False, False)

logo_canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file=logo_filepath)
logo_canvas.create_image(100, 100, image=logo_img)
logo_canvas.grid(column=0, row=0, columnspan=5)

website_title = Label(text="Website:")
website_title.grid(column=0, row=1, padx=5, pady=5)
website_input = Entry(width=30)
website_input.grid(column=1, row=1, columnspan=1, padx=5, pady=5)
website_input.focus()
website_search_button = Button(text="Search", width=20)
website_search_button.grid(column=2, row=1, columnspan=2, padx=5, pady=5)
website_search_button.config(command=search_website)


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
