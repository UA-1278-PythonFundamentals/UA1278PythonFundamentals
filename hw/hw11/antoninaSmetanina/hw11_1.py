# Write a program that prompts the user to enter their age, and then displays a
# message stating whether the age is even or odd. The program must provide the ability
# to enter a negative number, and in this case generate an exception. The master code
# should call a function that processes the information entered.

def age_user():
    try:
        age = int(input('Enter the age: '))
        if age < 0:
            raise ValueError('Age cannot be negative')
        elif age % 2 == 0:
            print('Your age is even')
        else:
            print('Your age is odd')

    except ValueError as e:
        print(f'Invalid input: {e}')


age_user()
