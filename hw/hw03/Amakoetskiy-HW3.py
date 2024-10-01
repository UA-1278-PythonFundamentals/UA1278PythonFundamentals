###1
#T 1.1

t = "Beautiful is better than ugly.\
Explicit is better than implicit.\
Simple is better than complex.\
Complex is better than complicated.\
Flat is better than nested.\
Sparse is better than dense.\
Readability counts.\
Special cases aren't special enough to break the rules.\
Although practicality beats purity.\
Errors should never pass silently.\
Unless explicitly silenced.\
In the face of ambiguity, refuse the temptation to guess.\
There should be one-- and preferably only one --obvious way to do it.\
Although that way may not be obvious at first unless you're Dutch.\
Now is better than never.\
Although never is often better than *right* now.\
If the implementation is hard to explain, it's a bad idea.\
If the implementation is easy to explain, it may be a good idea.\
Namespaces are one honking great idea -- let's do more of those!"

print("Separately the number of occurrences of the word \"better\" is:",t.count("better"))
print("Separately the number of occurrences of the word \"never\" is:",t.count("never"))
print("Separately the number of occurrences of the word \"is\" is:",t.count("is"))

# Task 1.2

print(t.upper())
 
 #Task 1.3



print(t.replace("i", "&"))


####2



number = 2124   
print ("Number:", number)

#2.1

digits = [int(digit) for digit in str(number)]

product = 1
for digit in digits:
 product *= digit
print("Product of the digits:", product)

# 2.2

reverse = int(str(number)[::-1])
print("Reversed number:", reverse)

# 2.3

sort = ''.join(sorted(str(number)))
print("Digits in ascending order:", sort)

###3
a= 20
b = 24
print("A =", a, "B =", b)
a , b = b , a
print("Now:\n","A =", a, "B =", b)
#
#
