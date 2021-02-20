import random

def computer_guess(x):
    guess = 0
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else: 
            guess = low
        feedback = input(f"If {guess} is too high (H), too low (L) and correct (C) ").lower()
        if feedback == 'h':
            high = guess - 1
        if feedback == 'l':
            low = guess + 1
    print(f"Computer guessed {guess} number correctly!")

computer_guess(10)