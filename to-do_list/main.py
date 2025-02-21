#Jonas Fairchild, to-do list

import os

to_do = []

with open("to-do_list/to-do.txt", "r") as file: #Opens the file and adds every line to a list
    data = file.read() + "\n"
    item = ""
    for line in data:
        if line == "\n":
            to_do.append(item)
            item = ""
        else:
            item += line

for i in to_do: #Removes junk from the list
    if i in ["", "\n"]:
        to_do.remove(i)

def select_item(): #A function used elsewhere to select a specific item in the to-do list. Returns the index of the item.
    print("What item do you want to select?")
    for line in to_do:
        print(f"- {line}", end="\n")
    choice = input()
    while True:
        if choice in to_do:
            return to_do.index(choice)
        else:
            print("That's not in the list. Try again.")
            choice = input("What item do you want to select?: ")

def add_item(): #Adds an item to the to-do list.
    item = input("What item do you want to add?: ")
    to_do.append(item)
    print("Item successfully added.")
    return to_do

def mark_item(): #Selects a item, then, if it's not already marked as complete, do so.
    if to_do:
        item = select_item()
        if " (Completed)" in to_do[item]:
            print("That item is already completed.")
        else:    
            to_do[item] += " (Completed)"
            print("Item successfully marked.")
    else:
        print("There are no items to mark complete.")
    return to_do

def remove_item(): #Similar to the mark function, but instead of adding a specific string to a specific item, it just removes the item entirely.
    if to_do:
        item = select_item()
        del to_do[item]
        print("Item successfully removed.")
    else:
        print("There are no items to remove.")
    return to_do

def display_items(): #Displays every item in the to-do list in a neat order.
    if to_do:
        print("To-do list:")
        for item in to_do:
            print(f"- {item}")
    else:
        print("There's nothing to display.")

def main(): #Main function that branches out to other parts of the program.
    while True:
        os.system("cls")
        match input("What do you want to do?\n1. Add an item\n2. Mark an item as complete\n3. Remove an item\n4. View all items\n5. Exit program\n"):
            case "1":
                to_do = add_item()
            case "2":
                to_do = mark_item()
            case "3":
                to_do = remove_item()
            case "4":
                display_items()
            case "5":
                break
            case _:
                print("Invalid input. Try again.")
        input("Done reading?: ")

main()

with open("to-do_list/to-do.txt", "w") as file: #Deletes the file contents
    file.write("")

with open("to-do_list/to-do.txt", "a") as file: #Writes the to-do list to the text file
    for i in to_do:
        file.write(i + "\n")