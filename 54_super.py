# super() = Functions used in a child class to call methods from a parent class (superclass).
#           Allows you to extend the functionality of the inherited methods
class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius
    def describe(self): # It is method override as child has same method as of parent, but if you want to use parent method also use super()
        super().describe()  # extend functionality
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius}cm²")

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self): # It is method override as child has same method as of parent, but if you want to use parent method also use super()
        super().describe()  # extend functionality
        print(f"It is a square with an area of {self.width * self.width}cm²")


class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self): # It is method override as child has same method as of parent, but if you want to use parent method also use super()
        super().describe()  # extend functionality
        print(f"It is a triangle with an area of {1/2 * self.width * self.height}cm²")


circle = Circle("red",True, 5)
square = Square("blue", False, 6)
triangle = Triangle("yellow", True, 7, 8)

# print(triangle.color)
# print(triangle.is_filled)
# print(triangle.width)
# print(triangle.height)
circle.describe()
square.describe()
triangle.describe()