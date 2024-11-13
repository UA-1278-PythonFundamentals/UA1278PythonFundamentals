class Employee:
    """This class about employees"""
    employyes = 0
    def __init__(self, name = "John", salary = 1800):
        self.name = str(name)
        self.salary = float(salary)
        Employee.employyes+=1

    def print_empl(self):
        print(f"This is {self.name}. His salary {self.salary}")

    @classmethod
    def emp_counter(cls):
        print(f"Total number of employyes is {cls.employyes}")

    def display_class_info(self):
        """Метод для виводу інформації про клас."""
        print("Інформація про клас Employee:")
        print(f"Базові класи: {self.__class__.__bases__}")
        print(f"Простір імен класу: {self.__class__.__dict__}")
        print(f"Ім'я класу: {self.__class__.__name__}")
        print(f"Ім'я модуля: {self.__class__.__module__}")
        print(f"Документація: {self.__class__.__doc__}")

e1 = Employee("flksdj", 45678)
e2 = Employee("ansldfn", 76890)
e3 = Employee()

e3.print_empl()

Employee.emp_counter()

e3.display_class_info()