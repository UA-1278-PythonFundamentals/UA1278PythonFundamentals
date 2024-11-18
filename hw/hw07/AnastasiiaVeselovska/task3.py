def number_of_characters(string):
    d = {}
    for key in string:
        value = string.count(key)
        d[key] = value 
    return d
    
string = input("Enter string: ")
print(number_of_characters(string))
    