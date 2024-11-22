import this
text = """
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
better_count = text.lower().count("better")
never_count = text.lower().count("never")
is_count = text.lower().count("is")

uppercase_text = text.upper()
modified_text = uppercase_text.replace( "I", "&")
print(f"Кількість 'better': {better_count}")
print(f"Кількість 'never': {never_count}")
print(f"Кількість 'is': {is_count}")
print("\nТекст у верхньому регістрі: ")
print(uppercase_text)
print("\nТекст із заміною 'I' на '&': ")
print( modified_text )

number = 9876
digits = [ int(digit) for digit in str(number)]
product = 1
for digit in digits:
    product *= digit

reserved_number = int(str(number)[::-1])

sorted_digits = sorted(digits)

print("Добуток чисел:", product)
print("Число у зворотньому порядку:",reserved_number)
print("Цифри у порядку зростання:", sorted_digits)


a = 5
b = 10
print("До обміну:")
print("a=", a)
print("b =", b)
a,b = b, a
print("Після обміну:")
print("a =", a)
print("b =", b)