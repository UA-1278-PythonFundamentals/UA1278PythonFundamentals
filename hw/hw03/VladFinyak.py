
# task1
import this
text = "The Zen of Python, by Tim Peters\
Beautiful is better than ugly.\
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


print ("Number of occurrence of better:", text.count("better"))
print ("Number of occurrence of never:", text.count("never"))
print ("Number of occurrence of is:", text.count("is"))               

up_text = text.upper()
print (up_text)

replace_text = up_text.replace("I", "&")
print (replace_text)


# task2
number = str(4637) 
product = 1
for digit in number:
        digit_int = int(digit)
        product = product * digit_int
print ("The product of the digits of this number:", product)


print ("The number in reverse order:",number[::-1])


sort = ""
for digit in sorted(number):
    sort += digit
print ("Ascending order:", sort)

# tast3
a = 10
b = 20 
print (a, b)
a, b = b, a 
print (a, b)