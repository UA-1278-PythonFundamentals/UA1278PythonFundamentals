# Ви маєте записати філософію Python у вигляді рядка:
# окремо підрахувати кількість появ слів "better", "never" і "is" у заданому рядку
# відобразити весь текст великими літерами (усі літери у верхньому регістрі)
# замінити всі входження символу "i" на "&"
# Задано натуральне чотиризначне число:
# знайти добуток цифр цього числа
# записати число у зворотному порядку
# відсортувати цифри числа у порядку зростання
# Поміняти значення двох змінних місцями без використання третьої змінної.

print("TASK1_______________________________")

zen = "Beautiful is better than ugly.\
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

print(f"Better: {zen.lower().count('Better')}")
print(f"Never: {zen.lower().count('Never')}")
print(f"Is: {zen.lower().count('Is')}")
print(zen.upper())
zen = zen.replace("i","&")
print(zen)

print("TASK2_______________________________")

n = 2143
n1 = n%10
n2 = n//10%10
n3 = n//100%10
n4 = n//1000%10
m = n1*n2*n3*n4
print(m)
print(str(n)[-1::-1])

if n1 > n2:
    n1, n2 = n2, n1
if n1 > n3:
    n1, n3 = n3, n1
if n1 > n4:
    n1, n4 = n4, n1
if n2 > n3:
    n2, n3 = n3, n2
if n2 > n4:
    n2, n4 = n4, n2
if n3 > n4:
    n3, n4 = n4, n3

newn = 1000 * n1 + 100 * n2 + 10 * n3 + n4

print(newn)

print("TASK3_______________________________")

n1, n2 = n2, n1









