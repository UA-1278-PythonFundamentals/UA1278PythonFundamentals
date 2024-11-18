class Employee:

    counter = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.counter += 1

    def get_info(self):
        return f"Name: {self.name}, Salary: {self.salary}"

    @classmethod
    def total_employees(cls):
        print(f"Total number of employees: {cls.counter}")

    def additional_class_info(self):
        print(f"Base classes: {self.__class__.__bases__}")
        print(f"Class namespace: {self.__class__.__dict__}")
        print(f"Class name: {self.__class__.__name__}")
        print(f"Module name: {self.__class__.__module__}")
        print(f"Documentation: {self.__class__.__doc__}")


e1 = Employee("John", 1800)
e2 = Employee("Julia", 2000)

print(e1.get_info())
print(e2.get_info())

Employee.total_employees()

e1.additional_class_info()
e2.additional_class_info()
