#Jonas Fairchild, Battle Simulator

import os
from characters import *
from battle import battle
from saving import *
from display import visualize
from analyze import analyze

chars = load() #Load the characters from previous runs of the program.

def main(chars): # Main function for the entire program.
    while True:
        os.system('cls')
        match input("What do you want to do?\n1. Create a character\n2. Generate a random character \n3. Delete a character\n4. View characters\n5. Visualize character stats\n6. Analyze characters\n7. Battle\n8. Exit\n"): # Show the user their choices and wait for their response.
            case "1":
                chars = create_char(chars)
            case "2":
                chars = random_char(chars)
            case "3":
                chars = remove_char(chars)
            case "4":
                display(chars)
            case "5":
                print("Note: Trying to display more than 5 characters at once may cause overlapping text.")
                visualize(chars)
            case "6":
                analyze(chars)
            case "7":
                chars = battle(chars)
            case "8":
                break
            case _:
                print("That's not a valid input. Try again.")
        input("Done reading?: ")
    return chars

chars = main(chars) # Makes sure that all the modifications made to the list of chararacters stay intact.

save(chars) # Saves all the characters to the csv file.