import re


def password_validation(password):
    return re.search('^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@])[A-Za-z0-9$#@]{6,16}$', password)


user_input = input('Enter a password: ')
print(f'Your password is {"valid" if password_validation(user_input) else "invalid"}.')
