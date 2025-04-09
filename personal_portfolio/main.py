#Jonas Fairchild, Personal Porfolio

import os # Imports the necessary functions from each program.
from problem import main as coin_problem
from problem import load as load_coins
from calculator import main as financial_calculator
from morse import main as morse_translator
from movies import main as movie_reccomender
from password import main as password_generator
from library import main as personal_library

def main(): # Main function that branches out to all the programs.
    while True:
        os.system('cls')
        match input("Which program would you like to use?:\n1. Coin Problem Solver\n2. Financial Calculator\n3. Morse Code Translator\n4. Movie Reccomender\n5. Password Generator\n6. Personal Audio Library\n7. Exit\n"):
            case '1':
                print("This is a program meant to solve the famous coin problem, and it can do so in many different currencies. I am especially proud of how I was able to make it fully customizable - You can add new currencies with extreme ease - and also near error-proof. It was the first coding project where I used multiple files, and to do so, I just imported necessary functions from the files I needed them from - pretty simple. While coding it, I learned how to do very good error handling (and it shows!), and I honestly enjoyed coding it a lot. To use it, simply select a currency, then open the coin problem and fill out the required fields.")
                input("Done reading?: ")
                try: # Basic error handling for if there are errors reading the file.
                    load_coins()
                    coin_problem()
                except:
                    print("Reading the csv file caused an error. Try renaming it to 'coins.csv' or, if it does not exist, create a csv file with that name.")
            case '2':
                print('This program is an all-purpose financial calculator, though it lacks error handling, so be careful. This program shows the first time I used functional decomposition in a thought-out way, and thus all the functions in the actual program are very clear and intuitive.')
                try:
                    financial_calculator()
                except:
                    print("Whoops! Looks like the program crashed. Returning you to the main menu.")
            case '3':
                print("This program is a translator for morse code and English. It was the first time I tried to use two different lists at the same time, which probably wasn't very effective as it would have been much better to have nested lists or dictionaries. I am proud of it, though, because I used some fairly niche methods and functions that I needed to look up.")
                try:
                    morse_translator()
                except:
                    print("Whoops! Looks like the program crashed. Returning you to the main menu.")
            case '4':
                print('This program takes a list of movies and reccomends you some based on search results. It was the first time I tried reading from a csv file (or any file for that matter) and making it work in a program. I also implemented a search function with multiple possible parameters, which is also cool.')
                try:
                    movie_reccomender()
                except:
                    print("Whoops! Looks like the program crashed. Returning you to the main menu.")
            case '5':
                print("This program generates completely random passwords based on your specifications. It doesn't have the same type of main function as my other projects, but I don't see that as an issue. While coding this program, I used sets for the first time and it made sense in the context of the program.")
                try:
                    password_generator()
                except:
                    print("Whoops! Looks like the program crashed. Returning you to the main menu.")
            case '6':
                print("This password lets you create a library/playlist of different songs. It was the first time I used tuples in a program, and though they made development tricky, I got it working in the end. I personally didn't enjoy coding this very much, though it's hard to argue with results. I do believe this was also the first time I implemented my own search function into a program.")
                try:
                    personal_library()
                except:
                    print("Whoops! Looks like the program crashed. Returning you to the main menu.")
            case '7':
                break
        input('Thank you for using the program!\nDone reading?: ')

main()