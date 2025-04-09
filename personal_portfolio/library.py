#Jonas Fairchild, Upgraded Personal Library Program

import os

def add(songs): #Adds a song to the tuple in dictionary form.
    song = input("What song do you want to add to the list?: ")
    writer = input("Who wrote the song?: ")
    studio = input("What studio does was it recorded in?: ")
    location = input("Where is the studio located?: ")
    print("Song successfully added.")
    return tuple(list(songs) + [{"name": song, "writer": writer, "studio": studio, "location": location}])

def remove(songs): #Removes songs from the tuple.
    if songs: #Checks that the songlist isn't empty.
        while True:
            print("What item do you want to remove from the list?\n\nOptions:")
            for item in songs: #Tell user options to remove
                print(item['name'], end = "\n")
            song = input().lower() #Get the item to remove
            for item in songs:
                if item['name'].lower() == song:
                    songList = list(songs)
                    del songList[songs.index(item)] #If item exists, remove it
                    print("Song successfully deleted.")
                    return tuple(songList)
            print("That song isn't on the list.")
            return songs
    else:
        print("There's nothing to remove.")
        return songs

def display(songs): #Displays songs and their information
    if songs: #Checks that songlist isn't empty.
        while True:
            match input("Do you want to display results in a simple or complex format?: ").lower(): #Gets what format the songs should be displayed in
                case "simple":
                    for song in songs:
                        print(f"{song['name']} / {song['writer']}\n") #Displays every song's information in a simple format.
                    break
                case "complex":
                    for i, song in enumerate(songs, start = 1):
                        print(f"{i}. {song['name']}, by {song['writer']}, recorded in {song['studio']}, {song['location']}.\n") #Displays every song's information in a complex format.
                    break
                case _:
                    print("Invalid input. Try again.")
    else:
        print("The song list is empty.")

def search(songs): #Searches through the list of songs.
    if songs: #Checks that the songlist isn't empty.
        searchType = ''
        while not searchType: #While not valid input
            searchResults = []
            match input("Do you want to search by title, artist, studio, or location?: ").lower(): #Gets search type and assigns it
                case "title":
                    searchType = 'name'
                case "artist":
                    searchType = 'writer'
                case "studio":
                    searchType = 'studio'
                case "location":
                    searchType = 'location'
                case _:
                    print("Invalid Input. Try again.")
        search = input("What is your search?: ").lower() #Gets the search
        for song in songs:
            if search in song[searchType].lower(): #Adds all results to a list
                searchResults += [song]
        print("Search results:")
        if searchResults != []:
            display(searchResults) #Prints all the search results
        else:
            print("None")
    else:
        print("There's nothing to search for.")

def main(): #Main UI for the program.
    songs = () #Assigns the songlist in tuple form
    while True:
        try:
            os.system("cls")
            choice = int(input("What do you want to do?\n1. Search the song list\n2. Add an item to the list\n3. Remove an item from the list\n4. Display the list\n5. Exit the program\n")) #Gets the user's choice and performs it
            if choice == 1:
                search(songs)
            elif choice == 2:
                songs = add(songs)
            elif choice == 3:
                songs = remove(songs)
            elif choice == 4:
                display(songs)
            elif choice == 5:
                break
            input("Done reading?: ")
        except:
            print("Invalid input. Try again.")
            input("Done reading?: ")