# Write a program that analyzes the entered number and, depending on the number, gives
# the day of the week that corresponds to this number (1 is Monday, 2 is Tuesday, etc.). Take
# into account cases of entering numbers from 8 and more, as well as cases of entering nonnumerical data.

def day_of_week():
    try:
        arr = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        user_number = int(input('Enter the number: '))
        if user_number > 7:
            raise ValueError('Only 7 days in week')
        elif user_number <= 0:
            raise ValueError('Write the num more then 0')
        elif True:
            for i, val in enumerate(arr):
                if i + 1 == user_number:
                    print(f'The day of week is {val}')

    except ValueError as e:
        print(f'Invalid input: {e}')


day_of_week()