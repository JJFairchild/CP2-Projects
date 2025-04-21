from shapes import *

def get_float(param):
    while True:
        try:
            num = float(input(param))
            if num > 0:
                return num
            else:
                print("Your number cannot be negative. Try again.")
        except:
            print("That's not a number. Try again.")

def make_shape():
    while True:
        name = input("What do you want your shape to be?:\n- Circle\n- Rectangle\n- Square\n- Triangle\n").lower()
        if name not in ["circle", "rectangle", "square", "triangle"]:
            print("That's not in the list. Try again.")
            continue
        break
    
    shape = input("What will you name your shape?: ").capitalize()

    match name:
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
                if a + b < c:
                    print("The third length of your triangle cannot exceed the other two lengths combined. Try again.")
                    c = get_float("What is the third sidelength of your triangle?: ")
                    continue
                break
            return triangle(shape, a, b, c)
    
def select_shape(shapes):
    if shapes:
        while True:
            print("What shape do you want to select?: ")
            for shape in shapes:
                print(f"- {shape.name}")
            name = input().capitalize()
            for shape in shapes:
                if shape.name == name:
                    return shape
            print("There are no shapes with that name. Try again.")
    else:
        print("There are no shapes to select. Create a shape by pressing '1' in the main menu.")

def shape_info(selected):
    if selected:
        selected.info()
    else:
        print("You haven't selected a shape yet. Select a shape by pressing '2' in the main menu.")

def calculate(selected):
    if selected:
        while True:
            match input("What do you want to do?:\n1: Calculate area\n2: Calculate perimeter\n3: Exit"):
                case "1":
                    print(selected.area())
                case "2":
                    print(selected.perimeter())
                case "3":
                    break
                case _:
                    print("That's not a valid input. Try again.")