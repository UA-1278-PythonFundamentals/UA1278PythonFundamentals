def check_age():
    try:
        age = int(input('Please enter your age: '))
        if age <= 0:
            raise ValueError('Your age cannot be a negative number!')
        print('Odd' if age % 2 else 'Even')
    except ValueError as e:
        print(f'ValueError: {e}. Use an integer number to describe your age.')


if __name__ == '__main__':
    check_age()

