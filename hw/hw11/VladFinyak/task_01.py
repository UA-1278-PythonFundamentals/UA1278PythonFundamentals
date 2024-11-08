try:
    age = int(input("Enter age: "))
    if age <= 0:
        raise ValueError("Age must be a positive number greater than zero.")
    if age % 2 == 0:
        print("Age is even")
    else:
        print("Age is odd")
except ValueError as a:
    print("Invalid input:", a)


