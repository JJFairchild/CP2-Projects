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

    match name:
        case "circle":
            return circle(get_float("What is the radius of your circle?: "))
        case "rectangle":
            return rectangle(get_float("What is the base length of your rectangle?: "), get_float("What is the height of your rectangle?: "))
        case "square":
            return square(get_float("What is the sidelength of your square?: "))
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
            return triangle(a, b, c)
    