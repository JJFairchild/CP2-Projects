from file_handling import load

def solve(country):
    if country:
        currency = load()[country]
        
    else:
        print("You haven't selected a country yet. Press '1' in the main menu to select a country.")

def get_country():
    if load():
        while True:
            print('Pick the currency you want to use for the coin change problem:')
            for country in load().keys():
                print(f'- {country}')
            choice = input().lower()
            for country in load().keys():
                if choice == country.lower():
                    return country
            print("That's not a valid currency. Try again.")
    print("It looks like there are no countries to select from. Try adding to coins.csv in this format:\ncurrency_name,currency,value,currency,value...")
    return None