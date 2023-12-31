# **MasterCode - Testing**

## **Table of Contents (Testing):**

1. [**Testing Throughout Development**](#testing-throughout-development)
   - [**Manual Testing Methods**](#manual-testing-methods)
     - [**Print Statements**](#print-statements)
     - [**python3 run.py**](#python3-runpy)
     - [**python3**](#python3)
     - [**Python Tutor**](#python-tutor)
     - [**Input Testing**](#input-testing)
1. [**Notable Bugs and Fixes**](#notable-bugs-and-fixes)
   - [**_Print Statement Sabotage_**](#print-statement-sabotage)
   - [**_Player Guess Output Predicament_**](#player-guess-output-predicament)
   - [**_Python's Bane: Backslashes in ASCII Art_**](#pythons-bane-backslashes-in-ascii-art)
   - [**_"None" Shall Follow_**](#none-shall-follow)
   - [**_The Curse of the Infinite Loop_**](#the-curse-of-the-infinite-loop)
   - [**_Not Even A Hero Can Escape_**](#not-even-a-hero-can-escape)
1. [**Post Development Testing**](#post-development-testing)
   - [**Validation**](#validation)
   - [**Unresolved Bugs**](#unresolved-bugs)
   - [**Testing Final Deployed Version**](#testing-final-deployed-versiontesting)

## **Testing Throughout Development**

### **Manual Testing Methods**

During the development of this project, I used a number of methods to manually test my code as I went along.

#### Print Statements

The use of print statements to test my code as I went along was absolutely critical for the development of this project. Not only because they are useful to add into functions to test whether individual parts are working as intended, but also - crucially - using them meant that I was able to print the randomly generated secret code to the console at the start of each game. Being able to see the code that had been generated meant that I was able to test whether the functions that handled the player input, the comparison between the player guess and the code, and the output to the player were not only working as intended but also raising the correct errors at the correct times.

#### python3 run.py

I used the 'python3 run.py' terminal command countless times during the development of this game, so that I could see the output in the desired terminal setting. It is how I tested the functionality of every single feature, and the interactions between each of them.

#### python3

Occasionally, I would use the 'python3' terminal command in order to test code that I wasn't 100% certain about, that I worried might interfere with the existing functionality of the game if I tried to test it in my code directly. This was extremely useful to do on several occasions, not least because it helped me realise where I might have either misunderstood how something works, or used the wrong terms/syntax.

#### Python Tutor

There were a few occasions during development (which I elaborate on in the [Notable Bugs and Fixes](#notable-bugs-and-fixes) section) where ([Python Tutor](https://pythontutor.com/python-debugger.html#mode=edit)) was an absolutely invaluable tool, not just for testing the functionality of my code (and identifying bugs created by poorly placed 'print' and 'break' statements), but also for testing my understanding of how the functions were interacting with one another. This helped develop my knowledge by solidifying my understanding of the arguments needed for certain functions, where those arguments needed to come from and how, and in general it helped me test the overall game logic to make sure I was doing things in the right order.

Python Tutor was also especially helpful in testing functions that required input to work, but I had not yet defined the functions that would take in the required input. By running them through Python Tutor, I could at least be reassured that my logic was sound, and that I could move onto the next step which was creating the functions to provide the input arguments needed.

#### **Input Testing**

Input testing was crucial during development, as I needed to make absolutely certain that wherever player input is required, there could be no circumstances under which the game could crash or cause bugs if incorrect input was entered.

As such, I used the 'python3 run.py' terminal command almost non-stop whilst testing that my ValueErrors were being raised correctly. Essentially, in order to successfully do the input testing, I needed to go out of my way to enter everything wrong on purpose, in as many different ways as I could think of, to make sure that the correct errors were being raised and that the inputs were not being accepted if they were invalid.

At one stage during input testing, I did attempt to implement the 'getpass' input function, as I had hoped to take the player's input and then convert it to the coloured blocks output, without printing their guess to the terminal. However, after importing 'getpass' and testing it out, I found that it was generally unsuitable for what I had in mind and decided against using it.

## **Notable Bugs and Fixes**

Encountering bugs when developing a program in a language such as Python is certainly to be expected, and I encountered a great many of them during the development of this game. Most of the time, these bugs were due to indentation errors, spelling errors, trying to import functions from other files (such as graphics.py) incorrectly, giving functions the wrong arguments (or none at all, when there should have been one), etc. I considered these as to be expected during the development process, so did not make note of them. However, below I have listed some bugs that I did keep record of, because I felt that they all served as noteworthy learning opportunities.

_(I have given them thematically appropriate names to these bugs that tie in with the theme of the game, just for a little fun!)_

### Print Statement Sabotage

The first major bug I encountered during testing was actually the result of testing itself, but it took me quite a while to figure it out. As I've mentioned above, one of the most crucial things I needed to do throughout the development of this game is actually see the randomly generated code so that I could test whether the game was functioning properly. I did this initially for the generate_code() function, but didn't properly begin to utilise this until the majority of the main functions were created. I quickly found quite a significant bug:

![Screenshot of correct code entered, but result showing as 0 in correct position, only 2 correct in wrong position](docs/images/print-statement-sabotage-1.png)

![Screenshot of 3 out of 4 characters correct, but result showing 0 correct position, and 0 correct in wrong position](docs/images/print-statement-sabotage-2.png)

The reason it took me so long to identify where this bug was coming from was because I was approaching it from the wrong angle entirely. I was convinced that the issue was in the functions themselves, and so I was taking the functions - _without_ the print statement included - and running them through Python Tutor where I found no issues. Eventually I ran everything through Python Tutor together (including the infamous print statement), where I finally realised that what I had done was this:

![Screenshot showing that I had incorrectly called the function INSIDE the print statement](docs/images/print-statement-sabotage-3.png)

By calling the function inside the print statement, I was asking the program to generate a secret code, then generate _another_ secret code and print _that_ code to the terminal. Upon identifying this, I realised that I needed to define the variable 'original_answer' and call the generate_code() function as its value (this became a crucial addition to the code), and add 'print(original_answer)' below this variable in order for the correct code to print to the terminal and allow for me to test the game effectively.

![Screenshot of the solution to this bug](docs/images/print-statement-sabotage-4.png)

### Player Guess Output Predicament

Initially, I had not included any kind of visual feedback of the player's guess - the only thing that was output after their guess was the text explaining how many correct answers they had (as shown above in the previous bug's screenshots). Eventually I realised that having the colours displayed to the user as well would vastly improve the overall user experience, and set out to implement it. However, when testing, I came across the following bug:

![Screenshot of player input as "RRRR", but output displays only 1 red block](docs/images/player-guess-output-predicament-1.png)

_Technically_, this output is correct, because the player input is only the colour red. However, I wanted the output to show each individual entry, even if they were all the same colour.

I soon realised that I had incorrectly included the 'return output' statement _inside_ the if/elif statement within the display_player_guess() function's for loop.

![Screenshot of incorrectly places return statement](docs/images/player-guess-output-predicament-2.png)

I fixed this by correcting the indentation and putting the 'return output' statement at the bottom of the for loop, outside of the if/elif statements.

![Screenshot of correctly placed return statement](docs/images/player-guess-output-predicament-3.png)

Although this bug comes under the category of 'indentation bugs', I considered this one to be significant as it made me really consider what I was asking the code to do by having put the statement in the wrong place.

### Python's Bane: Backslashes in ASCII Art

When I first began experimenting with ASCII text, I experienced the following bug:

![Screenshot of broken ASCII art](docs/images/pythons-bane-backslash.png)

A quick Google search led me immediately to the answer for this, which is that Python ignores backslashes as it's an escape character. This is a common feature in most, if not all, programming languages, but I had not considered this when including the graphics.

To fix this, as will be evident in the functions within graphics.py, I needed to add many, many additional backslashes so that the output matched what was intended. Unfortunately, as a result, the code itself looks quite messy at times. I will be interested to learn whether there are neater ways of fixing this issue for future projects.

### "None" Shall Follow

Once I had fixed the backslash issue with my graphics, I noticed a new problem had arisen, which is that immediately after every single one, the text "None" was appearing before the text that followed the graphic.

![Screenshot of main logo, followed by "None"](docs/images/none-shall-follow-1.png)

![Screenshot of banner image, followed by "None"](docs/images/none-shall-follow-2.png)

Despite my previous issue with incorrectly attempting to call functions within print statements, I realised that I had made the same mistake again, this time with the graphics functions. Each of the functions in graphics.py includes a print statement that prints the graphic to the terminal. However, instead of calling the functions from the graphics.py file by name, I was wrapping them in the print statement, meaning that I was creating a duplicate print request that was returning the value "None", as the duplicate print request was returning empty. I fixed this by removing the print statement and just calling the functions as normal.

### The Curse of the Infinite Loop

The play_again() function was created much later in development than most other functions, as I wanted to make sure the core functions were working correctly before introducing it. After doing so, two major bugs appeared in my code (this bug, and the following bug listed).

This first bug was creating an infinite gameplay loop that was impossible to break out of unless the terminal was forced to close. When the game ended, and the play_again() function was called, it didn't matter whether the player entered 'Y', 'N', or any other character - the same thing happened each time:

![Screenshot of infinite loop after answering 'Y' to play_again()](docs/images/infinite-loop-1.png)

![Screenshot of infinite loop after answering 'N' to play_again()](docs/images/infinite-loop-2.png)

![Screenshot of infinite loop after answering 'f' to play_again()](docs/images/infinite-loop-3.png)

The culprit for this issue was a series of wrongly placed, and ultimately unnecessary, 'break' statements within the function itself that were interfering with its functionality. They were also causing the game to skip some parts of the run_game() function (such as clearing the screen, displaying the banner image, etc). The bug was fixed by removing these break statements, and more care was taken to investigate whether any similar issues had arisen from issues like this.

### Not Even A Hero Can Escape

My investigation led me almost immediately to a different kind of infinite loop that was being caused by a similar, though technically opposite issue:

![Screenshot of infinite loop that made exiting the game impossible](docs/images/no-escape.png)

In this instance, the problem was that pressing '4' to exit the game was creating a similar infinite gameplay loop to the one seen in the previous bug. The reason I was able to identify where the issue was coming from so quickly was that this bug only occurred AFTER playing the main game/visiting the instructions or Triforce pages once. If you ran the program and pressed '4' straight away, the program would close as expected. This meant the issue had to be with the play_game() function.

Whereas the previous issue had been that I had too many wrongly placed break statements, in this case the problem was that I _hadn't_ included break statements after calling the play_game() function in the main menu options. This was leading to two separate instances of the game trying to run side-by-side, resulting in the bug pictured above. Adding break statements under each option fixed this bug.

## **Post Development Testing**

### **Validation**

Once I was happy with my code overall, I entered the code from each of my files into the [CI Python Linter](https://pep8ci.herokuapp.com/) to validate it. Initially, there were a few issues such as trailing whitespace, or the accidental inclusion of white space on what should have been a blank line. This was very quickly tidied up. All significant issues such as this were removed, though if you run my 'run.py' and 'graphics.py' files through the linter you will see that many issues remain, which I have detailed in the [Unresolved Bugs](#unresolved-bugs) section below.

### **Unresolved Bugs**

At the time of submission, there are no known bugs within the game's code, save for the following issue regarding the [CI Python Linter](https://pep8ci.herokuapp.com/).

When running my 'run.py' and 'graphics.py' files through the linter, you will see that the 'run.py' file returns twenty-two "E501 line too long" errors, and my 'graphics.py' file returns ten "E501 line too long" errors as well as thirty-one "W605 invalid escape sequence" errors.

Looking at the code in these files, and also by looking at some of the information in the README and TESTING files, it is easy to see where these errors are coming from. In the case of the "E501 line too long" errors, they are all due either to strings that begin several indentations in, or due to changing colours throughout the strings. When printed into the terminal, I have taken significant care to ensure that not a single line of text is longer than 79 characters when displayed.

It is also evident that the "W605 invalid escape sequence" errors are due to the issues I have mentioned above regarding the use of escape characters in the ASCII artwork.

I would absolutely welcome any and all feedback on how I might avoid these kinds of errors whilst also ensuring that the output displayed in the terminal is as visually appealing as intended!

### **Testing Final Deployed Version**

As I conducted most of my testing through the terminal in Gitpod's VSCode cloud IDE, once I had deployed to Heroku I needed to ensure that my final submitted project was to the highest standard, and optimised specifically for the Heroku virtual platform.

As a result, after deployment, there was a large increase in the frequency of my commits and pushes to GitHub, to update my code as I went. By doing this, I was able to make minor tweaks such as reducing the size of some graphics, condensing certain text strings, rearranging the layouts of certain outputs, etc, and confirming that everything was outputting properly without interfering with any of the game's logic.

When I was confident that the game was optimised for the Heroku platform, I shared the link with some friends so that they could test it in their browsers. No issues were reported.

Thanks to [**Damon Kreft**](https://github.com/damon-kreft) I was also able to confirm that the game runs perfectly on local machines if this repository is cloned. Damon tested it in Ubuntu's default terminal, and in [Terminator (Linux's Terminal Emulator)](https://gnome-terminator.org/), and in each case the game ran as smoothly, and with no issues.

I am therefore confident that the testing that has been conducted throughout development and post-development has resulted in a stable, robust application that works consistently and without error.

Please click the following link to return to the [**README.md**](README.md) file.
