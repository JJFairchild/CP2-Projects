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
    return chars.append({"name": get_prop("name", False).capitalize(), "health": get_prop("health"), "strength": get_prop("strength"), "defense": get_prop("defense"), "speed": get_prop("speed")})

def edit_char(chars):
    if len(chars) >= 1:
        char = get_char(chars, "edit")
        while True:
            match input("What trait do you want to edit?\n- Name\n- Health\n- Strength\n- Defense\n- Speed\n").lower():
                case "name":
                    char["name"] = get_prop("new name", False).capitalize()
                    break
                case "health":
                    char["health"] = get_prop("new health")
                    break
                case "strength":
                    char["strength"] = get_prop("new strength")
                    break
                case "defense":
                    char["defense"] = get_prop("new defense")
                    break
                case "speed":
                    char["speed"] = get_prop("new speed")
                    break
                case _:
                    print("That's not a valid option. Options: name, health, strength, defense, speed. Try again.")
        return chars
    else:
        print("There aren't any characters to edit.")

def remove_char(chars):
    if len(chars) >= 1:
        return chars.remove(get_char(chars, "remove"))
    else:
        print("There aren't any characters to edit.")