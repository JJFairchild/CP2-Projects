#Jonas Fairchild, Word Counter

#Note: Add an option to input the file to read.

import os
import time
from file_handling import count
from time_handling import check_time

def main():
    last_count = count()
    while True:
        os.system("cls")
        match input("What do you want to do?: \n1. View the text file's current wordcount\n2. View the time passed since the last wordcount update\n3. Exit\n"):
            case "1":
                print(f"The document currently has {count()} words.")
            case "2":
                check_time(last_count)
            case "3":
                break
            case _:
                print("Invalid input. Try again.")
        input("Done reading?: ")
        last_count = count()

main()