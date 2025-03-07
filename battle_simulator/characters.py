def get_prop(prop, num=True):
    if not num:
        return input(f"What do you want the character's {prop} to be?: ").strip()
    try:   
        x = int(input(f"What do you want the character's {prop} to be?: "))
        if x in range(0, 101):
            return x
        else:
            print("That's not in the range (1-100). Try again.")
            return get_prop(prop, num)
    except:
        print("That's not a number. Try again.")
        return get_prop(prop, num)

def get_char(chars, type, other=' character do'):
    print(f"What{other} you want to {type}?")
    for char in chars:
        print(f"- {char["name"]}")
    choice = input().lower()
    for char in chars:
        if choice == char["name"].lower():
            return char
    print("That's not a valid character. Try again.")
    return get_char(chars, type)

def create_char(chars):
    return chars.append({"name": get_prop("name", False).capitalize(), "health": get_prop("health"), "strength": get_prop("strength"), "defense": get_prop("defense"), "speed": get_prop("speed"), "level": 1})

def remove_char(chars):
    if len(chars) >= 1:
        return chars.remove(get_char(chars, "remove"))
    else:
        print("There aren't any characters to remove.")

def display(chars):
    for char in chars:
        print(f'{char["name"]}:\n\tHealth: {char["health"]}\n\tStrength: {char["strength"]}\n\tDefense: {char["defense"]}\n\tSpeed: {char["speed"]}\n\tLevel: {(char["level"] - 0.8) / 0.2}')