# II. Find The Distance Between Two Points

# Given two ordered pairs calculate the distance between them.
# Round to two decimal places.
# This should be easy to do in 0(1) timing.

def calculate_and_print_distance(x1, y1, x2, y2):
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    
    print("The distance between the points is: {}".format(round(distance, 2)))

x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))

calculate_and_print_distance(x1, y1, x2, y2)
