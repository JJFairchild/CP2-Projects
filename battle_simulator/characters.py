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

def get_char(chars, type):
    print(f"What character do you want to {type}?")
    for char in chars:
        print(f"- {char["name"]}")
    choice = input()
    for char in chars:
        if choice == char["name"]:
            return char
    print("That's not a valid character. Try again.")
    get_char(chars, type)

def create_char():
    return {"name": get_prop("name", False).capitalize(), "health": get_prop("health"), "strength": get_prop("strength"), "defense": get_prop("defense"), "speed": get_prop("speed")}

def edit_char(chars):
    get_char(chars, "edit")
    match input("What do you want to do?\n"):
        case "1":
            pass
    