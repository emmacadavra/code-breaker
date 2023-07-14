"""
MasterCode - a code breaker game in the style of Mastermind.
"""

# imports
import random
from classes.graphics import main_logo, triforce
from classes.colors import Colors

# constants
COLOR_CHOICES = ["R", "G", "B", "Y", "P", "W"]
CODE_LENGTH = 4
MAX_ATTEMPTS = 9

# menu/title screen
def main_menu():
    """
    Title screen/menu with player options
    """
    print(main_logo())
    print("Welcome to MasterCode!\n")

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
                instructions()
                break
            elif menu_select == 3:
                triforce()
                break
            elif menu_select == 4:
                print("Exiting program...")
                print("Program closed.")
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



# instructions on how to play
def instructions():
    """
    Instructions for the user on how to play the game
    """
    print("Instructions on how to play MasterCode:\n")
    print("A secret code of four colours will be randomly generated from the following colours:\n")
    print(f"{Colors.red}R  {Colors.green}G  {Colors.blue}B  {Colors.yellow}Y  {Colors.pink}P  {Colors.white}W{Colors.default}")
    print(f"{Colors.red_block} {Colors.default}  {Colors.green_block} {Colors.default}  {Colors.blue_block} {Colors.default}  {Colors.yellow_block} {Colors.default}  {Colors.pink_block} {Colors.default}  {Colors.white_block} {Colors.default}\n")
    print("Your heroic challenge is to find the solution in 10 attempts or fewer.")
    print("In doing so, you will become a MasterCode breaker!\n")
    print("A colour may appear more than once in the secret code, so don't forget to consider this!")
    print("The terminal will ONLY accept answers that are 4 characters long, with no commas or spaces.")
    print("Make sure you only use the following characters for their respective colours:\n")
    print(f"{Colors.red}R  {Colors.green}G  {Colors.blue}B  {Colors.yellow}Y  {Colors.pink}P  {Colors.white}W{Colors.default}\n")
    print(f"{Colors.white}Go forth, hero, and become the MasterCode breaker!{Colors.default}\n")


# function to generate code
def generate_code():
    """
    Generates a 4-color combination from the 6 choices in COLOR_CHOICES.
    Duplicates are enabled.
    """
    color_code = []
    while len(color_code) < CODE_LENGTH:
        random_color = random.choice(COLOR_CHOICES)
        color_code.append(random_color)
    return color_code


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
        print(f"{display_player_guess(player_guess)}")
        position, color = check_result(player_guess, modified_answer)
        if position == CODE_LENGTH:
            print("You cracked the code like a true Hero!")
            print(f"You defeated this challenge in {Colors.white}{attempt_number + 1}{Colors.default} attempt(s).\n")
            break
        elif attempt_number == MAX_ATTEMPTS and position != CODE_LENGTH:
            print("Oh no! You weren't able to crack the code this time.")
            # print("Try again?")
            break
        else:
            attempt_number += 1
            print(f"Correct colour and position: {position}")
            print(f"Correct colour, but incorrect position: {color}")
            print(f"You have {Colors.white}{MAX_ATTEMPTS - attempt_number + 1}{Colors.default} attempt(s) remaining.\n")


# function for user input
def player_guess_input(attempt):
    """
    Asks the player to enter their guess, and validates the input.
    """
    while True:
        try:
            guess = input("Enter your prediction: \n", end="").upper()
            guess_list = [g for g in guess]

            if len(guess_list) != CODE_LENGTH:
                raise ValueError(f"Invalid - please enter {CODE_LENGTH} characters, with no commas or spaces.\n")
                continue

            for character in guess_list:
                if character not in COLOR_CHOICES:
                    raise ValueError(f"Error: '{character}' is not a valid character.\n" +
                                    f"Choose only from the following characters, with no commas or spaces:\n" +
                                    f"{Colors.red}R  {Colors.green}G  {Colors.blue}B  {Colors.yellow}Y  {Colors.pink}P  {Colors.white}W{Colors.default}\n")
            
            break

        except ValueError as e:
            print(e)

    return guess_list


# display the player's guess in colour
def display_player_guess(guess):
    """
    Displays the player's guess as a string of color blocks
    """
    output=""
    for item in guess:
        if item == "R":
            output += f" {Colors.red_block} {Colors.default}"
        elif item == "G":
            output += f" {Colors.green_block} {Colors.default}"
        elif item == "B":
            output += f" {Colors.blue_block} {Colors.default}"
        elif item == "Y":
            output += f" {Colors.yellow_block} {Colors.default}"
        elif item == "P":
            output += f" {Colors.pink_block} {Colors.default}"
        elif item == "W":
            output += f" {Colors.white_block} {Colors.default}"
    return output


# function to compare user input with code
def check_result(guess, answer):
    correct_position = 0
    correct_color = 0
    for i in range(CODE_LENGTH):
        if guess[i] == answer[i]:
            correct_position += 1
            guess[i] = 0
            answer[i] = 0
        index_count = guess.count(0)

    while index_count > 0:
        guess.remove(0)
        index_count = guess.count(0)

    for i, letter in enumerate(guess):
        if letter in answer:
            correct_color += 1
            answer.remove(letter)

    return correct_position, correct_color 


# main function 
main_menu()
