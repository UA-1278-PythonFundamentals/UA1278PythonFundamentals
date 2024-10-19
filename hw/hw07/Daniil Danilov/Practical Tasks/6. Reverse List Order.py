# In this kata you will create a function that takes in a list and returns a list with the reverse order.

# Examples (Input -> Output)
# * [1, 2, 3, 4]  -> [4, 3, 2, 1]
# * [9, 2, 0, 7]  -> [7, 0, 2, 9]

user_input = input("Your numbers: ")

numbers = []
for num in user_input.split():
    numbers.append(int(num))

def reverse_list(numbers):
    return numbers[::-1]

result = reverse_list(numbers)
print(result)
