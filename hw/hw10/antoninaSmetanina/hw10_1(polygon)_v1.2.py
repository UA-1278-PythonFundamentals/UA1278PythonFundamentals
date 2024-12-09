# Create a polygon class and a rectangle class
# that inherits from the polygon class and finds the square
# of rectangle

# from math import tan, radians


class Polygon:
    def __init__(self, sides):
        self.sides = sides


class Rectangle(Polygon):
    def __init__(self, a, b):
        super().__init__(4)
        self.a = a
        self.b = b

    def find_area(self):
        area = self.a * self.b
        return print(f'The area of the triangle is {area}')


rectangle = Rectangle(2, 4)
rectangle.find_area()  # Calculate and display the area
