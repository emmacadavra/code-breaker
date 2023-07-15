"""
MasterCode - a code breaker game in the style of Mastermind, heavily themed around text adventure style games and The Legend of Zelda.
"""
# imports
import random
import os
import classes.graphics as graphics
from classes.colors import Colors


# constants
COLOR_CHOICES = ["R", "G", "B", "Y", "P", "W"]
CODE_LENGTH = 4
MAX_ATTEMPTS = 11


# menu/title screen
def main_menu():
    """
    Title screen/menu with player options
    """
    clear_screen()
    graphics.main_logo()
    print("~*~ Press '1' to Play   ~*~   Press '2' for Instructions ~*~")
    print("~*~ Press '3' for the Triforce   ~*~   Press '4' to Exit ~*~")

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
                clear_screen()
                graphics.triforce()
                play_again()
                break
            elif menu_select == 4:
                graphics.divider_image()
                print(f"""
                   {Colors.white}Exiting game...

                   ...Game closed.{Colors.default}
                """)
                graphics.divider_image()
                break
            else:
                raise ValueError

        except ValueError:
            print("""
        Invalid key press. Please choose from the following:\n
        ~*~ Press '1' to Play   ~*~   Press '2' for Instructions ~*~
        ~*~ Press '3' for the Triforce   ~*~   Press '4' to Exit ~*~
            """)


# instructions on how to play
def instructions():
    """
    Instructions for the user on how to play the game
    """
    # clear the screen and input the header image
    clear_screen()
    graphics.header_image()

    # display the game instructions to the player
    print(f"A secret code of 4 colors will be randomly generated from the following colors:\n")
    print(f"    {Colors.red}Red  {Colors.green}Green  {Colors.blue}Blue  {Colors.yellow}Yellow  {Colors.purple}Purple  {Colors.white}White{Colors.default}\n")
    print("Your heroic challenge is to find the solution in 12 attempts or fewer.")
    print("Remember: a color may appear more than once in the secret code!")
    print("Only type guesses that are 4 characters long with no commas or spaces.\n")
    print("Make sure you only use the following characters for their respective colors:\n")
    print(f"    {Colors.red}R  {Colors.green}G  {Colors.blue}B  {Colors.yellow}Y  {Colors.purple}P  {Colors.white}W{Colors.default}")
    print(f"    {Colors.red_block} {Colors.default}  {Colors.green_block} {Colors.default}  {Colors.blue_block} {Colors.default}  {Colors.yellow_block} {Colors.default}  {Colors.purple_block} {Colors.default}  {Colors.white_block} {Colors.default}\n")
    print(f"{Colors.white}Go forth, Hero, and become the MasterCode Breaker!{Colors.default}")
    print("Are you ready? ('Y' to play, 'N' to return to the menu)")

    # call the play_again function to direct player to game/menu depending on their choice
    play_again()


# play again function
def play_again():
    """
    Checks if the player has entered 'Y' or 'N' correctly, and directs them to game/menu.
    Outputs ValueError if user key press is invalid.
    """
    while True:
        try:
            play_again_choice = (input("Enter choice: \n")).upper().strip()
            if play_again_choice == "Y":
                clear_screen()
                run_game()
                break
            elif play_again_choice == "N":
                clear_screen()
                main_menu()
                break
            else:
                raise ValueError

        except ValueError:
            print("""
            Invalid key press.
            Press 'Y' to play the game, or 'N' to return to the main menu.
            """)


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
    # clear the screen and input the header image with introduction text below
    clear_screen()
    graphics.header_image()
    print("      Welcome, Hero, to the ultimate challenge!\n")
    print(" A secret code, unknown to anyone, prevents you from")
    print("    completing your heroic quest to save the world!\n")
    print(" You must solve the puzzle by breaking the secret code,")
    print("and doing so will earn you the title of MasterCode Breaker!\n")
    print("  Have you the courage to face up to the mighty task...?")
    graphics.divider_image()

    # randomly generate a new secret code, and set the attempt number to 0
    original_answer = generate_code()
    attempt_number = 0

    while attempt_number <= MAX_ATTEMPTS:
        player_guess = player_guess_input(attempt_number)
        # creates a modified list variable that can be amended without changing original secret code
        modified_answer = list(original_answer)

        # displays the player's guess as coloured blocks for visual clarity
        print(f"{display_player_guess(player_guess)}\n")

        # checks the player's guess against the modified list and outputs appropriately
        position, color = check_result(player_guess, modified_answer)
        if position == CODE_LENGTH:
            graphics.you_win()
            print(f"The secret code is: {display_player_guess(original_answer)}\n")
            print("You cracked the code like a true Hero, and became the MasterCode Breaker!")
            print(f"You defeated this challenge in {Colors.white}{attempt_number + 1}{Colors.default} attempt(s).\n")
            print("Would you like to try to become the MasterCode Breaker once more? (Y/N)")
            play_again()
            break

        elif attempt_number == MAX_ATTEMPTS and position != CODE_LENGTH:
            graphics.game_over()
            print(f"The secret code was: {display_player_guess(original_answer)}\n")
            print("You were defeated this time, but do not despair! Try again? (Y/N)")
            play_again()
            break

        else:
            attempt_number += 1
            print(f"Correct color and position: {position}")
            print(f"Correct color, but incorrect position: {color}")
            print(f"You have {Colors.white}{MAX_ATTEMPTS - attempt_number + 1}{Colors.default} attempt(s) remaining.\n")


# function for player input
def player_guess_input(attempt):
    """
    Asks the player to enter their guess, and validates the input.
    Outputs ValueError if input is invalid.
    """
    while True:
        try:
            guess = input("Enter your prediction: \n").upper()
            print("")
            guess_list = [g for g in guess]

            if len(guess_list) != CODE_LENGTH:
                raise ValueError(f"Invalid - please enter {CODE_LENGTH} valid characters.\n" +
                                 f"Please choose only from the following characters, with no commas or spaces:\n" +
                                 f"{Colors.red}R  {Colors.green}G  {Colors.blue}B  {Colors.yellow}Y  {Colors.purple}P  {Colors.white}W{Colors.default}\n")
                continue

            for character in guess_list:
                if character not in COLOR_CHOICES:
                    raise ValueError(f"Error: You have entered one or more invalid characters.\n" +
                                     f"Please choose only from the following characters, with no commas or spaces:\n" +
                                     f"{Colors.red}R  {Colors.green}G  {Colors.blue}B  {Colors.yellow}Y  {Colors.purple}P  {Colors.white}W{Colors.default}\n")
            break

        except ValueError as e:
            print(e)

    return guess_list


# display the player's guess in color
def display_player_guess(guess):
    """
    Displays the player's guess as a string of color blocks
    """
    output = ""
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
            output += f" {Colors.purple_block} {Colors.default}"
        elif item == "W":
            output += f" {Colors.white_block} {Colors.default}"
    return output


# function to compare user input with code
def check_result(guess, answer):
    """
    Checks the player's guess against the secret code.
    Outputs number in correct position and number correct but in wrong position.
    Removes any matches from the code list to prevent double counting.
    Feeds correct position/correct but in wrong position to run_game.
    """
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


# clear screen function
def clear_screen():
    """
    Clears the terminal screen/window
    """
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


# main function
main_menu()
