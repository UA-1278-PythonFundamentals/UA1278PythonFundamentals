#01task
with open('hw/hw02/Zen.txt', 'r') as file:
    text = file.read()

better_count = text.count("better")
never_count = text.count("never")
is_count = text.count("is")

up_text = text.upper()
mode_text = up_text.replace("I", "&")

print(f"Слово 'better' зустрічається: {better_count}")
print(f"Слово 'never' зустрічається: {never_count}")
print(f"Слово 'is' зустрічається: {is_count}")

print("\nТекст зі змінами 'I' на '&':\n")
print(mode_text)

#02task
number = 1488
myNumber = str(number)
product = 1
for digit in myNumber:
        digit_int = int(digit)
        product = product * digit_int

reverse = int(str(number)[::-1])

sort = ''
for digit in sorted(str(number)):
    sort += digit

print(f"Добуток: {product}")
print(f"У зворотному: {reverse}")
print(f"У зростаючому: {sort}")

#task03
a = 5
b = 10
a = a + b 
b = a + b 
print(a, b)

