# Task2.
#  Write a Python program to check the validity of a password (input from users).

#  Validation :
#  At least 1 letter between [a-z] and 1 letter between [A-Z].
#  At least 1 number between [0-9].
#  At least 1 character from [$#@].
#  Minimumlength 6 characters.
#  Maximumlength 16 characters.

import re


def password_checker(password):
    if len(password) < 6 or len(password) > 16:
        return "Bad password. Try again. (Minimumlength 6 characters, and maximumlength 16 characters.)"
    if not re.search("[A-Z]", password):
        return "Bad password. Try again. (You need add something A-Z)"
    if not re.search("[a-z]", password):
        return "Bad password. Try again. (You need add something a-z)"
    if not re.search("[0-9]", password):
        return "Bad password. Try again. (You need add something 0-9)"
    if not re.search("[$#@]", password):
        return "Bad password. Try again. (You need add something $#@)"
    return "Good job! You are welcome!! :3"

password = input("Check your password: ")
result = password_checker(password)
print(result)