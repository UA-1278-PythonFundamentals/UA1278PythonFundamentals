import re

pattern = "(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$])"

while True:
    passw = input("Enter password: ")

    if 6 <= len(passw) <= 16:
        res = re.search(pattern, passw)

        if res:
            print("Password is valid")
            break
        else:
            print("Input correct password (format doesn't match)")
    else:
        print("Password length must be between 6 and 16 characters")