# Guessing Game

import random

rand_int = random.randrange(1, 11)

while True:
    while True:
        try:
            guess = int(input("Enter a guess: "))
            break
        except:
            print("You didn't enter a number")
    if rand_int == guess:
        print("You guessed {} correct".format(rand_int))
        break
    else:
        print("You guessed wrong, guess again")
