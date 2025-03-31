'''
Coin Change Problem:
Implement the logic to solve the Coin Change Problem using the provided coin denominations.
The program should handle various edge cases, such as negative or zero target amounts, and invalid coin denominations.

User Interaction:
Prompt the user to enter the country for which they want to solve the Coin Change Problem.
Prompt the user to enter the target amount.
Display the minimum number of coins needed to make the target amount, as well as the names of the coins used.

Program Structure:
Use inner functions to implement the main features (loading coin denominations, solving the Coin Change Problem).
Implement helper functions for repetitive tasks (e.g., reading and parsing the coin denomination file).
Create a main function to handle user interaction and call the appropriate functions.

Error Handling:
Ensure the program handles potential errors, such as the coin denomination file not being found or the user providing invalid inputs.
'''
import os
from problem import *

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