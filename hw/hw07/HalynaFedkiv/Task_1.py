def largest_number_1(num1, num2):
    '''The function will return the largest
     of two entered numbers.'''
    return max(num1, num2)

#or

def largest_number_2(num1, num2):
    '''The function will return the largest
         of two entered numbers.'''
    return num1 if num1 > num2 else num2


print(largest_number_1(10,2))
print(largest_number_2(45, 6))

