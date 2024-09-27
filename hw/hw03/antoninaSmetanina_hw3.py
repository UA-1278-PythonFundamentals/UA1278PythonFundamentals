# 1. You need to write Python's philosophy in the string format:
# - find separately the number of occurrences of the words
# "better", "never" and "is" in the given line

# Import python philosophy
# import this

# Saved the philosophy in variable
s = '''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''

# Find the count of word better
count_of_better = s.lower().count('better')
print(f'Count of word \'better\' in text is {count_of_better}')

# Find the count of word never
count_of_never = s.lower().count('never')
print(f'Count of word \'never\' in text is {count_of_never}')

# Find the count of word is
count_of_is = s.lower().count('is')
print(f'Count of word \'is\' in text is {count_of_is}')

# Count of each words in the text
count_of = {}
for i in s.split():
    if i in count_of:
        count_of[i] += 1
    else:
        count_of[i] = 1
print(count_of)

# Find each 'better' in text and its index
count = 0
for i, word in enumerate(s.split()):
    if word == 'better':
        count += 1
        print(f'Index: {i}, count {count}')


# - you need to display all text in uppercase (all letters in uppercase)
text_in_upper = s.upper()
print(text_in_upper)

# - replace all occurrences of the symbol “i” with “&”
change_letter = s.replace('i', '&')
print(change_letter)



# 2. A four-digit natural number is specified:
# - find the product of the digits of this number
# - write the number in reverse order
# - in ascending order, you need to sort the numbers included in the given number

num = 1243
num_str = str(num)
print(num_str)

# Easy approach to find the multiplication of digit
mult_num = int(num_str[0]) * int(num_str[1]) * int(num_str[2]) * int(num_str[3])
print(mult_num)

# Hard approach to find the multiplication of digit
# Converting str to list
list_num = list(num_str)
print(list_num)

# Converting each number of list to digit and place it in new list digits
digits = []
for digit in list_num:
    digits.append(int(digit))
print(digits)

# Multiplication every digit
mult = 1
for i in digits:
    mult *= i
print(mult)

# write the number in reverse order:
# approach 1: slicing
reverse_num = num_str[::-1]
print(reverse_num)

# approach 2: using method
list_num.reverse()
print(list_num)

# approach 3: using function
reverse_num2 = list(reversed(list_num))
print(reverse_num2)

# - in ascending order, you need to sort the numbers included in the given number
# approach 1:
list_num.sort()
print(list_num)

# approach 2:
sort_num = sorted(list_num)
print(sort_num)

# In descending order
list_num.sort(reverse=True)
print(list_num)



# 3. Interchange the values of two variables without using the third variable.

a = 3
b = 5
a, b = b, a
print(a, b)