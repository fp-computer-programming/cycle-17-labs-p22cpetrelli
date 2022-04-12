#author CJP 4/12/2022
import math

class Circle:
    """ Circle class represents a circle """
    def __init__(self):
        """ Create a new circle with radius 3 """
        self.radius = 3
    def get_diameter(self):
        """ Calculate diameter of circle """
        return self.radius * 2
    def get_perimeter(self):
        """ Calculate perimeter of circle """
        return self.get_diameter() * math.pi

my_circle = Circle()

print(my_circle.radius)
print(my_circle.get_diameter())
print(my_circle.get_perimeter())