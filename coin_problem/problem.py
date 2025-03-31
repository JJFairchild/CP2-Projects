from file_handling import load

def solve(country):
    if country:
        currency = load()[country] # Gets the values of the currency the user selected.
        print("You are a cashier deciding how much change to give back to a person.") # Gives the user some background information

        while True: # Gets the value of the item the customer wants to buy
            try:
                target = float(input("\nWhat is the price of the item the customer wants to buy?: "))
                if target < 0:
                    print("There are no items with negative value. Try again.")
                elif not round(target / currency[1], 2).is_integer():
                    print("That number does not fit with the selected currency. Try inputting an integer or selecting a different currency.")
                else:
                    break
            except:
                print("Invalid input. Try again.")

        while True: # Gets the amount of money that the customer paid for the item
            try:
                paid = float(input("\nHow much money did the customer give you?: "))
                if paid < target:
                    print("The customer has to pay at least as much as the item is worth.")
                elif not round(paid / currency[1], 2).is_integer():
                    print("That number does not fit with the selected currency. Try inputting an integer or selecting a different currency.")
                else:
                    break
            except:
                print("Invalid input. Try again.")
        
        names = []
        values = []
        for i in currency: # Gets the names and values in seperate lists for easier processing
            if currency.index(i) % 2 == 0:
                names.append(i)
            else:
                values.append(i)
        
        difference = round(paid - target, 2)
        pay = []
        for i in reversed(values): # Calculates how much the cashier actually needs to pay
            if difference // i > 0:
                pay.append(f"{int(difference // i)} {names[values.index(i)]}s")
                difference -= (difference // i) * i

        if pay:
            print("\nYou need to give back:") # Displays results to the user
            for i in pay:
                print(i)
        else:
            print("You don't need to give back anything.")     
        
    else:
        print("You haven't selected a country yet. Press '1' in the main menu to select a country.")

def get_country(): # Gets the currency that the user wants to use.
    if load():
        while True:
            print('\nPick the currency you want to use for the coin change problem:')
            for country in load().keys():
                print(f'- {country}')
            choice = input().lower()
            for country in load().keys():
                if choice == country.lower():
                    print("Successfully selected currency.")
                    return country
            print("That's not a valid currency. Try again.")
    print("It looks like there are no countries to select from. Try adding to coins.csv in this format:\ncurrency_name,currency,value,currency,value...")