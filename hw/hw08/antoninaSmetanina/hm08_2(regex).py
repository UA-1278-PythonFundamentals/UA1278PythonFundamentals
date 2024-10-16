# Write a Python program to check the validity of a password (input from users).

import re

def validity_of_password(password='qwE2$123'):
    '''At least 1 letter between [a-z] and 1 letter between [A-Z].
     At least 1 number between [0-9].
     At least 1 character from [$#@].
     Minimum length 6 characters.
     Maximum length 16 characters.'''
    password = input('Enter the password: ')
    pattern = r'(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[$#@]).{6,16}'
    if re.fullmatch(pattern, password):
        return 'Success'
    else:
        return 'Password not valid'


print(validity_of_password())


