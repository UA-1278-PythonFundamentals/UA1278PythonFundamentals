class Employee:
    """
    Class to represent an Employee.
    
    Attributes:
    __counter (int): Class variable to keep track of the number of Employee instances.
    __name (str): Instance variable for the employee's name.
    __salary (float): Instance variable for the employee's salary.
    """
    __counter = 0

    def __init__(self, name: str, salary: float):
        """
        Constructor to initialize an Employee object.
        
        Args:
        name (str): The name of the employee.
        salary (float): The salary of the employee.
        """
        Employee.__counter += 1
        self.__name = name
        self.__salary = salary
    
    def get_info(self) -> str:
        """
        Method to get the employee's information.
        
        Returns:
        str: A string containing the employee's name and salary.
        """
        return f"Name: {self.__name}, Salary: {self.__salary}"
    
    @classmethod
    def count(cls) -> int:
        """
        Class method to get the current count of Employee instances.
        
        Returns:
        int: The number of Employee instances.
        """
        return Employee.__counter
    
    def __del__(self):
        """
        Destructor to decrement the employee counter when an Employee object is deleted.
        """
        Employee.__counter -= 1