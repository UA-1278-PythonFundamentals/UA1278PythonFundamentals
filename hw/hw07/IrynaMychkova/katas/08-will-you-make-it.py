# Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg * fuel_left

print(zero_fuel(50, 25, 2)) # => False