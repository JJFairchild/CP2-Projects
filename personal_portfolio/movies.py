#Jonas Fairchild, movie recommender

import csv
import os
import copy

movies = [] #Opens the movie file and gives it a variable in the form of a dictionary for easy access.
with open('personal_portfolio/movie_list.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for i in csv_reader:
        movies.append({"title": i[0], "director": i[1], "genre": i[2], "rating": i[3], "length": i[4], "note_actors": i[5]})

def display_movies(movies): #Displays a given list of movies in an easy-to-read format.
    for movie in movies:
        print(f'Title: {movie["title"]}\nDirector: {movie["director"]}\nGenre: {movie["genre"]}\nRating: {movie["rating"]}\nLength: {movie["length"]} minutes\nNotable actors: {movie["note_actors"]}\n')

def search_movies(): #Searches the list of movies for specific movies.
    searches = []
    while True: #Gets the number of search conditions to use
        try:
            count = int(input("How many search conditions do you want to use?: "))
            if count > 0 and count < 7:
                break
            else:
                print("Invalid input. Try again.")
        except:
            print("That's not a number. Try again.")

    for i in range(count): #Gets the categories of the search and the search itself for each category
        match input("What category do you want to search for? (title, director, genre, rating, length, actors): ").lower():
            case "title":
                searches.append(["title", input("What will you search for?: ")])
            case "director":
                searches.append(["director", input("What will you search for?: ")])
            case "genre":
                searches.append(["genre", input("What will you search for?: ")])
            case "rating":
                searches.append(["rating", input("What will you search for?: ")])
            case "length":
                searches.append(["length", input("What will you search for?: ")])
            case "actors":
                searches.append(["note_actors", input("What will you search for?: ")])
            case _:
                print("Invalid input.")
    
    movie_copy = copy.deepcopy(movies)
    for movie in movies: #Searches a copy of the list of movies and removes anything that doesn't match, displays the results at the end
        for search in searches:
            if not search[1] in movie[search[0]]:
                try:
                    movie_copy.remove(movie)
                except:
                    pass
    print("Search results:\n")
    display_movies(movie_copy)

def main(): #Main UI function, branches to the different parts of the program.
    while True:
        os.system("cls")
        match input("What do you want to do?\n1. Search the movie list\n2. Print the movie list\n3. Exit\n"):
            case "1":
                search_movies()
            case "2":
                display_movies(movies)
            case "3":
                break
            case _:
                print("Invalid input. Try again.")
        input("Done reading?: ")