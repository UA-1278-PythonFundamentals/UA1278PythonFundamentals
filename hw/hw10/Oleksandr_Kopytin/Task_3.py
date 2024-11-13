class Employee:
    """class of employee"""

    __counter = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.__counter += 1

    @classmethod
    def employee_counter(cls):
        return cls.__counter

    def employee_info(self):
        return f"name - {self.name}; salary - {self.salary}"


Alex = Employee("Alex", 3000)
Bob = Employee("Bob", 3000)

print("employee counter:", Bob.employee_counter())

print(Employee.__bases__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)
