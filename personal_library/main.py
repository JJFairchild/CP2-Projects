#Jonas Fairchild, Personal Library Program

import os

def add(songs):
    song = input("What song do you want to add to the list?: ")
    writer = input("Who wrote the song?: ")
    return tuple(list(songs) + [[song, writer]])

def remove(songs):
    if songs != ():
        while True:
            print("What item do you want to remove from the list?\n\nOptions:")
            for item in songs:
                print(item[0], end = "\n")
            song = input().lower()
            for item in songs:
                if item[0].lower() == song:
                    songList = list(songs)
                    del songList[songs.index(item)]
                    return tuple(songList)
            else:
                print("That song isn't on the list.")
                return songs
    else:
        print("There's nothing to remove.")
        return songs

def display(songs):
    if songs != ():
        count = 1
        for song in songs:
            print(f"{count}. {song[0]}, by {song[1]}.\n")
            count += 1
    else:
        print("The song list is empty.")

def search(songs):
    if songs != ():
        searchResults = []
        if input("Do you want to search by artist or by title?: ").lower()[0] == "a":
            searchType = 1
        else:
            searchType = 0
        search = input("What is your search?: ").lower()
        for song in songs:
            if search in song[searchType].lower():
                searchResults += [song]
        print("Search results:")
        if searchResults != []:
            display(searchResults)
        else:
            print("None")
    else:
        print("There's nothing to search for.")

def main():
    songs = ()
    while True:
        try:
            os.system("cls")
            choice = int(input("What do you want to do?\n1. Search the song list\n2. Add an item to the list\n3. Remove an item from the list\n4. Display the list\n5. Exit the program\n"))
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
        
main()