def str_to_number(number1, number2):
    if str.isdigit(number1) == True:
        number1 = int(number1)
    else:
        number1 = float(number1)
        
    if str.isdigit(number2) == True:
        number2 = int(number2)
    else:
        number2 = float(number2)
        
    return (number1, number2)

def large_number(number1_to_number, number2_to_number):
    """Write a function that returns the largest number of two numbers."""
    if number1_to_number > number2_to_number:
        return number1_to_number
    else:
        return number2_to_number


number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")
number1_to_number = str_to_number(number1, number2)[0]
number2_to_number = str_to_number(number1, number2)[1]
print(f"The largest number of two numbers: {large_number(number1_to_number, number2_to_number)}")
