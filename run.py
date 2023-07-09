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
COLOUR_CHOICES = ["R", "G", "Y", "B", "P", "W"]
CODE_LENGTH = 4
MAX_ATTEMPTS = 9

# colour class
class Colours:
    """
    ANSI escape codes to be used with their respective colours
    """
    red = "\033[1;31;40m"
    green = "\033[1;32;40m"
    yellow = "\033[1;33;40m"
    blue = "\033[1;34;40m"
    pink = "\033[1;35;40m"


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


# function for user input
def player_guess_input(attempt):
    """
    Asks the player to enter their guess, and validates the input.
    """
    invalid_input = True
    while invalid_input:
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
            invalid_input = False

    return guess_list


# function to compare user input with code
def check_result(guess, answer):
    correct_position = 0
    correct_colour = 0
    for i in range(CODE_LENGTH):
        if guess[i] == answer[i]:
            correct_position += 1
            guess[i] = 0
            answer[i] = 0
        index_count = guess.count(0)

    while index_count > 0:
        guess.remove(0)
        index_count = guess.count(0)

    for i in range(len(guess)):
        if guess[i] in answer:
            correct_colour += 1
            answer.remove(guess[i])

    return correct_position, correct_colour 


# display user input with result of comparison



# main game code
def run_game():
    """
    Run main game functions
    """
    original_answer = generate_code()
    print(original_answer)

    attempt_number = 0

    while attempt_number <= MAX_ATTEMPTS:
        player_guess = player_guess_input(attempt_number)
        modified_answer = list(original_answer)
        position, colour = check_result(player_guess, modified_answer)
        if position == CODE_LENGTH:
            print("You cracked the code!")
            print(f"You did it in {attempt_number + 1} attempt(s).\n")
            break
        elif attempt_number == MAX_ATTEMPTS and position != CODE_LENGTH:
            print("Oh no! You weren't able to crack the code this time.")
            # print("Try again?")
            break
        else:
            attempt_number += 1
            print(f"Correct colour and position: {position}")
            print(f"Correct colour, but incorrect position: {colour}")
            print(f"You have {MAX_ATTEMPTS - attempt_number + 1} attempt(s) remaining.\n")


# menu/title screen
def menu():
    """
    Title screen/menu with options:
    Press 1 to play
    Press 2 for instructions
    press 3 to exit
    """
    print("""
            Press '1' to Play Game
            Press '2' for Instructions
            Press '3' for Triforce
            Press '4' to Exit
            """)

    while True:
        try:
            menu_select = int(input("Press key: \n"))
            
            if menu_select == 1:
                run_game()
                break
            elif menu_select == 2:
                print("These are some instructions!")
                break
            elif menu_select == 3:
                print("This will be a picture of the Triforce for fun")
                break
            elif menu_select == 4:
                print("This will exit the program (I think?)")
                break
            else:
                raise ValueError
        
        except ValueError:
            print("""
                Invalid key press. Please choose from the following:\n
                Press '1' to Play Game
                Press '2' for Instructions
                Press '3' for Triforce
                Press '4' to Exit
                """)


menu()