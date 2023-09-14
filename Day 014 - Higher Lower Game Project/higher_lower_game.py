# ----------------------------------------------------------------------------- #
# Higher Lower Game.

import sys
import os
import random
import higher_lower_art
import higher_lower_data


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


def get_higher_lower_data(other_data=None):
    """
    This function returns one data from the higher_lower_data.py file.
    If its given an Argument, it will make sure to return a data value 
    different from that 'other_data'.
    """
    # If our function has no ARGUMENT, just choose one from the data.
    if other_data is None:
        new_data = random.choice(higher_lower_data.data)
    # Else check that the data that we return does not match the data used 
    # as argument.
    else:
        new_data = random.choice(higher_lower_data.data)
        while new_data == other_data:
            new_data = random.choice(higher_lower_data.data)
    return new_data


def compare_followers(ig_data_a, ig_data_b):
    """
    This function will compare two datas from the higher_lower_data.py file.
    It will return 'A' if the first data follower_count value is higher, 'B' 
    if the second data follower_count value is higher, and 'draw' if they are 
    the same value.
    """
    if ig_data_a["follower_count"] > ig_data_b["follower_count"]:
        return "A"
    elif ig_data_a["follower_count"] < ig_data_b["follower_count"]:
        return "B"
    else:
        return "draw"


def format_data(ig_data):
    """
    Takes a data from higher_lower_data.py and formats a string without
    spoiling the follower_count value.
    Data is formatted to feel good inside the higher_lower game.
    """
    ig_name = ig_data["name"]
    ig_description = ig_data["description"]
    ig_location = ig_data["country"]
    return f"{ig_name}, a {ig_description} from {ig_location}."


def get_player_guess(): 
    """
    This function keeps assign the player to input 'A' or 'B' until he inputs
    any of those values. 
    """
    user_guess = ""
    while user_guess != "A" and user_guess != "B":
        user_guess = input("\nWho has more followers? Type 'A' or 'B': ")
        user_guess = user_guess.upper()
    return user_guess


def check_lose_condition(computer_value, user_value):
    """
    Checks if the computer value and the user value are the same so the player
    can continue playing.
    Returns True both values are the same or computer value == 'draw'. 
    Returns True otherwise.
    """
    if computer_value == "draw":
        return False
    elif computer_value == user_value:
        return False
    else: 
        return True


def play_again():
    """
    Asks the player if it wants to play again and keeps asking until the input
    is equal to 'yes' or 'no'.
    Returns True if the player inputs 'yes'.
    Returns False if the player inputs 'no'.
    """
    want_to_play = ""
    while want_to_play != "yes" and want_to_play != "no":
        want_to_play = input("\nDo you want to play again? "
                             "Type 'yes' or 'no'.\n")
        want_to_play = want_to_play.lower()
    if want_to_play == "yes":
        return True
    else:
        return False


def higher_lower_game():

    lose_condition = False
    rounds_counter = 0
    ig_account_1 = None
    ig_account_2 = None
    ig_winner = ""

    while not lose_condition:
        clear_screen()
        print(higher_lower_art.logo)
        # If first round, set a random ig_data from the higher_lower_data.py, 
        # else, keep the winner ig_data.
        if rounds_counter == 0:
            ig_account_1 = get_higher_lower_data()
        else:
            print("\nYou are right! "
                  f"Your Current Score is: {rounds_counter}.\n")
            if ig_winner == "B":
                ig_account_1 = ig_account_2

        # Set second ig_data, checking that is not the same as ig_data_1
        ig_account_2 = get_higher_lower_data(ig_account_1)

        print(f"Compare A: {format_data(ig_account_1)}")
        print(higher_lower_art.vs)
        print(f"Against B: {format_data(ig_account_2)}")

        # Check the winner from the database and get the player guess.
        ig_winner = compare_followers(ig_account_1, ig_account_2)
        player_guess = get_player_guess()
        # Check if player and ig_winner have the same value to verify for the 
        # losing condition.
        lose_condition = check_lose_condition(ig_winner, player_guess)
        # If we keep playing, add one to the score counter, if not, print the 
        # final score.
        if not lose_condition:
            rounds_counter += 1
        else:
            print("\nSorry, that's wrong. " 
                  f"YOUR FINAL SCORE IS: {rounds_counter}.\n")

    # Ask the user if it wants to keep playing.
    if play_again():
        higher_lower_game()


# Game Starts.
higher_lower_game()
# ----------------------------------------------------------------------------- #
