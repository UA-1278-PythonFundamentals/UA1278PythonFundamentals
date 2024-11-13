a = int(input("Enter your age: "))

if a < 0:
    raise ValueError("You age can not be negative")
elif a % 2 == 0:
    print("Your age is even")
elif a % 2 == 1:
    print("Your age is odd")

