#Jonas Fairchild, Password Generator

import random

#This section of the code simply defines all the sets of letters and characters used in the possible passwords.
lower_letters = {"q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"} 
upper_letters = []
for letter in lower_letters:
    upper_letters.append(letter.upper())
upper_letters = set(upper_letters)
numbers = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}
special = {"`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "{", "]", "}", "|", ";", ":", "'", '"', ",", "<", ".", ">", "/", "?"}
all_characters = [special, numbers, upper_letters, lower_letters]

def characters(): #Gets the length of the user's password
    while True:
        try:
            characters = int(input("How many characters should your password have?: "))
            while characters < 1 or characters > 10000:
                print("That number is too small or too big. Try again.")
                characters = int(input("How many characters should your password have?: "))
            else:
                return characters
        except:
            print("That isn't a number. Try again.")

def add_lower(): #Asks if lowercase letters should be added and removes them from all_characters if not
    choice = input("Should your password include lowercase letters? (Y/n): ").lower()
    if choice == "n":
        del all_characters[3]
        return all_characters
    elif choice == "y":
        return all_characters
    else:
        print("Invalid input. Try again.")
        add_lower()
    
def add_upper(): #Asks if uppercase letters should be added and removes them from all_characters if not
    choice = input("Should your password include uppercase letters? (Y/n): ").lower()
    if choice == "n":
        del all_characters[2]
        return all_characters
    elif choice == "y":
        return all_characters
    else:
        print("Invalid input. Try again.")
        add_upper()

def add_numbers(): #Asks if numbers should be added and removes them from all_characters if not
    choice = input("Should your password include numbers? (Y/n): ").lower()
    if choice == "n":
        del all_characters[1]
        return all_characters
    elif choice == "y":
        return all_characters
    else:
        print("Invalid input. Try again.")
        add_numbers()
    
def add_special(): #Asks if special characters should be added and removes them from all_characters if not
    choice = input("Should your password include special characters? (Y/n): ").lower()
    if choice == "n":
        del all_characters[0]
        return all_characters
    elif choice == "y":
        return all_characters
    else:
        print("Invalid input. Try again.")
        add_special()
    

def password_gen(ch): #Takes the list of all characters and an intended password length, then randomly generates 4 passwords with this information.
    for i in range(1, 5):
        password = ""
        while len(password) != ch:
            password += random.choice(list(random.choice(all_characters)))
        print(f"{i}. {password}")

def main(): #Collects all the previous functions neatly, and gets all the information the password_gen function needs to make passwords.
    choice = "y"
    while True:
        if choice == "y":
            ch = characters()
            all_characters = add_lower()
            all_characters = add_upper()
            all_characters = add_numbers()
            all_characters = add_special()
            print()
            password_gen(ch)
            print()
            choice = input("Print more passwords? (Y/n): ").lower()
        elif choice == "n":
            break
        else:
            while choice not in ["y", "n"]:
                print("Invalid input. Try again.")
                choice = input("Print more passwords? (Y/n): ").lower()

main()