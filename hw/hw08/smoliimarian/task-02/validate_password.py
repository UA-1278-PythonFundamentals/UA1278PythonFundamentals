import re


user_input = input("Enter password: ")


def validate_password(password):
    pattern = r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{6,16}$"

    if re.match(pattern, password):
        print("Password is valid")
    else:
        print("Password is invalid")


validate_password(user_input)
