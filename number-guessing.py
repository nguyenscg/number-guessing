import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100. ")

# The answer from 1 to 100
computer_answer = random.randint(1, 100)
print(computer_answer)

print("Choose a difficulty. Type 'easy' or 'hard':")

# Easy should have 10 attempts, Hard should be 5 attempts

# User's guess, will only take int
guess = int(input("Make a guess: "))

# Too high or too low against the user's guess

def check_answer(user_guess, the_actual):
    if user_guess > the_actual:
        print("Too high!")
    elif user_guess < the_actual:
        print("Too low!")
    else:
        print("You got it!")