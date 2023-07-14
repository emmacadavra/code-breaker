"""
MasterCode - a code breaker game in the style of Mastermind.
"""

# imports
import random

# constants
COLOUR_CHOICES = ["R", "G", "Y", "B", "P", "W"]
CODE_LENGTH = 4
MAX_ATTEMPTS = 9


# menu/title screen
def main_menu():
    """
    Title screen/menu with options:
    Press 1 to play
    Press 2 for instructions
    press 3 to exit
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



# instructions on how to play
def instructions():
    """
    Instructions for the user on how to play the game
    """
    print("Instructions on how to play MasterCode:\n")
    print("A secret code of four colours will be randomly generated, choosing from the following colours:\n")
    print(f"{Colours.red}R  {Colours.green}G  {Colours.yellow}Y  {Colours.blue}B  {Colours.pink}P  {Colours.white}W{Colours.default}")
    print(f"{Colours.red_block} {Colours.default}  {Colours.green_block} {Colours.default}  {Colours.yellow_block} {Colours.default}  {Colours.blue_block} {Colours.default}  {Colours.pink_block} {Colours.default}  {Colours.white_block} {Colours.default}\n")
    print("Your heroic challenge is to find the solution in 10 attempts or fewer.")
    print("In doing so, you will become a MasterCode breaker!\n")
    print("A colour may appear more than once in the secret code, so don't forget to consider this!")
    print("The terminal will ONLY accept answers that are 4 characters long, with no commas or spaces.")
    print("Make sure you only use the following characters for their respective colours:\n")
    print(f"{Colours.red}R  {Colours.green}G  {Colours.yellow}Y  {Colours.blue}B  {Colours.pink}P  {Colours.white}W{Colours.default}\n")
    print(f"{Colours.white}Go forth, hero, and become the MasterCode breaker!{Colours.default}\n")


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
            print("You cracked the code like a true Hero!")
            print(f"You defeated this challenge in {Colours.white}{attempt_number + 1}{Colours.default} attempt(s).\n")
            break
        elif attempt_number == MAX_ATTEMPTS and position != CODE_LENGTH:
            print("Oh no! You weren't able to crack the code this time.")
            # print("Try again?")
            break
        else:
            attempt_number += 1
            print(f"Correct colour and position: {position}")
            print(f"Correct colour, but incorrect position: {colour}")
            print(f"You have {Colours.white}{MAX_ATTEMPTS - attempt_number + 1}{Colours.default} attempt(s) remaining.\n")


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
            print(f"Invalid - please enter {CODE_LENGTH} characters, with no commas or spaces.\n")
            continue

        for character in guess_list:
            if character not in COLOUR_CHOICES:
                print(f"Error: '{character}' is not a valid character.")
                print(f"Choose only from the following characters, with no commas or spaces:")
                print(f"{Colours.red}R  {Colours.green}G  {Colours.yellow}Y  {Colours.blue}B  {Colours.pink}P  {Colours.white}W{Colours.default}\n")
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


# Triforce lol
def triforce():
    tri = f"{Colours.yellow}▲"
    big_tri = []
    for i in range(1,21,2):
        big_tri.append(" "*int((19-i)/2) + tri*i + " "*int((19-i)/2))
    for t1 in big_tri:
        print(" "*10 + t1 + " "*10)
    for t2 in big_tri:
        print(t2 + " " + t2)

# main function 
main_menu()
