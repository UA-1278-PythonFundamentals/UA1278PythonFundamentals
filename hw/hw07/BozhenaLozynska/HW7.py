def largest_number(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
        print(largest_number(10, 20))











        import math

def area_of_rectangle(length, width):
    return length * width
def area_of_triangle(base, height):
     return 0.5 * base * height

def area_of_circle(radius):
    return math.pi * radius ** 2

def main():
    print("Choose a shape to calculate the area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    choice = input("Enter the number corresponding to your choice: ")

    if choice == "1":
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        print(f"The area of the rectangle is: {area_of_rectangle(length, width)}")
    
    elif choice == "2":
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        print(f"The area of the triangle is: {area_of_triangle(base, height)}")
    
    elif choice == "3":
        radius = float(input("Enter the radius of the circle: "))
        print(f"The area of the circle is: {area_of_circle(radius)}")
    
    else:
        print("Invalid choice. Please select 1, 2, or 3.")






def character_count(input_string):
    char_count = {}
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

print(character_count(input_string))