# 07.1 Practical tasks / [GitHub Topic 7]
print()
print("07.1 Practical tasks / [GitHub Topic 7]")

# Task 1

def numbers(a,b):
    if a > b:
        return(a)
    else:
        return(b)
print(numbers(10,40))



# Task 3
def word(w):
    c = {}
    for i in w:
        c.count(i)
    print(c)
word("hello")