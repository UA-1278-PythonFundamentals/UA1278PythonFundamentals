# Task3. Write a function that calculates the number of characters 
# included in a given string
#  • input: "hello"
#  • output: {"h":1, "e":1,"l":2,"o":1}

user_text = input("Write here: ")

def calculator (text):
    chars = {}
    
    for char in text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    
    return chars

result = calculator(user_text)
print(result)