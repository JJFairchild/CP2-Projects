#Jonas Fairchild, to-do list

to_do = []

with open("to-do_list/to-do.txt", "r") as file:
    data = file.read() + "\n"
    item = ""
    for i in data:
        if i == "\n":
            to_do.append(item)
            item = ""
        else:
            item += i
