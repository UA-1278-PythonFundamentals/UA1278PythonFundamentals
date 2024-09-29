###################################### TASK 1 ################################################

#Task 1.1
# import this
t1_1= "Task 1.1 \n"
print(t1_1)
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
print("Separately the number of occurrences of the word \"better\" is:",t.count("never"))
print("Separately the number of occurrences of the word \"is\" is:",t.count("is"))

# Task 1.2
t1_2= "\nTask 1.2 \n"
print(t1_2)
print(t.upper())

#Task 1.3
t1_3= "\nTask 1.3 \n"
print(t1_3)

print(t.replace("i", "&"))

###################################### TASK 2 ################################################

t2_1= "\nTask 2 \n"
print(t2_1)

number = 2124   
print ("Number:", number)

t2_1= "\nTask 2.1 \n"
print(t2_1)

digits = [int(digit) for digit in str(number)]

product = 1
for digit in digits:
 product *= digit
print("Product of the digits:", product)

t2_2= "\nTask 2.2 \n"
print(t2_2)

reverse = int(str(number)[::-1])
print("Reversed number:", reverse)

t2_3= "\nTask 2.3 \n"
print(t2_3)

sort = ''.join(sorted(str(number)))
print("Digits in ascending order:", sort)


###################################### TASK 3 ################################################

t3= "\nTask 3 \n"
print(t3)

a= 20
b = 24
print("A =", a, "B =", b)
a , b = b , a
print("Now:\n","A =", a, "B =", b)