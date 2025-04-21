import math

class circle:
    def __init__(self, radius):
        self.name = "circle"
        self.radius = radius

    def help():
        print("A circle has 1 attribute, radius.\n\nHere are some methods you can use:\n- .area() uses pi*r^2 to calculate the area of a circle.\n- .perimeter() uses 2*pi*r to calculate the perimeter of a circle.")
    
    def area(self):
        return math.pi * pow(self.radius, 2)
    
    def perimeter(self):
        return 2 * math.pi * self.radius

class rectangle: # Rectangle class, also compatible with parallelograms
    def __init__(self, base, height):
        self.name = "parallelogram"
        self.base = base
        self.height = height
    
    def help():
        print("A rectangle has 2 attributes, base and height.\n\nHere are some methods you can use:\n- .area() uses base * height to calculate the area of a parallelogram, rectangle, or square.\n- .perimeter() uses 2*base+2*height to calculate the perimeter of a parallelogram, rectangle, or square.")
    
    def area(self):
        return self.base * self.height
    
    def perimeter(self):
        return 2 * self.base + 2 * self.height
    
class square: # Class for squares specifically
    def __init__(self, sidelength):
        self.sidelength = sidelength

    def help():
        print("A square has 1 attribute, sidelength.\n\nHere are some methods you can use:\n- .area() uses sidelength^2 to calculate the area of a square.\n- .perimeter() uses 4*sidelength to calculate the perimeter of a square.")

    def area(self):
        return pow(self.sidelength, 2)
    
    def perimeter(self):
        return 4 * self.sidelength
    
class triangle:
    def __init__(self, a, b, c):
        self.name = "triangle"
        self.a = a
        self.b = b
        self.c = c
    
    def help():
        print("A triangle has 3 attributes, each a different side's length.\n\nHere are some methods you can use:\n- .area() uses sqrt(s(s-a)(s-b)(s-c)) where s is (a+b+c)/2 to calculate the area of a triangle.\n- .perimeter() uses a+b+c to calculate the perimeter of a triangle.")
    
    def area(self): # Calculates the area using three sides rather than base and height
        s = (self.a + self.b + self.c)/2 # Half perimeter
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c)) # Formula
    
    def perimeter(self):
        return self.a + self.b + self.c