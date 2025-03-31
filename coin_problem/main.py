# Jonas Fairchild, Coin Change Problem

import os
from problem import *
from file_handling import load

def main(): # Simple main function that branches out to other parts of the program.
    country = None
    while True:
        os.system('cls')
        match input("What do you want to do?:\n1. Select a currency\n2. Solve the coin change problem\n3. Exit\n"):
            case '1':
                country = get_country()
            case '2':
                solve(country)
            case '3':
                break
            case _:
                print("That's not a valid input. Try again.")
        input("Done reading?: ")

try: # Basic error handling for if there are errors reading the file.
    load()
    main()
except:
    print("Reading the csv file caused an error. Try renaming it to 'coins.csv' or, if it does not exist, create a csv file with that name.")