import random

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100. ")

# The answer from 1 to 100
computer_answer = random.randint(1, 100)
print(computer_answer)

# Too high or too low against the user's guess

def check_answer(user_guess, the_actual):
    if user_guess > the_actual:
        print("Too high!")
    elif user_guess < the_actual:
        print("Too low!")
    else:
        print("You got it!")

# Easy should have 10 attempts, Hard should be 5 attempts
def choose_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if level == 'easy':
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS
    
turns = choose_difficulty()


# User's guess, will only take int
guess = int(input("Make a guess: "))