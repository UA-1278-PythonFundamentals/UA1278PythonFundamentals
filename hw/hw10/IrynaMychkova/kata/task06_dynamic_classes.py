
class MyClass:
    def __init__(self, name: str = 'old') -> None:
        self.name = name

import re

def class_name_changer(cls, new_name):
    """
    Function to change the class name.
    
    Args:
    cls (type): The class to change the name of.
    new_name (str): The new name for the class.
    
    Returns:
    type: The class with the new name.
    """

    # Validate the new name
    if not re.match(r'^[A-Z][A-Za-z0-9]*$', new_name):
        raise ValueError("Class name must start with an uppercase letter and contain only alphanumeric characters.")
    
    cls.__name__ = new_name
    return cls

myObject = MyClass();
print(MyClass.__name__, "MyClass")

class_name_changer(MyClass, "UsefulClass");
print(MyClass.__name__, "UsefulClass")

class_name_changer(MyClass, "SecondUsefulClass");
print(MyClass.__name__, "SecondUsefulClass")

