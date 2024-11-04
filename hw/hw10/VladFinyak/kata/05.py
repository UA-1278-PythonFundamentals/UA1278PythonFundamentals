import math

class Sphere():
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
    
    def get_radius(self):
        return self.radius
    
    def get_mass(self):
        return self.mass
    
    def get_volume(self):
        return 4/3 * math.pi * self.radius ** 3
    
    def get_surface_area(self):
        return 4 * math.pi * self.radius ** 2
    
    def get_density(self):
        self.volume = 4/3 * math.pi * self.radius ** 3
        return self.mass / self.volume