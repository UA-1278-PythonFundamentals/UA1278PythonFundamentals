import re

def password_validation(password: str):
    """
    Validates a password using regular expressions.

    Validation criteria:
        - At least 1 letter between [a-z]
        - At least 1 letter between [A-Z]
        - At least 1 number between [0-9]
        - At least 1 character from [$#@]
        - Minimum length of 6 characters
        - Maximum length of 16 characters

    :param password: str: The password to validate
    :return: bool: True if the password is valid, False otherwise
    """

    pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@])[A-Za-z\d$#@]{6,16}$')

    return None != pattern.search(password)


password = input("Enter Your password please: ")

print(f"Password is {'' if password_validation(password) else 'in'}valid")
