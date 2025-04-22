from shapes import *

def get_float(param): # Basic helper function for getting a float.
    while True:
        try:
            num = float(input(param))
            if num > 0:
                return num
            else:
                print("Your number cannot be negative. Try again.")
        except:
            print("That's not a number. Try again.")

def make_shape(): # Adds a shape to the list of shapes.
    while True: # Gets a circle, rectangle, triangle, or square.
        name = input("What do you want your shape to be?:\n- Circle\n- Rectangle\n- Square\n- Triangle\n").lower()
        if name not in ["circle", "rectangle", "square", "triangle"]:
            print("That's not in the list. Try again.")
            continue
        break
    
    shape = input("What will you name your shape?: ").capitalize() # Gets the shape's name.

    match name: # Creates the shape.
        case "circle":
            return circle(shape, get_float("What is the radius of your circle?: "))
        case "rectangle":
            return rectangle(shape, get_float("What is the base length of your rectangle?: "), get_float("What is the height of your rectangle?: "))
        case "square":
            return square(shape, get_float("What is the sidelength of your square?: "))
        case "triangle":
            a = get_float("What is the first sidelength of your triangle?: ")
            b = get_float("What is the second sidelength of your triangle?: ")
            c = get_float("What is the third sidelength of your triangle?: ")
            while True:
                if a + b < c: # Error handling for triangle lengths.
                    print("The third length of your triangle cannot exceed the other two lengths combined. Try again.")
                    c = get_float("What is the third sidelength of your triangle?: ")
                    continue
                break
            return triangle(shape, a, b, c)
    
def select_shape(shapes): # Assigns a selected shape.
    if shapes: # Error handling for if there are no shapes.
        while True:
            print("What shape do you want to select?: ")
            for shape in shapes: # Shows the available shapes.
                print(f"- {shape.name}")
            name = input().capitalize()
            for shape in shapes: # aka If the shape the user selected exists
                if shape.name == name:
                    return shape
            print("There are no shapes with that name. Try again.")
    else:
        print("There are no shapes to select. Create a shape by pressing '1' in the main menu.")

def shape_info(selected): # Prints the selected shape's info
    if selected: # Error handling for if the user hasn't selected a shape.
        selected.info()
    else:
        print("You haven't selected a shape yet. Select a shape by pressing '2' in the main menu.")

def calculate(selected): # Small menu for calculating the perimeter and area of the selected shape.
    if selected:
        while True:
            match input("What do you want to do?:\n1: Calculate area\n2: Calculate perimeter\n3: Exit\n"):
                case "1":
                    print(f"Your shape's area is {selected.area()}.")
                case "2":
                    print(f"Your shape's perimeter is {selected.perimeter()}.")
                case "3":
                    break
                case _:
                    print("That's not a valid input. Try again.")
    else:
        print("You haven't selected a shape yet. Select a shape by pressing '2' in the main menu.")

def compare(selected, shapes): # Gets another shape to compare with, then lets the user compare their areas and perimeters.
    if len(shapes) >= 2: # There have to be at least 2 shapes to compare.
        if selected:
            while True:

                print("What shape do you want to compare yours to?: ")
                for shape in shapes:
                    print(f"- {shape.name}")
                name = input().capitalize()
                for shape in shapes:
                    if shape.name == name:

                        while True: # Small menu for comparing shapes.
                            match input("What do you want to do?:\n1: Compare area\n2: Compare perimeter\n3: Exit\n"):
                                case "1":
                                    selected.is_larger(shape)
                                case "2":
                                    selected.is_longer(shape)
                                case "3":
                                    return
                                case _:
                                    print("That's not a valid input. Try again.")

                print("There are no shapes with that name. Try again.")
        else:
            print("You haven't selected a shape yet. Select a shape by pressing '2' in the main menu.")
    else:
        print("You need at least two shapes to compare shapes. Create a shape by pressing '1' in the main menu.")

def area_sort(x): # This and the next function are helper functions for the sort methods used in shape_sort().
    return x.area()

def perim_sort(x):
    return x.perimeter()

def shape_sort(shapes): # Sorts the shapes based on area or perimeter.
    if shapes:
        while True: # Small menu for switching between sorting types.
            match input("What do you want to do?:\n1: Sort shapes by area\n2: Sort shapes by perimeter\n3: Exit\n"):
                case "1":
                    shapes.sort(key=area_sort, reverse=True)
                    for i in shapes:
                        print(f"- {i.name}: {i.type} with an area of {i.area()}")
                case "2":
                    shapes.sort(key=perim_sort, reverse=True)
                    for i in shapes:
                        print(f"- {i.name}: {i.type} with a perimeter of {i.perimeter()}")
                case "3":
                    break
                case _:
                    print("That's not a valid input. Try again.")
    else:
        print("There are no shapes to sort. Create shapes by pressing '1' in the main menu.")

def shape_formulas(selected): # Prints all the formulas used for the selected shape type.
    if selected:
        selected.formulas()
    else:
        print("You haven't selected a shape yet. Select a shape by pressing '2' in the main menu.")