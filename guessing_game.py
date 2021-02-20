import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Give me a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, try again. Your number is too low.")
        elif guess > random_number:
            print("Try again. Your number is too high.")
    print(f"You have got the correct number {random_number}!")

guess(10)