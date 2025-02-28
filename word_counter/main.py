#Jonas Fairchild, Word Counter

import os

def main():
    while True:
        os.system("cls")
        match input("What do you want to do?: \n1. View the text file's current wordcount\n2. View the time passed since the last wordcount update\n3. Exit\n"):
            case "1":
                pass
            case "2":
                pass
            case "3":
                break
            case _:
                print("Invalid input. Try again.")
        input("Done reading?: ")

main()