import math
class circle:
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return math.pi * self.radius**2
    def calculate_perimeter(self):
        return 2* math.pi * self.radius 

radius = float(input("enter the radius of the circle: "))
circle1 = circle(radius)
perimeter = circle1.calculate_perimeter()
area = circle1.calculate_area()

print("Area of the circle: ", area)
print("Perimeter of the circle: ", perimeter)

        