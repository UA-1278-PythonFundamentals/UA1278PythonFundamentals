
print("Task 1")
print("")

zen_of_python = """
Beautiful is better than ugly.
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
Namespaces are one honking great idea -- let's do more of those!
"""

better_count = zen_of_python.count("better")
never_count = zen_of_python.count("never")
is_count = zen_of_python.count("is")

zen_upper = zen_of_python.upper()

zen_replaced = zen_upper.replace("I", "&")

print("Occurrences of 'better':", better_count)
print("Occurrences of 'never':", never_count)
print("Occurrences of 'is':", is_count)
print("\nText in uppercase with 'I' replaced by '&':")
print(zen_replaced)

print("Task 2")
print("")

number = 4321

product_of_digits = 1
for digit in str(number):
    product_of_digits *= int(digit)

reverse_number = int(str(number)[::-1])

sorted_digits = "".join(sorted(str(number)))

print("Product of the digits:", product_of_digits)
print("Number in reverse order:", reverse_number)
print("Digits in ascending order:", sorted_digits)


print("")
print("Task 3")
print("")

a = 5
b = 10

a = a + b
b = a - b
a = a - b

print("After interchange:")
print("a =", a)
print("b =", b)