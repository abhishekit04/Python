


class Circle:
    # Class variable
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * Circle.pi * self.radius

# Creating an object of the Circle class
circle = Circle(7)

# Accessing methods
print(f"Area: {circle.area()}")
print(f"Circumference: {circle.circumference()}")