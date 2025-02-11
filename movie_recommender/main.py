#Jonas Fairchild, movie recommender

import csv

with open('movie_recommender\Movies list.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for i in csv_reader:
        pass