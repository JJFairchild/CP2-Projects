import csv

def load(): #Imports the contents of coins.csv as a dictionary that the other files can work with.
    denominations = {}
    with open("coin_problem/coins.csv", 'r') as file:
        csv_reader = csv.reader(file)
        for line in csv_reader:
            denominations.update({line[0]: []})
            for i in line:
                if line.index(i) != 0:
                    try:
                        denominations[line[0]].append(float(i))
                    except:
                        denominations[line[0]].append(i)
    return denominations