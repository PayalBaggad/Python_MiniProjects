# A game where the user guesses a randomly chosen number.

import random

def number_guessing_game():
    number = random.randint(1, 100)
    attempts = 0

    print("Guess the number between 1 and 100!")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

number_guessing_game()


'''
Explanation:
1. The program selects a random number between 1 and 100.
2. The user guesses the number, and the program gives hints:
    A) "Too low" if the guess is smaller.
    B) "Too high" if the guess is larger.
3. When the user guesses correctly, it displays the number of attempts.
'''
