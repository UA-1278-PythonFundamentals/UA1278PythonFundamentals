# Write a Python program to check the validity of a password (input from users).

import re

def validity_of_password(password='Forester990$'):
   
    password = input('Enter the password: ')
    pattern = r'(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[$#@]).{6,16}'
    if re.fullmatch(pattern, password):
        return 'Success'
    else:
        return 'Password not valid'


print(validity_of_password())


