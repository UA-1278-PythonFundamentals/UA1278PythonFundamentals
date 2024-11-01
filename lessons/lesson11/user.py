
from log import logging

class UserError(Exception):
    pass


class User:
    count = 0
    def __init__(self, name: str, age: int) -> None:
        logging.debug(f"create user {self.count} name={name} age={age}")
        self.__class__.count +=1 
        self.name = f"name_{self.count}"
        if age < 0:
            logging.error(f"create user id_{self.count} error age: {age}")
            raise UserError(f"error age: {age}")
        
        self.age = age
        logging.info(f"create user {self}")
    def __repr__(self) -> str:
        logging.debug(f"print user {self.name}")
        return f"({self.name}, {self.age})"
