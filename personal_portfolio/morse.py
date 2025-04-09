#Jonas Fairchild, Morse Translator

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '-----', '/']
import os

def english_to_morse(): # Translates english to morse code.
    string = input("What message do you want to translate to morse code?: ")
    
    translated_list = []  # Creates a new list to store translated characters
    for char in string:
        if char.lower() in characters:
            translated_list.append(morse[characters.index(char.lower())])  # Gets Morse equivalent
    
    translated_string = ' '.join(translated_list) # Joins letters with spaces, actual spaces appear as slashes.
    print(f"Here is your translated message:\n{translated_string}")

def morse_to_english(): # Translates morse code to english.
    string = input("What message do you want to translate to English?: ") + " "
    string_list = []
    morse_character = ""
    for i in string: # Makes the string a list so it can be modified
        if i == " ":
            string_list.append(morse_character)
            morse_character = ''
        else:
            morse_character += i
    
    for i in string_list: # Changes morse code letters to their corresponding characters.
        if i in morse:
            string_list[string_list.index(i)] = characters[morse.index(i)]
        else:
            del string_list[string_list.index(i)]
    

    string = ''.join(string_list) 
    print(f"Here is your translated message:\n{string}")

def main():
    while True:
        os.system("cls")
        match input("What do you want to do?\n1. Translate English to morse\n2. Translate morse to English\n3. Exit\n"):
            case '1':
                english_to_morse()
            case '2':
                morse_to_english()
            case '3':
                break
            case _:
                print("Invalid input. Try again.")
        input("Done reading?: ")