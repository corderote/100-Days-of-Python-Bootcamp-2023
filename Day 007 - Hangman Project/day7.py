# ----------------------------------------------------------------------------- #
# HANGMAN 
# Today's objective is to develop a Hangman terminal version using Python.
# Our first step will be to make a flowchart of the Hangman game.
# The flowchart is a paper representation on how the program will behave.
# We can find a couple of flowcharts examples in the Hangman project folder.
# ----------------------------------------------------------------------------- #
# STEPS LIST
# 1- Choose a random word from a words list.
# 2- Ask the user to guess a letter.
# 3- Check if the guessed letter is part of the chosen word.
# 4- Create an empty list called display, fill it with blanks according to the
#    chosen word number of letters.
# 5- If the guessed letter is in the word, change the blank spaces from the 
#    display word to the guess. 
# 6- Print the display word.
# 7- Use a while loop to let the user guess again until he finds the correct 
#    word. This is the Win Condition.
# 8- Add and keep track of the player lives. This is the Lose Condition.
# 9- QoL Improvements: 
#    --> Use a proper word list from hangman_words.py
#    --> Import the hangman logo and stages from hangman_art.py
# ----------------------------------------------------------------------------- #
# TODO: FIX: Handle player inputs that are not valid. [strings or numbers]
# ----------------------------------------------------------------------------- #

import sys
import os
import random
import hangman_art
import hangman_words


# ----------------------------------------------------------------------------- #
# This function clears our terminal screen. It has dependencies from the system
# and the operating system that we are using, this may cause ERROR. 
# NOTE: If ERROR here, check sys.platform and os.system on the python API.
def clear_screen():
    if sys.platform == 'win32':
        # 'cls' works to clear the screen in Windows.
        os.system('cls') 
    elif sys.platform == 'linux':
        # 'clear' works to clear the screen in Linux.
        os.system('clear')
    elif sys.platform == 'darwin':
        # 'clear' works to clear the screen in Mac.
        os.system('clear')


# Choose a random word from the word list.
# words_list = ["word", "cat", "random", "hangman", "project"]
# QoL Improvement #1
words_list = hangman_words.word_list 
chosen_word = random.choice(words_list)
display_word_list = []

for _ in chosen_word: 
    display_word_list.append("_")
# range(len(chosen_word)) is also a valid solution.

player_lives = 5
end_of_game = False
guessed_letters_list = []

# QoL improvement #2
clear_screen()
print(f"{hangman_art.logo}")

while not end_of_game:
    # Ask the user to guess a letter.
    # To print the list as a string we use the str.join() method.
    print(f"Word to guess:\n{''.join(display_word_list)}\n") 
    # QoL improvement #3:

    hangman_stage = hangman_art.stages[player_lives + 1]
    print(f"{hangman_stage}Remaining Lives: {player_lives}")
    guessed_letter = input("Guess a letter: ").lower() 
    # We use str.lower() to convert the input result to lowercase. 

    clear_screen()

    if guessed_letter not in guessed_letters_list:
        guessed_letters_list.append(guessed_letter)
        # Find the letter in the chosen word.
        for letter_position in range(len(chosen_word)): 
            if chosen_word[letter_position] == guessed_letter:
                display_word_list[letter_position] = guessed_letter

        if guessed_letter not in chosen_word:
            print(f"'{guessed_letter}' is not in the word. You lose a life.")
            player_lives -= 1
            # LOSE CONDITION CHECK
            if player_lives < 0:
                end_of_game = True
                print(f"{hangman_art.stages[player_lives + 1]}")
                print("\nSorry, you lose this time, better luck next one.\n")

# ----------------------------------------------------------------------------- #
# NOTE: Here we have 2 different win condition checks, only one is needed in 
#       order to make our program work as intended. Both are valid.
# ----------------------------------------------------------------------------- #

        # WIN CONDITION CHECK #1
        # Check if our list still has any blank space on it. 
        if "_" not in display_word_list:
            end_of_game = True
            print("\nCONGRATULATIONS! YOU WIN!\n")
    
        # WIN CONDITION CHECK #2
        # Convert display_word_list into a string. 
        display_word = ""
        for letter in display_word_list:
            display_word += letter
        # "".join(display_word_list) also works to turn the list into a string.
        if display_word.find("_") == -1:
            end_of_game = True
        # The find() function with strings arguments returns the first index of 
        # our string where we can find the argument that we have given. 
        # It returns '-1' if our input is not in the string.
        
    else:
        print(f"'{guessed_letter}' Already used. Try again.")
# ----------------------------------------------------------------------------- #
