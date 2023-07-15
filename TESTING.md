# **MasterCode - Testing**

## **Table of Contents (Testing):**

1. [**Testing Throughout Development**]
   - [**Manual Testing Methods**](#manual-testing-methods)
   - [**Input Testing**](#input-testing)
   - [**Game Logic Testing**](#game-logic-testing)
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

During the development of this project, I used a number of methods to manually test my code as I went.

(print statements)

(python3)

(python3 run.py)

([Python Tutor](https://pythontutor.com/python-debugger.html#mode=edit))

([Replit](https://replit.com/~))

### **Input Testing**

(python3 run.py)

(ValueErrors - entering everything wrong on purpose)

(attempt at using getpass)

### **Game Logic Testing**

(print statements)

(where logic relied on input, but input not possible due to bugs/not being defined yet: [Python Tutor](https://pythontutor.com/python-debugger.html#mode=edit))

## **Notable Bugs and Fixes**

Encountering bugs when developing a program in a language such as Python is certainly to be expected, and I encountered a great many of them during the development of this game. Most of the time, these bugs were due to indentation errors, spelling errors, trying to import functions from other files (such as graphics.py) incorrectly, giving functions the wrong arguments (or none at all, when there should have been one), etc. I considered these as to be expected during the development process, so did not make note of them. However, below I have listed some bugs that I did keep record of, because I felt that they all served as noteworthy learning opportunities (I have given them quirky names in line with the theme of the game, for a little fun).

### Print Statement Sabotage

(incorrectly placed print statement)

### Player Guess Output Predicament

(incorrectly placed return statement)

### Python's Bane: Backslashes in ASCII Art

(graphics displaying weirdly due to backslashes)

### "None" Shall Follow

('None' after graphics due to wrapping functions in print())

### The Curse of the Infinite Loop

(play_again() bug where any input led to 'Enter Your Prediction:')

### Not Even A Hero Can Escape

(similar bug with exit game where break was not added)

## **Post Development Testing**

### **Validation**

(code linter)

### **Unresolved Bugs**

(linter issues due to line length, unavoidable due to most of it being code rather than output)

### **Testing Final Deployed Version**

(mention increased frequency in commits & pushes)

(asking friends to test on local machines & deployed version)

Please click the following link to return to the [**README.md**](README.md) file.
