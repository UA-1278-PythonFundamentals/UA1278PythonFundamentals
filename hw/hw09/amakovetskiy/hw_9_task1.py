# Task 1


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