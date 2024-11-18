# Task1. Create a polygon class and a rectangle class
# that inherits from the polygon class and finds the square of rectangle.

class Polygon:
    """Class Polygon"""
    
    def area(self) -> float:
        """Method area"""
        pass

class Rectangle(Polygon):
    """Class Rectangle"""

    def __init__(self, a:float, b:float):
        """Constructor"""
        if a<=0 or b<=0:
            raise ValueError('The sides of the rectangle must be positive')
        
        self.__a = a
        self.__b = b

    def area(self) -> float:
        """Method area"""
        return round(self.__a * self.__b, 2)
    

rect = Rectangle(3, 4)
print(rect.area()) # 12.0
