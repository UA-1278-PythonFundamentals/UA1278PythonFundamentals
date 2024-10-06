# Task1. In the range from 1 to 10 determine
# • even numbers that are divisible by 2,
# • odd numbers, which are divisible by 3,
# • numbers that are not divisible by 2 and 3.

even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print("Even numbers:", even_numbers)

odd_numbers = [x for x in range(1, 11) if x % 2 == 1 and x % 3 == 0]
print("Odd numbers divisible by 3:", odd_numbers)

not_divisible_by_2_or_3 = [x for x in range(1, 11) if x % 2 != 0 and x % 3 != 0]
print("Numbers not divisible by 2 or 3:", not_divisible_by_2_or_3)

# Task2. Write a script that checks the login that the user enters.
# If the login is "First", then greet the users. If the login is
# different, send an error message.
# (need to use loop while)

while True:
    login = input("Enter your login: ")
    if login == "First":
        print("Hello users")
        break
    else:
        print("Error. Please try again.")

# Or
login = input("Enter your login: ")

while login != "First":
    print("Error. Please try again.")
    login = input("Enter your login: ")
else:
    print("Hello users")
