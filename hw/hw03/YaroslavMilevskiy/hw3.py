zen ='''Beautiful is better than ugly.
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
Namespaces are one honking great idea -- let's do more of those'''
#TASK_1_1
print("Better: " ,zen.count('better') ,"\nNever: " ,zen.count('never'), "\nIs: " ,zen.count('is') )
print()
#TASK_1_2
print("Upper: " ,zen.upper() )
print()
#TASK_1_3
print("Replace: " ,zen.replace("i", "&"))
print()
#TASK_2_1
a,b,c,d = 8,3,1,0
print("Product of the digits: " , a*b*c*d)
print()
#TASK_2_2
numbers = [a,b,c,d]
rvs = numbers[::-1]
print("Answer: " , a)
print()
#TASK_2_3
print("Answer: " , sorted(numbers))
print()
#TASK3
a,b = c,d
print("Swap_A: " , a ,"\nSwap_b:" ,b)

