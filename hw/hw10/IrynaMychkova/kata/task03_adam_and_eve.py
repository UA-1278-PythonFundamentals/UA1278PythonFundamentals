class Human:
    def __init__(self, name: str):
      self.name = name

class Man(Human):
  pass

class Woman(Human):
  pass

class God:
  def __new__(cls):
    return [Man('Adam'), Woman('Eve')]
  
paradise = God()
print(isinstance(paradise[0], Man)) # True
print(paradise[0].name) # Adam
print(paradise[1].name) # Eve