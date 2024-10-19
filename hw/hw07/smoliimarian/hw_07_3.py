def num_of_char(str):
    return {i: str.count(i) for i in str}


print(num_of_char("hello"))
