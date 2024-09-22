#Create a console-based number guessing game where users attempt to guess a randomly generated number between 1 and 100. Users can select their difficulty level, either "easy" with 10 attempts or "hard" with 5 attempts. The game should generate a random number and prompt the user for their guess, providing feedback on whether the guess is too low, too high, or correct, while tracking the number of remaining attempts. Additionally, the game should allow users to exit at any time and must include input validation to handle non-integer guesses gracefully.


import logo
import random

def game(number_of_attempts: int):
    """
    Takes input of number of attempts and produce the result
    """
    print(f"You have {number_of_attempts} attempts.")
    chosen_number = random.randint(1, 100)
    while number_of_attempts > 0:
        guess = int(input("\n\nMake a guess:    "))
        if chosen_number > guess:
            print("Too low.")
        elif chosen_number < guess:
            print("Too high.")
        elif chosen_number == guess:
            print("You got it!")
            return
        number_of_attempts -= 1
        if number_of_attempts == 0:
            print("You have run out of attempts, you lose!")
        print("Guess again.")
        print(f"You have {number_of_attempts} attempts remaining to guess the number.")
        

print(logo.logo)
print("Welcome To The Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard':    ").lower()
if difficulty == "easy":
    game(10)
elif difficulty == "hard":
    game(5)
        