class Employee:
    total_count = 0

    def __init__(self, full_name, salary_amount):
        self.full_name = full_name
        self.salary_amount = salary_amount
        Employee.total_count += 1

    @classmethod
    def count_employees(cls):
        print(f"Total number of employees: {cls.total_count}")

    def show_info(self):
        print(f"Name: {self.full_name}, Salary: {self.salary_amount}")

employee1 = Employee("Oleh Kovalenko", 55000)
employee2 = Employee("Anna Shevchenko", 65000)

Employee.count_employees()
employee1.show_info()
employee2.show_info()

print(f"Base classes: {Employee.__bases__}")
print(f"Class namespace: {Employee.__dict__}")
print(f"Class name: {Employee.__name__}")
print(f"Module name: {Employee.__module__}")
print(f"Documentation panel: {Employee.__doc__}")
