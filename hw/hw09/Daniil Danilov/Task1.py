# Task 1. Write a game script that randomly generates a number from a range of
# 1 to 100 and asks the user to guess that number in 10 tries.
# The program reads the numbers entered by the user and prompts the user
# whether the guessed number is greater or less than the number entered by the
# user. The game must continue until the user has used 10 attempts and guessed
# the number. If the user guessed the number, the program prints a
# congratulatory message, and if 10 attempts have been exhausted and the user
# did not have time to guess the number, then the corresponding message is
# displayed.
# (to perform the task, you need to import the random module,
# and from it the randint() function)

import random

random_number = random.randint(1, 100)

tries = 0

def user_tries(tries):
    tries += 1
    return tries

while tries <10:
    user_number = (int(input("Write your number: ")))
    tries = user_tries(tries)

    if user_number > random_number:
        print("Tries number:", tries)
        print("Your number is bigger!")
    elif user_number < random_number:
        print("Tries number:", tries)
        print("Your number is smaller!")
    elif user_number == random_number:
        print("Tries number:", tries)
        print("Super! You guessed the number! Congratulations!")
        break