# ----------------------------------------------------------------------------- #
# Pomodoro App APP
from tkinter import *
# ---------------------------- CONSTANTS -------------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
POMODORO_REPETITIONS = 5

pomodoro_counter = 1
pomodoro_break = False
pomodoro_is_running = False


# ---------------------------- UI UPDATES ------------------------------------- #
def update_pomodoro_checks():
    checks_text = ""
    for i in range(1, POMODORO_REPETITIONS + 1):
        if i < pomodoro_counter:
            checks_text += "✔️"
        elif i == pomodoro_counter and pomodoro_break is True:
            checks_text += "⭕"
        else:
            checks_text += "➖"
    pomodoro_checks.config(text=checks_text)


def update_pomodoro_text():
    title_text = ""
    if pomodoro_is_running:
        if pomodoro_break is False:
            title_text = f"WORK TIME #{pomodoro_counter}"
        else:
            title_text = f"BREAK TIME #{pomodoro_counter}"
    else:
        title_text = "POMODORO APP"
    title.config(text=title_text)


# ---------------------------- TIMER MECHANISMS ------------------------------- #
def start_pomodoro():
    global pomodoro_is_running
    if pomodoro_is_running is False:
        pomodoro_is_running = True
        update_pomodoro_checks()
        update_pomodoro_text()
        countdown(WORK_MIN*60)


def reset_pomodoro():
    global pomodoro_is_running
    global pomodoro_break
    global pomodoro_counter
    pomodoro_counter = 0
    pomodoro_break = False
    pomodoro_is_running = False
    update_pomodoro_checks()
    update_pomodoro_text()


# ---------------------------- COUNTDOWN MECHANISM ---------------------------- #
def countdown(count):
    global pomodoro_is_running
    global pomodoro_break
    global pomodoro_counter
    if pomodoro_is_running:
        seconds = '{:02}'.format(count % 60)
        minutes = '{:02}'.format(int(count / 60))
        canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
        if count > 0:
            window.after(1000, countdown, (count - 1))
        else:
            pomodoro_break = not pomodoro_break
            if pomodoro_break is True:
                if pomodoro_counter < POMODORO_REPETITIONS:
                    countdown(SHORT_BREAK_MIN*60)
                else:
                    countdown(LONG_BREAK_MIN * 60)
            elif pomodoro_break is False:
                if pomodoro_counter < POMODORO_REPETITIONS:
                    pomodoro_counter += 1
                    countdown(WORK_MIN * 60)
                else:
                    pomodoro_counter = 0
                    pomodoro_break = False
                    pomodoro_is_running = False
            update_pomodoro_checks()
            update_pomodoro_text()
    else:
        zero_value = '{:02}'.format(0)
        canvas.itemconfig(timer_text, text=f"{zero_value}:{zero_value}")


# ---------------------------- UI SETUP --------------------------------------- #
window = Tk()
window.title("Pomodoro APP")
window.minsize(width=500, height=375)
window.maxsize(width=500, height=375)
window.config(bg=YELLOW)
# ----------------------------------------------------------------------------- #
# tkinter Canvas Widget.
# It works as a real life canvas. Allows you to put layer on top of other things.
# In our case we are going to use it to print the image that we are going to use
# as the background of our Pomodoro app.
# ----------------------------------------------------------------------------- #
canvas = Canvas(width=250, height=250, bg=YELLOW, highlightthickness=0)
background_image = PhotoImage(file="Pomodoro App/tomato.png")
canvas.create_image(125, 125, image=background_image)
timer_text = canvas.create_text(125, 150, text="00:00", font=(FONT_NAME, 25, "bold"), fill="white")
canvas.grid(column=1, row=1)

title = Label(text="POMODORO APP", font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
title.grid(column=1, row=0, pady=(10, 0))

start_button = Button(fg=GREEN, bg=YELLOW, text="START", font=(FONT_NAME, 15, "bold"))
start_button.grid(column=0, row=2, padx=25, pady=(10, 25))
start_button.config(command=start_pomodoro)

reset_button = Button(fg=GREEN, bg=YELLOW, text="RESET", font=(FONT_NAME, 15, "bold"))
reset_button.grid(column=2, row=2, padx=25, pady=(10, 25))
reset_button.config(command=reset_pomodoro)

pomodoro_checks = Label(text="➖➖➖➖➖", font=(FONT_NAME, 10, "bold"), fg=GREEN, bg=YELLOW)
pomodoro_checks.grid(column=1, row=2)

window.mainloop()
# ----------------------------------------------------------------------------- #
# tkinter after() method. It works as an event listener (kind of?)
# Allows the app to call a method after a time defined in milliseconds.
# window.after(1000, countdown, 75)
# tkinter after_cancel() allows us to break this kind of events, we need to
# assign a variable to know what event we want to stop/cancel.
# ----------------------------------------------------------------------------- #
# DYNAMIC TYPING
# Python is strongly, dynamically typed.
# STRONG TYPING means that the type of value doesn't change in unexpected ways.
# A string containing only digits doesn't magically become a number, as may
# happen in other languages. Every change of type requires an explicit
# conversion.
# DYNAMIC TYPING means that runtime objects (values) have a type, as opposed to
# static typing where variables have a type.

# DYNAMIC TYPING allows us to assign different types to a variable without
# launching an error.
# eg: we can type a = 3, and it will be an int type variable, but nothing can
# stop us from after that typing a = "Hello" and a will become a string type
# variable.
# That is the meaning behind dynamic typing, it allows us to manipulate the
# type behind our variables without questioning it.
# Python is also a 'strongly type' programming language that knows the type of
# the variable that we are assigning and does not let the user use the variable
# as something that type is not ment for.
# ----------------------------------------------------------------------------- #
