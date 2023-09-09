# ----------------------------------------------------------------------------- #
import sys
import os
import blind_aution_art


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


# Secret auction program.
print("Welcome to the secret auction program.")
auction_bids = {}
more_bids = ""
while more_bids != "no":
    more_bids = ""
    new_name = ""
    print(blind_aution_art.logo)
    # Ask for the bidder name.
    # If bidder already exist, tell the user and ask again.
    bidder_already_exists = True
    while bidder_already_exists:
        bidder_already_exists = False
        new_name = input("What is your name? ")
        for bidder_name in auction_bids:
            if bidder_name == new_name:
                bidder_already_exists = True
                print(f"Name '{new_name}' already used in the auction.")
                print("Please use other name.")
    # Ask for the price to bid.
    new_bid = int(input("What is your bid? "))
    # Add the name and bid to a list or a dictionary.
    auction_bids[new_name] = new_bid
    # Asks if there is any other bidder until you answer yes or no. 
    while more_bids != "no" and more_bids != "yes":
        more_bids = input("Are there any other bidders? Type 'yes' or 'no'. ")
        more_bids = more_bids.lower() 
    clear_screen()

# Check for the highest bid inside the auction bids. 
winner_name = "ERROR: No bidders found."
winner_bid = 0
for bidder_name in auction_bids:
    if auction_bids[bidder_name] > winner_bid:
        winner_name = bidder_name
        winner_bid = auction_bids[bidder_name]

# Print the winner of the auction.
print(f"The winner is {winner_name} with a bid of {winner_bid}.")
# ----------------------------------------------------------------------------- #
