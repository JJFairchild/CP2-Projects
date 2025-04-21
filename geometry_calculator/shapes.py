import math

class circle:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius
        self.type = "circle"

    def formulas():
        print("- .area() uses pi*r^2 to calculate the area of a circle.\n- .perimeter() uses 2*pi*r to calculate the perimeter of a circle.")

    def info(self):
        print(f"Shape info:\nName: {self.name}\nType: {self.type}\nRadius: {self.radius}")
    
    def area(self):
        return math.pi * pow(self.radius, 2)
    
    def perimeter(self):
        return 2 * math.pi * self.radius

class rectangle: # Rectangle class, also compatible with parallelograms and squares
    def __init__(self, name, base, height):
        self.name = name
        self.base = base
        self.height = height
        self.type = "rectangle"
    
    def formulas():
        print("- .area() uses base * height to calculate the area of a parallelogram, rectangle, or square.\n- .perimeter() uses 2*base+2*height to calculate the perimeter of a parallelogram, rectangle, or square.")
    
    def info(self):
        print(f"Shape info:\nName: {self.name}\nType: {self.type}\nBase length: {self.base}\nHeight: {self.height}")

    def area(self):
        return self.base * self.height
    
    def perimeter(self):
        return 2 * self.base + 2 * self.height
    
class square: # Class for squares specifically
    def __init__(self, name, sidelength):
        self.name = name
        self.sidelength = sidelength
        self.type = "square"

    def formulas():
        print("n- .area() uses sidelength^2 to calculate the area of a square.\n- .perimeter() uses 4*sidelength to calculate the perimeter of a square.")
    
    def info(self):
        print(f"Shape info:\nName: {self.name}\nType: {self.type}\nSidelength: {self.sidelength}")

    def area(self):
        return pow(self.sidelength, 2)
    
    def perimeter(self):
        return 4 * self.sidelength
    
class triangle:
    def __init__(self, name, a, b, c):
        self.name = name
        self.a = a
        self.b = b
        self.c = c
        self.type = "triangle"
    
    def formulas():
        print("- .area() uses sqrt(s(s-a)(s-b)(s-c)) where s is (a+b+c)/2 to calculate the area of a triangle.\n- .perimeter() uses a+b+c to calculate the perimeter of a triangle.")
    
    def info(self):
        print(f"Shape info:\nName: {self.name}\nType: {self.type}\nSidelengths: {self.a}, {self.b}, {self.c}")

    def area(self): # Calculates the area using three sides rather than base and height
        s = (self.a + self.b + self.c)/2 # Half perimeter
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c)) # Formula
    
    def perimeter(self):
        return self.a + self.b + self.c