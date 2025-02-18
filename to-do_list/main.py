#Jonas Fairchild, to-do list

to_do = []

with open("to-do_list/to-do.txt", "r") as file:
    data = file.read()
    print(data)