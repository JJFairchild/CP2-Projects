#Jonas Fairchild, Password Generator

#A main function that runs the code
#Functions for the different password requirements
#A function that assembles that password once it is the correct length
#Users should be able to specify length and if they want to include
#uppercase letters
#lowercase letters
#numbers
#special characters

import os
import copy

lower_letters = {"q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"}
upper_letters = []
for letter in lower_letters:
    upper_letters.append(letter.upper())
upper_letters = set(upper_letters)
numbers = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}
special = {"`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "{", "]", "}", "|", ";", ":", "'", '"', ",", "<", ".", ">", "/", "?"}
all_characters = [lower_letters, upper_letters, numbers, special]

def characters():
    while True:
        try:
            characters = int(input("How many characters should your password have?: "))
            while characters < 1 or characters > 100:
                print("That number is too small or too big. Try again.")
                characters = int(input("How many characters should your password have?: "))
            else:
                return characters
        except:
            print("That isn't a number. Try again.")

def add_lower():
    if input("Should your password include lowercase letters? (Y/n): ").lower()[0] == "n":
        del all_characters[0]
        return all_characters
    else:
        return all_characters
    
def add_upper():
    if input("Should your password include uppercase letters? (Y/n): ").lower()[0] == "n":
        del all_characters[1]
        return all_characters
    else:
        return all_characters

def add_numbers():
    if input("Should your password include numbers? (Y/n): ").lower()[0] == "n":
        del all_characters[2]
        return all_characters
    else:
        return all_characters
    
def add_special():
    if input("Should your password include special characters? (Y/n): ").lower()[0] == "n":
        del all_characters[3]
        return all_characters
    else:
        return all_characters