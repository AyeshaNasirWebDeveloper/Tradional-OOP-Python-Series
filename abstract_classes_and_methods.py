# Assignment: 9

# Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangel(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    
class Sqaure(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5* self.base * self.height
    

rect = Rectangel(10, 5)
circle = Circle(7)
sqaure = Sqaure(4)
triangle = Triangle(6, 8)

print(f"Area of rectangle: {rect.area()}")
print(f"Area of circle: {circle.area()}")
print(f"Area of sqaure: {sqaure.area()}")
print(f"Area of triangle: {triangle.area()}")