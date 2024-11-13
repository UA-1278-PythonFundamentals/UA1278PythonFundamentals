# Write a script that checks the login that the user enters. 
# If the login is "First", then greet the users. If the login is 
# different, send an error message. 


while True:
    login = input("Login: ")
    if login == "First":
        print("You are welcome!")
        break
    else:
        print("Fail. Try again!")
    continue