# 1. Write a program that prompts the user to enter their age, 
# and then displays a message stating whether the age is even or odd. 
# The program must provide the ability to enter a negative number, 
# and in this case generate an exception. 
# The master code should call a function that processes the information entered.

age = input("Enter your age: ")

def check_age(age: str) -> str:
    try:
        age = int(age)
        if age < 0:
            raise ValueError("Age cannot be negative")
        return "Even" if age % 2 == 0 else "Odd"
    except ValueError as e:
        return str(e)
    

print(check_age(age))







