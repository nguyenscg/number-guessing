import random 

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

# Global constants || won't ever be changing these variables
EASY_LEVEL = 10
HARD_LEVEL = 5

# Create a function that sets the difficulty
def set_difficulty():
    if difficulty == "easy":
        print(EASY_LEVEL)
        return EASY_LEVEL
    else:
        return HARD_LEVEL
set_difficulty()

# User chooses a level, easy = 10 attempts, hard = 5 attempts
# Prompt 'Make a guess' input
# Compare guess if its lower or higher
# If the guess is wrong, should -1 from attempts, allows user to guess again
# Keeps going until reaches 0 attempts, stops the loop right away when the guess is correct