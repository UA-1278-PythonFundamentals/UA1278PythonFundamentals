#Task1. Write a function that returns the largest number 
# of two numbers (use DocStrings documentation strings in the function).

def largest_number(a: int, b: int) -> int:
    """
    This function returns the largest number of two numbers.
    :param a: int
    :param b: int
    :return: int
    """
    return a if a > b else b

# Print the largest number
print(largest_number(5, 10))

# You can get help by:
# Printing the docstring directly
# print(largest_number.__doc__)

# or by Using the help function to view the docstring
# help(largest_number)

# Or from the console call in the directory where the file is located:
# from task1 import largest_number
# help(largest_number)
