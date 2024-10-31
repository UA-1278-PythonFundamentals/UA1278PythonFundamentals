### GitHub Outside for Topic 7

### I. Jenny's secret message
print("I. Jenny's secret message \n")

def text(name):
    if name == "Johnny":
        return "Nice to meet you,", name
    else:
        return "Hello,", name
print(text(input("Hello. What is your name: ")))
print()



### II. Find The Distance Between Two Points
### Любомир, вітаю. Я не зрозумів це завдання, тому не зробив.


### III. No yelling!
print("III. No yelling! \n")

def filter_words(string):
    string = string.capitalize()
    string = string.split()
    string = " ".join(string)
    return(string)

print(filter_words("WOW this is REALLY          amazing"))
print()



### IV. Convert a Number to a String
print("IV. Convert a Number to a String \n")

def number(n):
    before = "before: ", type(n), n
    after = "after: ", type(n), n
    return before, after

print(number(int(10000)))
print()


### V. Reversing Words in a String
print("V. Reversing Words in a String \n")

def words(w):
    w = w.split()
    w = w[::-1]
    w = " ".join(w)
    return(w)
        
print(words("Hello World Today"))
print()


### VI. Reverse List Order
print("VI. Reverse List Order \n")

def listl(l):
    l = l[::-1]
    return(l)
        
print(listl([1,2,3,4]))
print()



### VII. Multiples of 3 or 5
print("VII. Multiples of 3 or 5 \n")

def solution(number):
    sum = 0
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
        if number < 0:
            return(0)
    return(sum)

print(solution(10))
print()


### VIII. Will you make it?
print("VIII. Will you make it? \n")

def fuel(f, distance=50, avr=25):
    x = avr * f
    if x >= distance:
        return(True)
    else:
        return(False)
print(fuel(2))
print()



### IX. Are You Playing Banjo?
print("IX. Are You Playing Banjo? \n")

def name(n):
    n = n.lower()
    for i in n:
        a = str(i)
        break
    if a == "r":
        return("you are playing banjo!")
    else:
         return("you are not playing banjo!")

print(name(input("Your name?: ")))
print()


### X. Convert boolean values to strings 'Yes' or 'No’
print("X. Convert boolean values to strings 'Yes' or 'No’ \n")

def yes_or_no(word):
    if word == "Yes" or word == "yes":
        print(True)
    elif word == "No" or word == "no":
        return(False)
    else:
         return(word, " is not Yes and not No ))")

print(yes_or_no(input("Yes or no?: ")))
print()


### XI. Counting sheep
print("XI. Counting sheep \n")


def sheep(s):
    x = 0
    for i in s:
        if i == True:
            x += 1
    return(x)

print(sheep([True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]))
print()


### XII. Is this my tail?
print("XII. Is this my tail? \n")

def zoo(body, tail):
    if body[-1] == tail:
        x = True
    else:
        x = False
    return(x)

print(zoo("Pig", 'g'))
print(zoo("Pig", 'i'))
