# Task3. Write a function that calculates the number of characters 
# included in given string
# • input: "hello"
# • output: {"h":1, "e": 1,"|": 2,"o": 1}

def number_of_characters(s: str) -> dict:
    """
    This function calculates the number of characters included in given string
    :param s: str
    :return: dict
    """
    return {i: s.count(i) for i in s}

print(number_of_characters("hello"))
print(number_of_characters("hello world"))