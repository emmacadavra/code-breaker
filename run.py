# Write your code to expect a terminal of 80 characters wide and 24 rows high
"""
Code Breaker in the style of Mastermind.
A code of four colours will be randomly generated from six colour choices.
Player objective: Guess the correct code within the allowed number of attempts.
Choices: Red (R), Green (G), Blue (B), Yellow (Y), Pink (P), White (W) 
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
        guess_list = [g for g in guess]
        if len(guess_list) != CODE_LENGTH:
            print(f"Invalid - please enter {CODE_LENGTH} characters.\n")
            continue

        for character in guess_list:
            if character not in COLOUR_CHOICES:
                print(f"Error: {character} is not a valid character.")
                print("Choose only from the following characters: R  G  B  Y  P  W")
                print("Please do not use commas or spaces.\n")
                break

    return guess_list


# function to compare user input with code
def check_result(guess, answer):
    for i in range(CODE_LENGTH):
        correct_position = 0
        correct_colour = 0

        if guess[i] == answer[i]:
            guess[i] = 0
            answer[i] = 0
            correct_position += 1
        index_count = guess.count(0)

    while index_count > 0:
        guess.remove(0)
        index_count = guess.count(0)



# display user input with result of comparison



# main game code

