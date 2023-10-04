# ----------------------------------------------------------------------------- #
from tkinter import *
import requests
import pandas

# ---------------------------- CONSTANTS -------------------------------------- #
BG_COLOR = "#F0F0F0"
TEXT_COLOR = "#FFFFFF"
FONT_TYPE = ("Arial", 15, "bold")
KW_API_URL = "https://api.kanye.rest"


# ---------------------------- FUNCTIONS -------------------------------------- #
def get_quote():
    kw_api_response = requests.get(KW_API_URL)
    kw_api_response.raise_for_status()
    kw_api_data = kw_api_response.json()
    kw_quote = kw_api_data["quote"]
    canvas.itemconfig(quote_text, text=kw_quote)


# ---------------------------- USER INTERFACE --------------------------------- #
window = Tk()
window.title("Kayne Quotes APP")
window.config(padx=50, pady=50, bg=BG_COLOR)
window.resizable(False, False)

canvas = Canvas(width=300, height=414, bg=BG_COLOR)
background_img = PhotoImage(file="Images/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="", width=250, font=FONT_TYPE, fill=TEXT_COLOR)
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="Images/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

get_quote()
window.mainloop()

# ----------------------------------------------------------------------------- #
