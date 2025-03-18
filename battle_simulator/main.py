#Jonas Fairchild, Battle Simulator

import os
from characters import *
from battle import battle
from saving import *

chars = load() #Load the characters from previous runs of the program.

def main(chars): # Main function for the entire program.
    while True:
        os.system('cls')
        match input("What do you want to do?\n1. Create a character\n2. Delete a character\n3. View characters\n4. Battle\n5. Exit\n"): # Show the user their choices and wait for their response.
            case "1":
                chars = create_char(chars)
            case "2":
                chars = remove_char(chars)
            case "3":
                display(chars)
            case "4":
                chars = battle(chars)
            case "5":
                break
            case _:
                print("That's not a valid input. Try again.")
        input("Done reading?: ")
    return chars

chars = main(chars) # Makes sure that all the modifications made to the list of chararacters stay intact.

save(chars) # Saves all the characters to the csv file.