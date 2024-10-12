login = input("Enter the login: ")

while True:
    if login == "First":
        print(f"Login is success! Hello, {login}!")
        break
    else:
        print("Error message. Repeat, pls!")
        login = input("Enter the login: ")
