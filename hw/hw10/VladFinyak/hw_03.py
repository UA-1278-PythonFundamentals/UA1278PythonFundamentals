class Employee:
    num = 0

    def __init__(self, name, salary):
        Employee.num += 1
        self.name = name
        self.salary = salary

    def __str__ (self):
        return f"Name: {self.name}. Salary: {self.salary}"



def class_info(cls):

    print('Base classes: ', cls.__base__)

    print('Class namespace: ', cls.__dict__)

    print('Class: ', cls.__name__)

    print('Module: ', cls.__module__)

    print('Documentation bar: ', cls.__doc__)


a = Employee("Vasia", 100)
print(a)
print(Employee.num)
b = Employee("Ivan", 200)
print(b)
print(Employee.num)
c = Employee("Navi", 300)
print(c)
print(Employee.num)

class_info(Employee)