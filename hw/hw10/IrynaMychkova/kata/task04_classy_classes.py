class Person:
    def __init__(self, name:str, age:int):
        self.info=f"{name}s age is {age}"
    
    def get_info(self) -> str:
        return self.info

jhon = Person("Jhon", 21)
print(jhon.get_info()) # Jhons age is 21