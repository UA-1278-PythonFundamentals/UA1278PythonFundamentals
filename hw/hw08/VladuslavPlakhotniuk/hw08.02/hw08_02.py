import re

def validate_password(password):
    checks = [
        (6 <= len(password) <= 16),
        (re.search(r'[a-z]', password)),
        (re.search(r'[A-Z]', password)),
        (re.search(r'[0-9]', password)),
        (re.search(r'[$#@]', password))
    ]
    
    return all(checks)

password_input = input("Enter your password: ")
print("Password is valid." if validate_password(password_input) else "Password is invalid.")
