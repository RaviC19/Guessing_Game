import random

random_number = random.randint(1, 10)  # numbers 1 - 10

# handle user guesses
#   if they guess correct, tell them they won
#     otherwise tell them if they are too high or too low

# BONUS - let player play again if they want!

guess = int(input("Guess a number between 1 and 10 "))

while guess != random_number:
    if guess < random_number:
        print(f"Your guess of {guess} is too low! Think higher")
        guess = int(input("Guess a number between 1 and 10 "))
    elif guess > random_number:
        print(f"Your guess of {guess} is too high! Think smaller")
        guess = int(input("Guess a number between 1 and 10 "))
print(f"Your guess of {guess} was correct, you won the game!")

repeat = input("Do you want to play again? (y/n)")
