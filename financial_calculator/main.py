#Jonas Fairchild, Financial Calculator

#Calculate time until goal, weekly or monthly (function)
#Calculate compound interest (function)
#Allocate budget (function)
#Calculate sale price (with discounts) (function)
#Calculate tips (function)

import copy
import os

def goalTime(): #Calculates the time until a specified goal is reached.
    print()
    balance = float(input("How much money do you have?: "))
    goal = float(input("How much money do you want to save?: "))
    if input("Would you like to create a weekly or monthly payment for your goal?: ").lower()[0] == "m":
        goalType = 30
    else:
        goalType = 7
    goalAmount = float(input("How much money will you allocate to your goal after this time?: "))
    print(f"Your goal will take {((goal - balance) / goalAmount) * goalType} days to reach.\n")

def compound(): #Calculates how much money will be made under compound interest.
    print()
    P = float(input("How much money will you invest?: "))
    r = float(input("What is the rate of your investment growth? (in percent form, but remove '%' sign): "))
    n = int(input("What is the rate of compounding? (days per year): "))
    t = float(input("How long will you invest your money? (in years): "))
    print(f"After you compound your money, you will have ${P * (pow((1 + (r / 100) / n), n * t))}, with a profit of ${(P * (pow((1 + (r / 100) / n), n * t))) - P}.\n")

def allocate(): #Gets a bunch of segments with a percent value, and allocates an amount of the total income to those segments.
    print()
    percent = 0
    allocateList = []
    while percent < 100:
        os.system('cls')
        for item in allocateList:
            print(item, end="\n")
        else:
            print()
        print(f"You have {100-percent}% left to allocate.")
        segment = input("What do you want to allocate your income to?: ")
        p = float(input("How much of your income do you want to allocate to this? (in percent form, but remove '%' sign): "))
        percent += p
        allocateList += [f"{copy.deepcopy(segment)}: {copy.deepcopy(p)}%"]
    os.system('cls')
    for item in allocateList:
        print(item, end="\n")
    print()

def sale(): #Calculates how expensive an item is if it is on sale.
    print()
    price = float(input("What is the price of the item you want?: "))
    discount = float(input("What is the discount on the item? (in percent form, but remove '%' sign): "))
    print(f"The item is on sale for ${price * ((100 - discount) / 100)}.\n")

def tip(): #Calclulates how expensive an item is if a tip is included.
    print()
    price = float(input("What is the price of the item you want?: "))
    tip = float(input("How big of a tip do you want to give? (in percent form, but remove '%' sign): "))
    print(f"The total will be ${price * ((100 + tip) / 100)}.\n")

def main(): 
    while True:
        os.system('cls')
        choice = int(input("What do you want to do?\n1: Save for a goal\n2: Use compound interest calculator\n3: Allocate your income for budgeting\n4: Use sale calculator\n5: Use tip calculator\n"))
        if choice == 1:
            goalTime()
        elif choice == 2:
            compound()
        elif choice == 3:
            allocate()
        elif choice == 4:
            sale()
        elif choice == 5:
            tip()
        input("Done reading?: ")

main()