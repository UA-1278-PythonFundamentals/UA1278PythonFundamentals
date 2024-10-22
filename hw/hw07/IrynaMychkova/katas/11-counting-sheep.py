# Counting sheep
def count_sheeps(sheep):
  return sum([x for x in sheep if x])

print(count_sheeps([True,  True,  True,  False]))
