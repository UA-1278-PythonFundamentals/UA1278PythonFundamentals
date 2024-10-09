# Task1. Create a list that contains elements of integer type, then use 
# the loop to change the type of these elements to a floating type.
# (Hint: use the built-in float () function).
list = [1, 2, 3, 4, 5, 0, -1, -2, -3, -4, -5]

for i in range(len(list)):
    list[i] = float(list[i])
    
print(list)
