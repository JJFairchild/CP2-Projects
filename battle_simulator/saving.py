import csv

def load(): # Creates a list of dictionaries containing every fighter.
    chars = []
    with open("battle_simulator/characters.csv", "r") as file:
        csv_reader = csv.reader(file)
        for char in csv_reader: # Find every character and make a new dictionary with all the proper information.
            chars.append({"name": char[0], "health": int(char[1]), "strength": int(char[2]), "defense": int(char[3]), "speed": int(char[4]), "level": float(char[5])})
    return chars

def save(chars): # Saves all the characters to the csv file.
    with open("battle_simulator/characters.csv", "w", newline='') as file:
        csv_writer = csv.writer(file)
        for char in chars: # Give every character a line in the file, with all the proper values.
            csv_writer.writerow(char.values())