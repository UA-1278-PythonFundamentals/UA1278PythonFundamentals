class Employee:

    counter = 0

    def __init__(self, name, salary):
        Employee.counter += 1
        self.name = name
        self.salary = salary

    def employee_info(self):
        return f'Employee: {self.name}. Salary: {self.salary}'

    @staticmethod
    def total_number():
        return Employee.counter


def class_info(cls):
    print('Base classes: ', cls.__base__)
    print('Class namespace: ', cls.__dict__)
    print('Class: ', cls.__name__)
    print('Module: ', cls.__module__)
    print('Documentation bar: ', cls.__doc__)


a = Employee('Harry', 20000)
b = Employee('Hermione', 40000)
c = Employee('Ronald', 10000)
print(a.employee_info())
print(Employee.total_number())
print()
class_info(Employee)
