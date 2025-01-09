#Jonas Fairchild, Financial Calculator

#store Balance
#Add to balance
#take from balance
#Calculate time until goal, weekly or monthly (function)
#Calculate compound interest (function)
#Allocate budget (function)
#Calculate sale price (with discounts) (function)
#Calculate tips (function)


def main():
    pass

import copy
balance = 100

def goalTime(): #Calculates the time until a specified goal is reached.
    print(f"You have ${balance}.")
    goal = float(input("How much money do you want to save?: "))
    if input("Would you like to create a weekly or monthly payment for your goal?: ").lower()[0] == "m":
        goalType = 30
    else:
        goalType = 7
    goalAmount = int(input("How much money will you allocate to your goal after this time?: "))
    print(f"Your goal will take {((goal - balance) / goalAmount) * goalType} days to reach.")
    if input("Would you like to follow this goal? (Y/n): ").lower()[0] == "y":
        print(f"{((goal - balance) / goalAmount) * goalType} days have passed. You now have ${goal}.")
        return goal
    else:
        return ""

def compound(): #Calculates how much money will be made under compound interest.
    print(f"You have ${balance}.")
    P = float(input("How much money will you invest?: "))
    r = float(input("What is the rate of your investment growth? (in percent form, but remove '%' sign): "))
    n = int(input("What is the rate of compounding? (days per year): "))
    t = float(input("How long will you invest your money? (in years): "))
    print(f"After you compound your money, you will have ${P * (pow((1 + (r / 100) / n), n * t))}, with a profit of ${(P * (pow((1 + (r / 100) / n), n * t))) - P}.")
    if input("Would you like to commit to this investment? (Y/n): ").lower()[0] == "y":
        print(f"{t} years have passed. You have profited by ${(P * (pow((1 + (r / 100) / n), n * t))) - P}.")
        return (P * (pow((1 + (r / 100) / n), n * t))) - P
    else:
        return ""

def allocate(): #Gets a bunch of segments with a percent value, and allocates an amount of the total income to those segments.
    percent = 0
    allocateList = []
    while percent < 100:
        segment = input("What do you want to allocate your income to?: ")
        p = int(input("How much of your income do you want to allocate to this? (in percent form, but remove '%' sign): "))
        percent += p
        allocateList += f"{copy.deepcopy(segment)}, {copy.deepcopy(p)}"
        print(f"You have {100-percent}% left to allocate.")
    print(allocateList, end='\n')

allocate()