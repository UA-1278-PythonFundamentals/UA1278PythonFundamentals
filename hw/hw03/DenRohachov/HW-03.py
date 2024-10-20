### HW 03.1 Practical tasks / [GitHub]

### Task 1 
### You need to write Python's philosophy in the string format:

### Task 1 | Part 1
### - find separately the number of occurrences of the words
### "better", "never" and "is" in the given line

# the first step is import Zen of Python and convert to string
# https://stackoverflow.com/questions/23794344/how-can-i-return-pythons-import-this-as-a-string

import this
python = "".join([this.d.get(c, c) for c in this.s])
print()

# the second step is find the number
print("03.1 Practical tasks / [GitHub]\nTask 1 | Part 1")
print()
print("find separately the number of occurrences of the words\n\"better\", \"never\" and \"is\" in the given linen\n")
print("better = ", python.count("better"))
print("never = ", python.count("never"))
print("is = ", python.count("is"))
print()


### Task 1 | Part 2
### You need to display all text in uppercase (all letters in uppercase)

print("Task 1 | Part 2")
print("You need to display all text in uppercase (all letters in uppercase)\n")
print(python.upper())
print()

### Task 1 | Part 3
### Replace all occurences of the symbol "i" with "%"
### PS only low "i" in Zen of Python

print("Task 1 | Part 3")
print("Replace all occurences of the symbol \"i\" with \"%\"\n")
print(python.replace("i","%"))
print()


### Task 2
### A four-digit natural number is specified

print("Task 2")
number = "1517"
print("A four-digit natural number is specified:", number)

### - find the product of the digits of this number
a = int(number[0])
b = int(number[1])
c = int(number[2])
d = int(number[3])
product = a * b * c * d
print("- find the product of the digits of this number:", product)

### - write the number in reverse order
reverse_number = number[::-1]
print("- write the number in reverse order:", reverse_number)

### - in ascending order, you need to sort the number included in the given number
list = [a,b,c,d]
list.sort()
a = str(list[0])
b = str(list[1])
c = str(list[2])
d = str(list[3])
print("- in ascending order:", a + b + c + d)
print()



### Task 3
### Interchange the value of two variables without using the third variable
print("Task 3")
print("Interchange the value of two variables without using the third variable:")
print("function: a, b = b, a")
a = 10
b = 20
print("before:", a, b)
a, b = b, a
print("after:", a, b)

