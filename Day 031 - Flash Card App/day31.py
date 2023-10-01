# ----------------------------------------------------------------------------- #
from tkinter import *
import pandas
import random
import os

# ---------------------------- CONSTANTS -------------------------------------- #
BG_COLOR = "#b1ddc6"
WORD_COLOR_FRONT = "#111111"
WORD_COLOR_BACK = "#EEEEEE"
FONT_NAME = "Arial"


# ---------------------------- FILE MANAGEMENT -------------------------------- #
def check_filepath_exists(filepath):
    return os.path.isfile(filepath)


def check_filepath_is_empty(filepath):
    if os.path.getsize(filepath) > 0:
        return False
    else:
        return True


def create_file(filepath):
    file = open(filepath, mode="w")
    file.close()


# ---------------------------- LOAD DATA -------------------------------------- #
data_filepath = "./Data/french_words.csv"
learned_words_filepath = "./Data/learned_words.csv"
data_df = pandas.read_csv(data_filepath)
data_dict = data_df.to_dict(orient="records")
current_word_dict = {}

if check_filepath_exists(learned_words_filepath) is False:
    create_file(learned_words_filepath)

if check_filepath_is_empty(learned_words_filepath) is False:
    learned_df = pandas.read_csv(learned_words_filepath)
    learned_dict = learned_df.to_dict(orient="records")

    for item in learned_dict:
        data_dict.remove(item)

print(data_dict)


# ---------------------------- FUNCTIONS -------------------------------------- #
def change_card():
    global data_dict
    global current_word_dict
    global window
    global flip

    window.after_cancel(flip)
    current_word_dict = random.choice(data_dict)
    card_language_text = list(current_word_dict.keys())[0]
    card_word_text = current_word_dict[card_language_text]
    card.itemconfig(bg_image, image=card_front_image)
    card.itemconfig(language_text, text=card_language_text, fill=WORD_COLOR_FRONT)
    card.itemconfig(word_text, text=card_word_text, fill=WORD_COLOR_FRONT)
    flip = window.after(3000, flip_card, current_word_dict)


def flip_card(word_dict):
    card_language_text = list(word_dict.keys())[1]
    card_word_text = word_dict[card_language_text]
    card.itemconfig(bg_image, image=card_back_image)
    card.itemconfig(language_text, text=card_language_text, fill=WORD_COLOR_BACK)
    card.itemconfig(word_text, text=card_word_text, fill=WORD_COLOR_BACK)


def word_known():
    global current_word_dict

    learned_word_list = [[current_word_dict[list(current_word_dict.keys())[0]],
                         current_word_dict[list(current_word_dict.keys())[1]]]]
    learned_word_cols = [list(current_word_dict.keys())[0],
                         list(current_word_dict.keys())[1]]

    learned_word = pandas.DataFrame(learned_word_list, columns=learned_word_cols)

    if check_filepath_is_empty(learned_words_filepath) is True:
        learned_word.to_csv(learned_words_filepath, index=False)
    else:
        l_df = pandas.read_csv(learned_words_filepath)
        final_learned_df = pandas.concat([l_df, learned_word])
        final_learned_df.to_csv(learned_words_filepath, index=False)

    data_dict.remove(current_word_dict)
    change_card()


# ---------------------------- USER INTERFACE --------------------------------- #
window = Tk()
window.title("Flash Card APP")
window.config(padx=50, pady=50, bg=BG_COLOR)
window.resizable(False, False)

flip = window.after(3000, flip_card)

card_front_image = PhotoImage(file="Images/card_front.png")
card_back_image = PhotoImage(file="Images/card_back.png")
right_image = PhotoImage(file="Images/right.png")
wrong_image = PhotoImage(file="Images/wrong.png")

card = Canvas(width=800, height=530, bg=BG_COLOR, highlightthickness=0)
bg_image = card.create_image(400, 265, image=card_front_image)
language_text = card.create_text(400, 175, text="lang_1", font=(FONT_NAME, 20, "normal italic"))
word_text = card.create_text(400, 250, text="lang_2", font=(FONT_NAME, 40, "bold"))
card.grid(column=0, row=0, columnspan=2)


right_button = Button(image=right_image, highlightthickness=0)
wrong_button = Button(image=wrong_image, highlightthickness=0)
right_button.grid(column=0, row=1, pady=(25, 0))
wrong_button.grid(column=1, row=1, pady=(25, 0))

right_button.config(command=word_known)
wrong_button.config(command=change_card)

# ---------------------------- LOOP ------------------------------------------- #

change_card()
window.mainloop()

# ---------------------------- RESOURCES -------------------------------------- #

# Wikipedia: Frequency Lists.
# https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists

# GitHub Frequency Words [2018]:
# https://github.com/hermitdave/FrequencyWords/tree/master/content/2018

# Open Subtitles:
# https://www.opensubtitles.org/en/search/subs

# Google Translate for Google Sheets:
# https://support.google.com/docs/answer/3093331?hl=en-GB

# Google Languages Support:
# https://cloud.google.com/translate/docs/languages?hl=en

# ----------------------------------------------------------------------------- #
