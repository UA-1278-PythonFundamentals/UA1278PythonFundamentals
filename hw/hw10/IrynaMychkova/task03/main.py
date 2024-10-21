# Task3. Create an employee class. Each employee has characteristics such as name and salary.
# The class should have a counter that calculates the total number of employees, as well as a 
# method that prints the total number of employees and a method that displays information 
# about each employee in particular, namely the name and salary.
#
# In addition to creating a class, display information about the base classes from which the 
# employee class is inherited (__base__), the class namespace (__dict__), the class name
# (__name__), the module name in which the class is defined (__module__), the documentation bar doc

from employee import Employee

def display_class_info(cls):
    """
    Function to display information about a class.
    
    Args:
    cls (type): The class to display information about.
    """
    print(f"Base classes: {cls.__bases__}")
    print(f"Class namespace: {cls.__dict__}")
    print(f"Class name: {cls.__name__}")
    print(f"Module name: {cls.__module__}")
    print(f"Documentation: {cls.__doc__}")


Kate = Employee("Kate", 1000)
print(Kate.get_info())
print(f"Total number of employees: {Employee.count()}")
Nick = Employee("Nick", 2000)
print(Nick.get_info())
print(f"Total number of employees: {Employee.count()}")
del Kate
print(f"Total number of employees: {Employee.count()}")

display_class_info(Employee)
