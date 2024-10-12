# Task2. Write a script that checks the login that the user enters.
# If the login is "First", then greet the users. If the login is
# different, send an error message.
# (need to use loop while)

login = input('Enter the login: ')
while login == 'First':
    print('Login is success!')
    break
else:
    print('Error message. Repeat, pls!')