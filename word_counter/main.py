#Jonas Fairchild, Word Counter

#Note: Add an option to input the file to read.

import os
import time
from file_handling import count
from time_handling import check_time

def find_path():
    txt = input("What is the relative path of the intended text file?: ")
    while True:
        try:
            with open(txt, "r") as file:
                file.read()
            break
        except:
            print("That path doesn't work. Try again.")
            txt = input("What is the relative path of the intended text file?: ")
    return txt

def main():
    txt = find_path()
    last_count = count(txt)
    edit_time = False
    while True:
        edit_time = check_time(last_count, txt, edit_time)
        last_count = count(txt)
        os.system("cls")
        match input("What do you want to do?:\n1. Change the path\n2. View the text file's current wordcount\n3. View the time passed since the last wordcount update\n4. Exit\n"):
            case "1":
                txt = find_path()
            case "2":
                print(f"The document currently has {count(txt)} words.")
            case "3":
                if edit_time:
                    print(f"The document's word count was updated {int(time.time() - edit_time)} seconds ago.")
                else:
                    print("The document has not been updated since the program started.")
            case "4":
                break
            case _:
                print("Invalid input. Try again.")
        input("Done reading?: ")

main()