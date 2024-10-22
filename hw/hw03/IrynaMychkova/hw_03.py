import this

###############################################################################
# 1. You need to write Python's philosophy in the string format
#   - find separately the number of occurrences of the words
#     "better", "never" and "is" in the given line
#   - you need to display all text in uppercase (all letters in uppercase)
#   - replace all occurrences of the symbol "¡" with "&"

# Decode the Zen of Python
zen_of_python = ''.join([this.d.get(c, c) for c in this.s]).lower()

print(f"Word occurances in the Zen of Python: \n\
    - 'better' - {zen_of_python.count('better')} times\n\
    - 'never' - {zen_of_python.count('never')} times\n\
    - 'is' - {zen_of_python.count('is')} times\n")

# Convert to uppercase and replace '¡' with '&'
modified_zen = zen_of_python.upper().replace('¡', '&')

print(f"Modified Zen of Python: \n{modified_zen}")

###############################################################################
# 2. A four-digit natural number is specified:
#   - find the product of the digits of this number
#   - write the number in reverse order
#   - in ascending order, you need to sort the numbers included in the given number

number = input("Enter a four-digit number: ")

# Ensure the input is a four-digit number
if len(number) == 4 and number.isdigit():
    # Find the product of the digits
    product_of_digits = 1
    for digit in number:
        product_of_digits *= int(digit)

    # Write the number in reverse order
    reversed_number = number[::-1]

    # Sort the numbers included in the given number in asc order
    sorted_digits = ''.join(sorted(number))

    # Print the results
    print(f"Product of the digits: {product_of_digits}")
    print(f"Number in reverse order: {reversed_number}")
    print(f"Digits sorted in ascending order: {sorted_digits}")
else:
    print(f"You entered not a 4 digit number: {number}")


###############################################################################
# 3. Interchange the values of two variables without using the third variable.
# Given two variables
a = False
b = 10
print(f"Given values: a = {a}, b = {b}")

# Interchange the values without using a third variable
a, b = b, a

# Print the results
print(f"After interchange: a = {a}, b = {b}")