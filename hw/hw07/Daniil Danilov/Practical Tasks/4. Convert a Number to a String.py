# We need a function that can transform a number (integer) into a string.

# What ways of achieving this do you know?

# Examples (input --> output):
# 123  --> "123"
# 999  --> "999"
# -100 --> "-100"

num = int(input("Your number: "))

def transformer(num):
    return str(num)

result = transformer(num)
print(type(result), "Result:", result)