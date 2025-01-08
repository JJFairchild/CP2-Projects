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

balance = 0
def goalTime(): #Calculates the time until a specified goal is reached.
    goal = int(input("How much money do you want to save?: "))
    goalType = input("Would you like to create a weekly or monthly payment for your goal?: ").lower()
    goalAmount = int(input("How much money will you allocate to your goal after this time?: "))
    print(f"Your goal will take ")
