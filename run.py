# Write your code to expect a terminal of 80 characters wide and 24 rows high
"""
Code Breaker in the style of Mastermind.
A code of four colours will be randomly generated from six colour choices.
Player objective: Guess the correct code within the allowed number of attempts.
Choices: Red (R), Green (G), Blue (B), Yellow (Y), Purple (P), White (W) 
"""

# imports
import random

# constants
COLOUR_CHOICES = ["R", "G", "B", "Y", "P", "W"]
CODE_LENGTH = 4
MAX_ATTEMPTS = 10


# menu/title screen
# press 1 to play
# press 2 for instructions
# press 3 to exit


# function to generate code
def generate_code():
    """
    Generates a 4-colour combination from the 6 choices in COLOUR_CHOICES.
    Duplicates are enabled.
    """
    colour_code = []
    while len(colour_code) < CODE_LENGTH:
        random_colour = random.choice(COLOUR_CHOICES)
        colour_code.append(random_colour)
    return colour_code

print(generate_code())


# function for user input
def player_guess_input(attempt):
    """
    Asks the player to enter their guess, and validates the input.
    """
    while True:
        guess = input("Enter your prediction: \n").upper().strip()

# function to compare user input with code



# display user input with result of comparison



# main game code

