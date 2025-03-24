#Jonas Fairchild, Battle Simulator

"""
Data Analysis:
Use Pandas to load character data into a DataFrame
Implement basic statistical analysis on character attributes (e.g., mean, median, max, min)

Documentation Reading:
Demonstrate understanding of library documentation by implementing at least one additional feature from each library not explicitly required above
"""

import os
from characters import *
from battle import battle
from saving import *
from display import visualize

chars = load() #Load the characters from previous runs of the program.

def main(chars): # Main function for the entire program.
    while True:
        os.system('cls')
        match input("What do you want to do?\n1. Create a character\n2. Generate a random character \n3. Delete a character\n4. View characters\n5. Visualize ALL character stats\n6. Analyze characters\n7. Battle\n8. Exit\n"): # Show the user their choices and wait for their response.
            case "1":
                chars = create_char(chars)
            case "2":
                chars = random_char(chars)
                pass
            case "3":
                chars = remove_char(chars)
            case "4":
                display(chars)
                print(chars)
            case "5":
                print("Note: Trying to display more than 5 characters at once may cause overlapping text.")
                visualize(chars)
                pass
            case "6":
                #analyze(chars)
                pass
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