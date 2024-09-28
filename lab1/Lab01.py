# 1. Name: 
#    Michael Johnson

# 2. Assignment Name: 
#    Lab 01: Python Review

# 3. Assignment Description:
#    This is a guessing game where the user can choose difficulty and then they are told whether their
#    guess is too high or too low based on their input. Once the user guesses the correct number. 
#    They are congratulated and told how many guesses they had, and what their guesses where.
#  
# 4. What was the hardest part? Be as specific as possible.
#    -a paragraph or two about how the assignment went for you-
#   It has been some time since I did python, so I had to get a quick refresh on some of the syntax.
#   But after that this assignment was pretty straight forward. I just had to set up a while loop to allow
#   the user to input as many guesses as needed, and then also make it so I only have one append for the guesses.
#   I mostly just had to refer to how to clear the terminal to keep the program looking clean, and less of an eye sore.
#   I had to make sure the input was being called as only a int, I kept getting errors every once in a while because it would
#   sometimes call the input as a string and then break, but overall this was a pretty simple program. Just a good
#   refresh of the python syntax. 


# 5. How long did it take for you to complete the assignment?
#    -total time in hours including reading the assignment and submitting the program-  

import random
import os
import time
# Game introduction.

# Prompt the user for how difficult the game will be. Ask for an integer.
print("This is the 'guess a number' game.")
value_max = input("Enter a number maximum to determine difficulty. Example (90) Number range 1-90: ")
value_max = int(value_max)
os.system('cls')

# Generate a random number between 1 and the chosen value.
value_random = random.randint(1, value_max)

# Give the user instructions as to what he or she will be doing.
print()
print(f"A random number between 1 and {value_max} has been generated. You will be told too high, or too low based on your guess.")
print()
print("Be smart with your guesses, and try to get the number in as minimal guesses as possible.")
print()
print("Good Luck!")
print()
# Initialize the sentinal and the array of guesses.
guesses = []
guess = -1
guess_count = 0
# Play the guessing game.

    # Prompt the user for a number.


while guess != value_random:
    # ask user for their guess
    guess = int(input("Enter your guess: "))
    guesses.append(guess)
    guess_count += 1
    #tell user too high if guess larger than number
    if guess > value_random:
        print("Too High! Think Lower!")
    # tell user to low if guess is smaller than number
    elif guess < value_random:
        print("Too Low! Think Higher!")
    # only other option is to guess number, so congradulate user when correct number given.
    else:
        os.system('cls')
        print("You got it!")
        time.sleep(2)
        os.system('cls')
        print(f"You guessed the number in {guess_count} tries!")
        print()
        print(f"your guesses where:\n{guesses}")
    

    # Store the number in an array so it can be displayed later.


    # Make a decision: was the guess too high, too low, or just right.

# Give the user a report: How many guesses and what the guesses where.


