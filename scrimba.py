# Guess the correct number in 3 guesses. If you don’t get it right after 3 guesses you lose the game.
# Give user input box: 1. To capture guesses,
# print(and input boxes) 1. If user wins 2. If user loses
# Tip:( remember you won’t see  print statements durng execution, so If you want to see prints during whle loop, then print to the input box

# Modification 1: number 1-100, tell user if guess is too high/low ,and let them have 5-10 guesses.
# Tip:( remember you won’t see  print statements during execution, so If you want to see prints during whle loop, print to the input box (This is specific to this platform)

import random

rand = random.randint(0, 100)
guess = None
i = 0

while (i < 5 and guess != rand):
    guess = int(input("Enter your guess "))        
    if (guess == rand):
        print("you guessed correctly")
        print("you win!")
        quit()
    elif (guess < rand):
        print("too low")
    else:
        print("too high")

    i += 1
print("please play again")
