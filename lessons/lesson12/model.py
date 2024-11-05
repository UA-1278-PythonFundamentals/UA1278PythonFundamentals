import random
import string

class User:
    def __init__(self, user_id, name, age, email, role):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.email = email
        self.role = role
    
    def __repr__(self):
        return f"User({self.user_id}, {self.name}, {self.age}, {self.email}, {self.role})"
    

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "role": self.role
        }

def generate_random_name():
    first_names = ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona", "George", "Hannah", "Ian", "Julia"]
    last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def generate_random_email(name):
    domains = ["example.com", "testmail.com", "mailservice.com", "webmail.com"]
    email_name = name.lower().replace(" ", ".")
    return f"{email_name}@{random.choice(domains)}"

def generate_random_role():
    roles = ["Admin", "User", "Moderator", "Guest", "Member"]
    return random.choice(roles)

def generate_users(n=10):
    users = []
    for i in range(1, n + 1):
        name = generate_random_name()
        age = random.randint(18, 60)
        email = generate_random_email(name)
        role = generate_random_role()
        users.append(User(user_id=i, name=name, age=age, email=email, role=role))
    return users


def get_next_id(u):
    return max( [user.user_id for user in u] )+1 if u else 1

# Generate 10 users
users = generate_users()
if __name__ == '__main__':
    for user in users:
        print(user)
