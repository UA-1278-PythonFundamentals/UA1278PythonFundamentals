from typing import Union
from math import pi

class Sphere(object):
    def __init__(self, radius: Union[int, float], mass: Union[int, float]) -> None:
        self.__radius = radius
        self.__mass = mass
    
    def get_radius(self) -> Union[int, float]:
        return self.__radius
  
    def get_mass(self) -> Union[int, float]:
        return self.__mass
    
    def volume(self) -> float:
        return 4/3 * pi * self.__radius ** 3
    
    def get_volume(self) -> float:
        return round(self.volume(), 5)
    
    def get_surface_area(self) -> float:
        return round(4 * pi * self.__radius ** 2, 5)
    
    def get_density(self) -> float:
        return round(self.__mass / self.volume(), 5)
    

sp = Sphere(3, 2)
print(sp.get_radius()) # 3
print(sp.get_mass()) # 2
print(sp.get_volume()) # 113.09734
print(sp.get_surface_area()) # 113.09734
print(sp.get_density()) # 0.01768

    