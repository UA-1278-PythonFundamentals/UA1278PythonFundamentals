# Task1. Write a function that returns the largest number of two
# numbers
# (use DocStrings documentation strings in the function).

def lagrest_number(two_numbers):
    '''function that returns the largest number of two numbers'''
    return max(two_numbers)


two_numbers = 11, 22
print(lagrest_number(two_numbers))


def larg(numbers1, numbers2):
    '''function that returns the largest number of two numbers
    Parameters:
        numbers1 - first parameters
        numbers2 - second parameters
    '''
    return numbers1 if numbers1 > numbers2 else numbers2


print(larg(112, 13))
