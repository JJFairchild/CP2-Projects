import math

# This page defines all the shapes used in the program.

class circle: # Circle class
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius
        self.type = "circle"

    def formulas(self): # Defines the formulas used, all classes here have this.
        print("- .area() uses pi*r^2 to calculate the area of a circle.\n- .perimeter() uses 2*pi*r to calculate the perimeter of a circle.")

    def info(self): # Shows a specific shape's info, all classes here have this.
        print(f"Shape info:\nName: {self.name}\nType: {self.type}\nRadius: {self.radius}")
    
    def area(self): # Shows a specific shape's area, all classes here have this.
        return math.pi * pow(self.radius, 2)
    
    def perimeter(self): #Shows a shape's perimeter, all classes here have this.
        return 2 * math.pi * self.radius
    
    def is_larger(self, shape): # Compares a shape's area to another's, all classes here have this.
        if self.area() > shape.area():
            print(f"{self.name}'s area is greater than {shape.name}'s by {self.area()-shape.area()}.")
        else:
            print(f"{self.name}'s area is smaller than {shape.name}'s by {shape.area()-self.area()}.")
    
    def is_longer(self, shape): # Compares a shape's perimeter to another's, all classes have this.
        if self.perimeter() > shape.perimeter():
            print(f"{self.name}'s perimeter is greater than {shape.name}'s by {self.perimeter()-shape.perimeter()}.")
        else:
            print(f"{self.name}'s perimeter is smaller than {shape.name}'s by {shape.perimeter()-self.perimeter()}.")

class rectangle: # Rectangle class, also compatible with parallelograms and squares
    def __init__(self, name, base, height):
        self.name = name
        self.base = base
        self.height = height
        self.type = "rectangle"
    
    def formulas(self):
        print("- .area() uses base * height to calculate the area of a parallelogram, rectangle, or square.\n- .perimeter() uses 2*base+2*height to calculate the perimeter of a parallelogram, rectangle, or square.")
    
    def info(self):
        print(f"Shape info:\nName: {self.name}\nType: {self.type}\nBase length: {self.base}\nHeight: {self.height}")

    def area(self):
        return self.base * self.height
    
    def perimeter(self):
        return 2 * self.base + 2 * self.height

    def is_larger(self, shape):
        if self.area() > shape.area():
            print(f"{self.name}'s area is greater than {shape.name}'s by {self.area()-shape.area()}.")
        else:
            print(f"{self.name}'s area is smaller than {shape.name}'s by {shape.area()-self.area()}.")
    
    def is_longer(self, shape):
        if self.perimeter() > shape.perimeter():
            print(f"{self.name}'s perimeter is greater than {shape.name}'s by {self.perimeter()-shape.perimeter()}.")
        else:
            print(f"{self.name}'s perimeter is smaller than {shape.name}'s by {shape.perimeter()-self.perimeter()}.")
    
class square: # Class for squares specifically
    def __init__(self, name, sidelength):
        self.name = name
        self.sidelength = sidelength
        self.type = "square"

    def formulas(self):
        print("n- .area() uses sidelength^2 to calculate the area of a square.\n- .perimeter() uses 4*sidelength to calculate the perimeter of a square.")
    
    def info(self):
        print(f"Shape info:\nName: {self.name}\nType: {self.type}\nSidelength: {self.sidelength}")

    def area(self):
        return pow(self.sidelength, 2)
    
    def perimeter(self):
        return 4 * self.sidelength

    def is_larger(self, shape):
        if self.area() > shape.area():
            print(f"{self.name}'s area is greater than {shape.name}'s by {self.area()-shape.area()}.")
        else:
            print(f"{self.name}'s area is smaller than {shape.name}'s by {shape.area()-self.area()}.")
    
    def is_longer(self, shape):
        if self.perimeter() > shape.perimeter():
            print(f"{self.name}'s perimeter is greater than {shape.name}'s by {self.perimeter()-shape.perimeter()}.")
        else:
            print(f"{self.name}'s perimeter is smaller than {shape.name}'s by {shape.perimeter()-self.perimeter()}.")
    
class triangle: # Triangle class, takes 3 sidelengths rather than base and height, this is so you can calculate both area and perimeter.
    def __init__(self, name, a, b, c):
        self.name = name
        self.a = a
        self.b = b
        self.c = c
        self.type = "triangle"
    
    def formulas(self):
        print("- .area() uses sqrt(s(s-a)(s-b)(s-c)) where s is (a+b+c)/2 to calculate the area of a triangle.\n- .perimeter() uses a+b+c to calculate the perimeter of a triangle.")
    
    def info(self):
        print(f"Shape info:\nName: {self.name}\nType: {self.type}\nSidelengths: {self.a}, {self.b}, {self.c}")

    def area(self): # Calculates the area using three sides rather than base and height
        s = (self.a + self.b + self.c)/2 # Half perimeter
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c)) # Formula
    
    def perimeter(self):
        return self.a + self.b + self.c
    
    def is_larger(self, shape):
        if self.area() > shape.area():
            print(f"{self.name}'s area is greater than {shape.name}'s by {self.area()-shape.area()}.")
        else:
            print(f"{self.name}'s area is smaller than {shape.name}'s by {shape.area()-self.area()}.")
    
    def is_longer(self, shape):
        if self.perimeter() > shape.perimeter():
            print(f"{self.name}'s perimeter is greater than {shape.name}'s by {self.perimeter()-shape.perimeter()}.")
        else:
            print(f"{self.name}'s perimeter is smaller than {shape.name}'s by {shape.perimeter()-self.perimeter()}.")