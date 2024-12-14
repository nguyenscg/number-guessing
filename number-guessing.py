import random 

# Global constants || won't ever be changing these variables
EASY_LEVEL = 10
HARD_LEVEL = 5

# Create a function that sets the difficulty
def set_difficulty():
    difficulty = input("Choose a difficulty: Type 'easy' or 'hard' ")
    if difficulty == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL

# Create a function that compares the guess to the number that the computer is thinking, pass in number input
def compare(guessed):
    computer_number = random.randint(1, 100)
    if guessed == computer_number:
        print(f"You guessed correctly! it is {computer_number}")

def game():
    # Print Welcome and Message statements
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    # Set the difficulty based on the user's level selection, this will trigger the set_difficulty function and store the amount of attempts based on level
    level = set_difficulty()

game()

# User chooses a level, easy = 10 attempts, hard = 5 attempts
# Prompt 'Make a guess' input
# Compare guess if its lower or higher
# If the guess is wrong, should -1 from attempts, allows user to guess again
# Keeps going until reaches 0 attempts, stops the loop right away when the guess is correct