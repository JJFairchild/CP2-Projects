#Jonas Fairchild, movie recommender

#User is able to choose at least 2 filters for the program to search through
#User can get recommendations based on genre, directors, length and/or actors 
#User is able to print the whole list

import csv
import os

movies = []
with open('movie_recommender\Movies list.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for i in csv_reader:
        movies.append({"title": i[0], "director": i[1], "genre": i[2], "rating": i[3], "length": i[4], "note_actors": i[5]})

def display_movies(movies):
    for movie in movies:
        print(f'Title: {movie["title"]}\nDirector: {movie["director"]}\nGenre: {movie["genre"]}\nRating: {movie["rating"]}\nLength: {movie["length"]} minutes\nNotable actors: {movie["note_actors"]}\n')

def search_movies(): #Searches the list of movies for specific movies.
    search_cats = set({})
    while True: #Gets the number of search conditions to use
        try:
            count = int(input("How many search conditions do you want to use?: "))
            if count > 0 and count < 7:
                break
            else:
                print("Invalid input. Try again.")
        except:
            print("That's not a number. Try again.")

    for i in range(count): #Gets the categories of the search
        match input("What category do you want to search for? (title, director, genre, rating, length, actors): ").lower():
            case "title":
                search_cats.add("title")
            case "director":
                search_cats.add("director")
            case "genre":
                search_cats.add("genre")
            case "rating":
                search_cats.add("rating")
            case "length":
                search_cats.add("length")
            case "actors":
                search_cats.add("note_actors")
            case _:
                print("Invalid input.")
    
    


def main():
    while True:
        os.system("cls")
        match input("What do you want to do?\n1. Get a movie reccomendation\n2. Search the movie list\n3. Print the movie list\n4. Exit\n"):
            case "1":
                pass
            case "2":
                search_movies()
            case "3":
                display_movies(movies)
            case "4":
                break
            case _:
                print("Invalid input. Try again.")
        input("Done reading?: ")

main()