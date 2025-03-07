#Jonas Fairchild, Battle Simulator

import os
from characters import *

def main(chars):
    while True:
        os.system('cls')
        match input("What do you want to do?\n1. Create a character\n2. Change a character's info\n3. Delete a character\n4. View characters\n5. Battle\n6. Exit\n"):
            case "1":
                chars = create_char(chars)
            case "2":
                chars = edit_char(chars)
            case "3":
                chars = remove_char(chars)
            case "4":
                pass
            case "5":
                pass
            case "6":
                break
            case _:
                print("That's not a valid input. Try again.")
        input("Done reading?: ")
    return chars

main()