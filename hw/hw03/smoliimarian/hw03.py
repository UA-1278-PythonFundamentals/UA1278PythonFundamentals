# TASK 1
import this

zen = "".join([this.d.get(c, c) for c in this.s])

count_better = zen.count("better")
count_never = zen.count("never")
count_is = zen.count("is")

print(f"better: {count_better}, never: {count_never}, is: {count_is}")

zen_upper = zen.upper()
print(zen_upper)

zen_replaced = zen.replace("i", "&")
print(zen_replaced)

# TASK 2

number = 9835
product = 1

for digit in str(number):
    product *= int(digit)

print(f"Product: {product}")

reverse_number = int(str(number)[::-1])

print(f"Reverse: {reverse_number}")

asc_order = int("".join(sorted(str(number))))

print(f"Ascending order: {asc_order}")

# TASK 3

a = 1
b = 2

a, b = b, a

print(f"a: {a}, b: {b}")
