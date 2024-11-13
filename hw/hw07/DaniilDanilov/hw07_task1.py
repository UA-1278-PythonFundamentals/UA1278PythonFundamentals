# Task1. Write a function that returns the largest number of two numbers 
# (use DocStrings documentation strings in the function).

a = float(input("Write first number: "))
b = float(input("Write second number: "))

print ("Your numbers:", a, "and", b)

def largest_number (a, b):
    """⬇️ \t ⬇️ \t ⬇️\tThis function show the largest number\t⬇️ \t⬇️ \t⬇️ """
    print (largest_number.__doc__)
    if a < b:
        print("Larger number is", b)
        return b
    elif a > b:
        print("Larger number is", a)
        return a

largest_number(a, b)