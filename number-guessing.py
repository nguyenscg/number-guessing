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
def compare(guessed, answer):
    if guessed == answer:
        print(f"You guessed correctly! it is {answer}")
    elif guessed > answer:
        print("Too high!")
    elif guessed < answer:
        print("Too low!")

def game():
    # Print Welcome and Message statements
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    # Set the difficulty based on the user's level selection, this will trigger the set_difficulty function and store the amount of attempts based on level
    turns = set_difficulty()

    # store random number that the computer is thinking of
    computer_number = random.randint(1, 100)

    # You have xx atempts remaining to guess the number
    print(f"You have {turns} attempts to guess the number.")
    # Prompt 'Make a guess'
    guess = int(input("Make a guess: "))
    # Compare the guess to computer's number, if it's wrong -1 but allow the user to guess again
    print(compare(guess, computer_number))

game()

# User chooses a level, easy = 10 attempts, hard = 5 attempts
# Prompt 'Make a guess' input
# Compare guess if its lower or higher
# If the guess is wrong, should -1 from attempts, allows user to guess again
# Keeps going until reaches 0 attempts, stops the loop right away when the guess is correct