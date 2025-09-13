
import random

lowest_num = 1
highest_num = 100
number = random.randint(lowest_num,highest_num)
guesses = 0
is_running = True

while is_running:
    guess = (input(f"Guess a number between {lowest_num} and {highest_num}: "))

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

    if guess == number:
        print("CORRECT..!")
        print(f"You guessed it right in {guesses} guesses..!")
        is_running = False
    elif guess < number:
        print("A little bit higher")

    elif guess > number:
        print("A little bit lower")
    elif guess == number - 1 or guess == number + 1:
        print("too close")
    else:
        print("Invalid guess")
        print(f"please select a number b/w {lowest_num} and {highest_num}")


