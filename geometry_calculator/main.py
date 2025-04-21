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
        match input("What do you want to do?:\n1. Create a shape\n2. Select a shape\n3. Run calculations\n4. Help\n5. Shape comparisons\n6. List shapes by value\n7. Exit\n"):
            case "1":
                shapes.append(make_shape())
                print(shapes)
            case "2":
                pass
            case "3":
                pass
        input("Done reading?: ")


main()