def get_prop(prop, num=True): # Helper function that defines a specific property of a fighter.
    if not num: # 'num' decides whether the output should be a number. This is helpful for selecting names, which are not numbers. By default, it is true.
        return input(f"What do you want the character's {prop} to be?: ").strip() # Directly return the user's choice.
    try:   
        x = int(input(f"What do you want the character's {prop} to be?: ")) # Return the user's choice if it is in the proper formatting and in the range.
        if x in range(0, 101):
            return x
        else:
            print("That's not in the range (1-100). Try again.")
            return get_prop(prop, num) # Calls the function again in error conditions to avoid redundancy.
    except:
        print("That's not a number. Try again.")
        return get_prop(prop, num)

def get_char(chars, type, other=' character do'): # Helper function that selects a specific character.
    print(f"What{other} you want to {type}?") # Customizable text helps for using in different circumstances.
    for char in chars: # Show the user the list of options.
        print(f"- {char['name']}")
    choice = input().lower()
    for char in chars: # If the user has selected a real character, return it. Otherwise, call the function again.
        if choice == char["name"].lower():
            return char
    print("That's not a valid character. Try again.")
    return get_char(chars, type)

def create_char(chars): # Creates a character with all the necessary values. Starts with a level of 1.
    chars.append({"name": get_prop("name", False).capitalize(), "health": get_prop("health"), "strength": get_prop("strength"), "defense": get_prop("defense"), "speed": get_prop("speed"), "level": 1})
    return chars

def remove_char(chars): # Uses the get_char() function to select a specific character to remove.
    if len(chars) >= 1:
        chars.remove(get_char(chars, "remove"))
    else:
        print("There aren't any characters to remove.")
    return chars

def display(chars): # Displays all the characters in a neat format.
    if chars:
        for char in chars:
            print(f'{char["name"]}:\n\tHealth: {char["health"]}\n\tStrength: {char["strength"]}\n\tDefense: {char["defense"]}\n\tSpeed: {char["speed"]}\n\tLevel: {round((char["level"] - 0.8) / 0.2)}')
    else:
        print("There are no characters to display.")