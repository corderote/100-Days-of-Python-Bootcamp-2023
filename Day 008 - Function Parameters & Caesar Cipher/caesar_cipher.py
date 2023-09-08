# ----------------------------------------------------------------------------- #
import sys
import os
import caesar_art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
end_program = False


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


def caesar_encrypt(plain_text, shift_amount, cipher_direction):
    # Handle the decryption shift.
    if cipher_direction == "decode":
        shift_amount *= -1
    # Check every letter in the message.
    end_text = ""
    for letter in plain_text:
        # If is part of the alphabet shift it.
        if letter in alphabet:
            alphabet_position = alphabet.index(letter)
            new_alphabet_pos = alphabet_position + shift_amount
            alphabet_lim = len(alphabet)-1
            # Check that the new alphabet position is always within bounds.
            while (new_alphabet_pos > alphabet_lim) or (new_alphabet_pos < 0):
                if new_alphabet_pos > alphabet_lim:
                    new_alphabet_pos -= len(alphabet)
                if new_alphabet_pos < 0:
                    new_alphabet_pos += len(alphabet)
            # Add the new letter to the now encrypted or decrypted text.
            new_letter = alphabet[new_alphabet_pos]
            end_text += new_letter
        # If is not part of the alphabet just add it to the end text.
        else:
            end_text += letter
    # Print the result.
    print(f"The {cipher_direction}d text is: {end_text}")


while not end_program:
    # Initialize Variables.
    direction = ""
    close_program = ""
    # Print Logo.
    clear_screen()
    print(caesar_art.logo)
    # Check if the user wants to encrypt a message or decrypt one.
    while direction != "encode" and direction != "decode":
        direction = input("Type 'encode' to encrypt,"
                          " type 'decode' to decrypt: ")
        direction = direction.lower()

    # Input the message and the shift that the user wants to apply.
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    # Call to the encrypting function.
    caesar_encrypt(text, shift, direction)

    # Check if the user wants to close the program or keep using it.
    while close_program.lower() != "yes" and close_program.lower() != "no":
        close_program = input("Close the program? Type 'yes' or 'no': ")
        if close_program == "yes":
            end_program = True
# ----------------------------------------------------------------------------- #
