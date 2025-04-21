#Jonas Fairchild, Geometry Calculator

import os
from ui import *

def main():
    shapes = []
    selected = None
    while True:
        os.system('cls')
        try:
            print(f"Selected shape: {selected.name}")
        except:
            pass
        match input("What do you want to do?:\n1. Create a shape\n2. Select a shape\n3. View shape info\n4. Run calculations\n5. Shape comparisons\n6. List shapes by value\n7. Help\n8. Exit\n"):
            case "1":
                shapes.append(make_shape())
            case "2":
                selected = select_shape(shapes)
            case "3":
                shape_info(selected)
            case "4":
                calculate(selected)
            case "8":
                break
            case _:
                print("That's not a valid input. Try again.")
        input("Done reading?: ")


main()