def weekdays(num):
    days = {
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday',
        7: 'Sunday'
        }
    if num not in days:
        raise ValueError('Incorrect input. Please enter a number in range 1 to 7.')
    return days[num]


if __name__ == '__main__':
    try:
        n = int(input('Enter a number: '))
        print(weekdays(n))
    except ValueError as e:
        print(f'ValueError: {e}. Please check your input and try again.')

