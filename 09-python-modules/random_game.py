import random
import sys

# My Solution


# def random_game():
#     number = random.randint(0, 10)

#     # code_guess = sys.argv[0]

#     # if code_guess:
#     #     guess = int(code_guess)
#     # else:
#     user_input = input("Guess a number between 0 and 10?\n")
#     guess = int(user_input)

#     if guess < number:
#         print(f"Guess too low, correct answer was {number}")
#     elif guess > number:
#         print(f"Guess too high, correct answer was {number}")
#     elif guess == number:
#         print(f"You are correct, correct answer was {number}")


# random_game()


# Provided Solution

answer = random.randint(int(sys.argv[1]), int(sys.argv[2]))


while True:
    try:
        guess = int(input(f"Guess a number {sys.argv[1]} ~ {sys.argv[2]}:\n"))
        if 0 < guess < 11:
            if guess == answer:
                print("Good Job, you guessed it!")
                break
        else:
            print(
                f"Number needs to be between {sys.argv[1]} and {sys.argv[2]}")
    except ValueError:
        print("Please enter a number")
        continue
