import csv

def load():
    denominations = []
    with open("coin_problem/coins.csv", 'r') as file:
        csv_reader = csv.reader(file)
        for line in csv_reader:
            zone = []
            for i in line:
                try:
                    zone.append(float(i))
                except:
                    zone.append(i)
            denominations.append(zone)
    return denominations