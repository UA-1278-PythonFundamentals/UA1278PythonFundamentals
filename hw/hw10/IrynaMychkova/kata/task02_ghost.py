import random

class Ghost:
  __colosrs = ['white', 'yellow', 'purple', 'red']

  def __init__(self):
    self.color = random.choice(self.__colosrs)

ghost = Ghost()

print(ghost.color) # random color from the list
