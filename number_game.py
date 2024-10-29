"""
Author: Stockton Nelson
Cowritter: {cowriter}
File: number_game.py
"""
import random;
magic_numebr = random.randint(1, 100)
guess_count = 0

while True:
    guess = int(input("Guess the number: "))
    if guess == magic_numebr:
        print(f"You got it!\n It took you {guess_count} guesses.")

        play_again = input("Do you want to play again? (y/n): ")
        if play_again == 'y':
            guess_count = 0
            magic_numebr = random.randint(1, 100)
            continue
        else:
            break
    elif guess > magic_numebr:
        print("Too high!")
        guess_count +=  1
    else:
        print("Too low!")
        guess_count +=  1
