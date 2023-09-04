# ----------------------------------------------------------------------------- #
# Rock, Paper, Scissors.

import random

game_images = ["👊", "✋", "✌"]
print("What do you choose?")
player_chose = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if player_chose < 0 or player_chose > 2:
    print("\nERROR: Player chose an Invalid Option.")
else: 
    print("\nPlayer Chose: " + game_images[player_chose])

computer_chose = random.randint(0, 2)
print("\nComputer Chose: " + game_images[computer_chose])

# We create a nested list that covers all the rock paper scissors options.
# Rows will represent the player option and Columns will represent the computer
# option.
rps_map = [["D", "C", "P"],
           ["P", "D", "C"],
           ["C", "P", "D"]]

# Player Win Conditions. 
if player_chose < 0 or player_chose > 2:
    print("\nERROR: Player chose an Invalid Option. You Lose!")
elif rps_map[player_chose][computer_chose] == "P":
    print("\nCongratulations! You Win!\n") 
# Computer Win Conditions
elif rps_map[player_chose][computer_chose] == "C":
    print("\nSorry, you lose this time.\n") 
# Draw Conditions.
elif rps_map[player_chose][computer_chose] == "D":
    print("\nWOW! It's a draw!\n") 
else:
    print("\nERROR: INVALID OPTION!\n")
# ----------------------------------------------------------------------------- #
