# ----------------------------------------------------------------------------- #
# Blackjack Project
import sys
import os
import random
import blackjack_art


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


# Close program Function.
def want_to_play(rounds):
    """ 
    End of game function. 
    Requires from a global variable to count the rounds from a session.
    Prints a different message if is the first time this function is called. 
    """
    keep_playing = ""
    while keep_playing != "yes" and keep_playing != "no":
        if rounds <= 0:
            keep_playing = input("Do you want to play a game of Blackjack? "
                                 "Type 'yes' or 'no'.\n").lower()
        else:
            keep_playing = input("Do you want to play another round? "
                                 "Type 'yes' or 'no'.\n").lower()
    
    if keep_playing == "yes":
        return True
    else:
        return False


# Dealing Cards Function.
def deal_cards(hand, number_of_cards):
    """ 
    Function that adds a number of random cards to a hand.
    Takes as parameters a list (hand) and the number of cards you want to add. 
    """
    new_hand = hand
    for _ in range(number_of_cards):
        new_card_number = random.randint(1, 13)
        new_card_key = ""
        if 1 < new_card_number < 11:
            new_card_key = str(new_card_number)
        elif new_card_number == 1:
            new_card_key = "A"
        elif new_card_number == 11:
            new_card_key = "J"
        elif new_card_number == 12:
            new_card_key = "Q"
        elif new_card_number == 13:
            new_card_key = "K"
        new_hand.append(new_card_key)
    return new_hand


# Print hand function.
def print_hand_cards(hand, number_of_cards=0):
    """
    This function prints the cards from a list (hand).
    Takes as parameters the list(hand) and the number of cards to print.
    If the second parameter is 0 or blank, it prints the full list(hand).
    """
    if number_of_cards != 0:
        for card_number in range(0, number_of_cards):
            print(f"[{hand[card_number]}]")
    else:
        for card in hand:
            print(f"[{card}]")


# Function that converts a list into a string.
def string_from_hand_cards(hand, number_of_cards=0):
    """
    This function takes a list(hand) and formats the list into a string.
    it takes the list(hand) and the number of cards that you want to 
    convert into the string. If the value for number of cards is 0 or not 
    given, it takes into account all the items from the list(hand)
    """
    hand_string = ""
    if number_of_cards != 0:
        for card_number in range(0, number_of_cards):
            hand_string += str(f"[{hand[card_number]}]")
    else:
        for card in hand:
            hand_string += str(f"[{card}]")
    return hand_string


# Function to calculate the value of a blackjack hand.
def check_hand_value(hand):
    """
    Takes a list(hand) of cards and returns its value as a blackjack hand.
    """
    hand_value = 0
    aces_in_hand = 0
    for card in hand:
        hand_value += cards_dictionary[card]
        # Save number of aces.
        if card == "A":
            aces_in_hand += 1
    # If we have ACES in our hand and our value is greater than 21.
    if "A" in hand and hand_value > 21:
        # While we have aces and our score is above 21, convert each ace value
        # to 1 until our score is below 21.
        while hand_value > 21 and aces_in_hand > 0:
            hand_value -= 10
            aces_in_hand -= 1
    return hand_value


# Cards Dictionary Variable.
cards_dictionary = {
    "A": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
}
game_rounds = 0

# End of game condition.
while want_to_play(game_rounds):
    clear_screen()
    game_rounds += 1
    computer_hand = []
    player_hand = []
    first_round_blackjack = False
    print(blackjack_art.logo)

    # Deal 2 cards to each player. (user and computer)
    computer_hand = deal_cards(computer_hand, 2)
    player_hand = deal_cards(player_hand, 2)

    # Check if computer or player has Blackjack on first round for the win. 
    # COMPUTER HAS PREFERENCE IN THIS STEP.
    if check_hand_value(computer_hand) == 21:
        print(f"Your Cards: {string_from_hand_cards(player_hand)}.")
        print("Computer has BLACKJACK! " 
              f"{string_from_hand_cards(computer_hand)}.")
        print("COMPUTER WINS!")
        first_round_blackjack = True
    elif check_hand_value(player_hand) == 21:
        print(f"Computer Cards: {string_from_hand_cards(computer_hand)}.")
        print(f"Player has BLACKJACK! {string_from_hand_cards(player_hand)}.")
        print("PLAYER WINS!")
        first_round_blackjack = True
    else:
        print(f"Your Cards: {string_from_hand_cards(player_hand)}.")
        print(f"Computer First Card: "
              f"{string_from_hand_cards(computer_hand, 1)}.")

    if not first_round_blackjack:
        keep_dealing_cards = ""
        # Keep dealing cards as long as the user wants without busting.
        while (keep_dealing_cards != "pass" 
               and check_hand_value(player_hand) < 21):
            keep_dealing_cards = input("Deal another card or pass? "
                                       "Type 'deal' or 'pass'.\n")
            keep_dealing_cards = keep_dealing_cards.lower()
            if keep_dealing_cards == "deal":
                player_hand = deal_cards(player_hand, 1)
                print(f"Your Cards: {string_from_hand_cards(player_hand)}.")
            elif (keep_dealing_cards != "deal" 
                  and keep_dealing_cards != "pass"):
                print(f"ERROR: Invalid command '{keep_dealing_cards}'. "
                      "Try again.")
        
        # Update Computer hand until it reaches a value more than 16.
        while (check_hand_value(computer_hand) < 16 
               and check_hand_value(player_hand) <= 21):
            computer_hand = deal_cards(computer_hand, 1)

        player_final_score = check_hand_value(player_hand)
        computer_final_score = check_hand_value(computer_hand)
        # Print final hands from player and computer.        
        print(f"Your Final Hand: {string_from_hand_cards(player_hand)} "
              f"= {str(player_final_score)}")
        print(f"Computer Final Hand: {string_from_hand_cards(computer_hand)} "
              f"= {str(computer_final_score)}")

        # Check for the winner and send the message. 
        if computer_final_score <= 21 and player_final_score <= 21:
            if computer_final_score == player_final_score:
                print("It´s a Draw!")
            elif computer_final_score > player_final_score:
                print("Computer WINS! Better luck next time!")
            elif computer_final_score < player_final_score:
                print("Congratulations! You WIN!")
        elif computer_final_score > 21 >= player_final_score:
            print("Congratulations! You WIN!")
        elif computer_final_score <= 21 < player_final_score:
            print("Sorry, you busted. Computer WINS! Better luck next time!")
# ----------------------------------------------------------------------------- #
