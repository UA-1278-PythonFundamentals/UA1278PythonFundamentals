# Task3. Create an employee class. Each employee has characteristics such as name and salary.
# The class should have a counter that calculates the total number of employees,
# as well as a method that prints the total number of employees and a method that displays information
# about each employee in particular, namely the name and salary.
# In addition to creating a class, display information about the base classes from which
# the employee class is inherited (__base__), the class namespace (__dict__),
# the class name (__name__), the module name in which the class is defined (__module__),
# the documentation bar ( __doc__)

class Employee:
    '''Create the class and count of employees'''
    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

        Employee.employee_count += 1

    @classmethod
    def total_employee(cls):
        '''Returns the total number of employees'''
        return cls.employee_count

    def info(self):
        return f'Name: {self.name}, Salary: ${self.salary}'

class Meta_information(Employee):
    '''The class with displaying information about parent class'''
    def display_meta():
        print('Base classes: ', Employee.__base__)
        print('Namespace: ', Employee.__dict__)
        print('Class name: ', Employee.__name__)
        print('Module name: ', Employee.__module__)
        print('Documentation bar: ', Employee.__doc__)


emp = Employee('Tonya', 22222)
emp1 = Employee('Sonya', 3333)


print(emp.info())
print(emp1.info())
print(f'Total employee: {Employee.total_employee()}')

Meta_information.display_meta()


