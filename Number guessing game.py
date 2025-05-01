# Number guessing game
# This is a simple number guessing game where the user has to guess a randomly generated number between 1 and 100.
# The user can keep guessing until they either guess the correct number or choose to quit the game.
# The game provides feedback on whether the guess was too high or too low.
# Importing the random module to generate a random number

import random

target = random.randint(1, 100)

while True:
    userChoice = input("Guess the target or Quit(Q) :")
    if(userChoice == "Q"):
        break

    userChoice = int(userChoice)
    if(userChoice == target):
        print("Sucses : Correct Guess!!")
        break
    elif(userChoice < target):
        print("Your number was too small. Take a bigger guess..")
    else:
        print("Your number was too big. Take a smaller guess..")

print("----Game Over----")