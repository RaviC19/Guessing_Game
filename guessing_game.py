# handle user guesses
#   if they guess correct, tell them they won
#     otherwise tell them if they are too high or too low

# BONUS - let player play again if they want!

import random

while True:
    random_number = random.randint(1, 10)  # numbers 1 - 10
    guess = int(input("Guess a number between 1 and 10 "))

    while guess != random_number:
        if guess < random_number:
            print(f"Your guess of {guess} is too low! Think higher")
            guess = int(input("Guess a number between 1 and 10 "))
        elif guess > random_number:
            print(f"Your guess of {guess} is too high! Think smaller")
            guess = int(input("Guess a number between 1 and 10 "))
        else:
            print(f"Your guess of {guess} was correct, you won the game!")

    repeat = input("Do you want to play again? Enter yes or no ")
    if repeat == "yes":
        continue
    elif repeat == "no":
        print("Thanks for playing the guessing game")
        break
    else:
        print("You need to enter yes or no here")
