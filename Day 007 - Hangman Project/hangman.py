# ----------------------------------------------------------------------------- #
import sys
import os
import random
import hangman_art
import hangman_words


# This function clears our terminal screen. It has dependencies from the system
# and the operating system that we are using, this may cause ERROR. 
# NOTE: If ERROR here, check sys.platform and os.system on the python API.
def clear_screen():
    if sys.platform == 'win32':
        os.system('cls')
    elif sys.platform == 'linux':
        os.system('clear')
    elif sys.platform == 'darwin':
        os.system('clear')


# Pick a random word from hangman_words.py. 
words_list = hangman_words.word_list 
chosen_word = random.choice(words_list)
# Generate the blank spaces display word.
display_word_list = []
for _ in chosen_word: 
    display_word_list.append("_")
    
# Global variables for our hangman game.
player_lives = 5
end_of_game = False
guessed_letters_list = []

# Display the start the game screen.
clear_screen()
print(f"{hangman_art.logo}")

# Game Loop.
while not end_of_game:
    # Display the word to guess progress (blank spaces the first time.) 
    print(f"Word to guess:\n{''.join(display_word_list)}\n") 
    # Display the hangman state and the player lives.
    hangman_stage = hangman_art.stages[player_lives + 1]
    print(f"{hangman_stage}Remaining Lives: {player_lives}")
    # Ask the player for a guess. 
    guessed_letter = input("Guess a letter: ").lower() 

    clear_screen()

    # Check if the guessed letter has already been used.
    if guessed_letter not in guessed_letters_list:
        # If not used already add it to the letters used list.
        guessed_letters_list.append(guessed_letter)
        # Check if the guessed letter is in out chosen word. 
        # If so, add the letter guessed to our display word.
        for letter_position in range(len(chosen_word)): 
            if chosen_word[letter_position] == guessed_letter:
                display_word_list[letter_position] = guessed_letter
        # If the guessed letter is not in the chosen word, player loses a life.
        if guessed_letter not in chosen_word:
            print(f"'{guessed_letter}' is not in the word. You lose a life.")
            player_lives -= 1
            # If player loses a life, check the game lose condition.
            if player_lives < 0:
                end_of_game = True
                print(f"{hangman_art.stages[player_lives + 1]}")
                print("\nSorry, you lose this time, better luck next one.\n")
        # Win condition check.
        if "_" not in display_word_list:
            end_of_game = True
            print("\nCONGRATULATIONS! YOU WIN!\n")

    else:
        # If used already. Tell that to the player without penalize him.
        print(f"'{guessed_letter}' Already used. Try again.")
# ----------------------------------------------------------------------------- #
