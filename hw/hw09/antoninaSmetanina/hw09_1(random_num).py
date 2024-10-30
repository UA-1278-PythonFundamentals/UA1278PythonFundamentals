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

from random import randint


def random_number(number_random):
    low_number = 1
    high_number = 100
    number_guesses = 0

    print("Try to guess the number!")

    while number_guesses < 10:
        number_user = int(input(f'Enter a number between {low_number} and {high_number}: '))
        number_guesses += 1

        if number_user < number_random:
            print('Higher!')
            low_number = number_user + 1
        elif number_user > number_random:
            print('Lower!')
            high_number = number_user - 1
        else:
            print(f'You guessed the number in {number_guesses} tries!')
            return f'Congratulations! You guessed the number {number_random}'

    print(f'Sorry, you\'ve used all 10 attempts. The number was {number_random}.')
    return f'Total guesses = {number_guesses}'


number_random = randint(1, 100)
print(random_number(number_random))
