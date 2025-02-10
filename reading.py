import csv

users = dict()

with open('Class CSV sample - Sheet1.csv', 'r') as file:
    csv_reader = csv.reader(file)

print(users)