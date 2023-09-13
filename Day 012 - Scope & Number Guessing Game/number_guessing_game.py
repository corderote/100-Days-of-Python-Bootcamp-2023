# ----------------------------------------------------------------------------- #
# Number Guessing Game:
import sys
import os
import random
import number_guessing_game_art


# Clear Screen Function.
def clear_screen():
    """
    This function clears our terminal screen.
    It has dependencies from the system and the operating system that we are
    using, this may cause ERROR.
    NOTE: If ERROR here, check 'sys.platform' and 'os.system' in the API.
    """
    if sys.platform == 'win32':
        os.system('cls')
    elif sys.platform == 'linux':
        os.system('clear')
    elif sys.platform == 'darwin':
        os.system('clear')


def set_game_difficulty():
    game_difficulty_string = ""
    while (game_difficulty_string != 'easy'
           and game_difficulty_string != 'hard'):
        game_difficulty_string = input("Choose a difficulty. "
                                       "Type 'easy' or 'hard': \n")
        game_difficulty_string = game_difficulty_string.lower()

    if game_difficulty_string == "easy":
        attempts = 10
    elif game_difficulty_string == "hard":
        attempts = 5
    else:
        attempts = 0

    return attempts


def get_player_guess():
    player_number = -1
    while player_number < 0 or player_number > 100:
        player_number = int(input("Make a guess: "))
        if player_number < 0 or player_number > 100:
            print(f"Invalid Guess: {player_number}. "
                  "Number has to be between 1 and 100.")
    return player_number


def check_player_number(player_number, computer_number):
    if player_number == computer_number:
        print(f"You got it! The answer was {player_number}.")
        return True
    elif player_number > computer_number:
        print(f"Too High.")
        return False
    elif player_number < computer_number:
        print(f"Too Low.")
        return False
    else:
        print("ERROR: Invalid player number.")
        return False


def play_again():
    want_to_play = ""
    while want_to_play != "yes" and want_to_play != "no":
        want_to_play = input("\nDo you want to play again? "
                             "Type 'yes' or 'no'.\n")
        want_to_play = want_to_play.lower()

    if want_to_play == "yes":
        return True
    else:
        return False


def number_guessing_game():
    clear_screen()
    print(number_guessing_game_art.logo)
    print("Welcome to the Number Guessing Game!")
    print("Im thinking of a number between 1 and 100.")
    game_number = random.randint(1, 100)

    guessing_attempts = set_game_difficulty()
    win_condition = False
    while guessing_attempts > 0 and not win_condition:
        print(f"You have {guessing_attempts} attempts remaining.")
        player_guessed_number = get_player_guess()
        win_condition = check_player_number(player_guessed_number, game_number)
        guessing_attempts -= 1

    if win_condition:
        print("Congratulations! "
              f"You WIN with {guessing_attempts} guessing attempts left.")
    else:
        print("You´ve run out of attempts to guess. You lose.\n"
              f"The number was {game_number}.")
    if play_again():
        number_guessing_game()


number_guessing_game()
# ----------------------------------------------------------------------------- #
