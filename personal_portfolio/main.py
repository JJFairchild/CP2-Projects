#Jonas Fairchild, Personal Porfolio

import os # Imports the necessary functions from each program.
from problem import main as coin_problem
from problem import load as load_coins
from calculator import main as financial_calculator

def main(): # Main function that branches out to all the programs.
    while True:
        os.system('cls')
        match input("Which program would you like to use?:\n1. Coin Problem Solver\n2. Financial Calculator\n3. Morse Code Translator\n4. Movie Reccomender\n5. Password Generator\n6. Personal Audio Library\n"):
            case '1':
                print("This is a program meant to solve the famous coin problem, and it can do so in many different currencies. I am especially proud of how I was able to make it fully customizable - You can add new currencies with extreme ease - and also near error-proof. It was the first coding project where I used multiple files, and to do so, I just imported necessary functions from the files I needed them from - pretty simple. While coding it, I learned how to do very good error handling (and it shows!), and I honestly enjoyed coding it a lot.")
                input("Done reading?: ")
                try: # Basic error handling for if there are errors reading the file.
                    load_coins()
                    coin_problem()
                except:
                    print("Reading the csv file caused an error. Try renaming it to 'coins.csv' or, if it does not exist, create a csv file with that name.")
            case '2':
                print('description')
                financial_calculator()
        input('Thank you for using the program!\nDone reading?: ')

main()