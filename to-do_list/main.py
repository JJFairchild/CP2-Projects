#Jonas Fairchild, to-do list

import os

to_do = []

with open("to-do_list/to-do.txt", "r") as file:
    data = file.read() + "\n"
    item = ""
    for line in data:
        if line == "\n":
            to_do.append(item)
            item = ""
        else:
            item += line

def select_item():
    print("What item do you want to select?")
    for line in to_do:
        print(f"- {line}", end="\n")
    choice = input()
    while True:
        if choice in to_do:
            return to_do.index(choice)
        else:
            print("That's not in the list. Try again.")

def add_item():
    item = input("What item do you want to add?: ")
    to_do.append(item)
    return to_do

def mark_item():
    if to_do:
        item = select_item()
        to_do[item]


    else:
        print("There are no items to mark complete.")
        return to_do

def main():
    while True:
        os.system("cls")
        match input("What do you want to do?\n1. Add an item\n2. Mark an item as complete\n3. Remove an item\n4. View all items\n5. Exit program"):
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                break