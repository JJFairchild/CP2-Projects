#Stores all items in a set or tuple (done)
#Function to add a new item (done)
#Function to search the items
#Function to remove an item (done)
#Function to display ALL items (done)
#Function that runs the code (displays the menu options inside and calls the functions inside of a while True loop)

songs = (['A', 'A'], ['B', 'B'])
import os

def add():
    song = input("What song do you want to add to the list?: ")
    writer = input("Who wrote the song?: ")
    return tuple(list(songs) + [[song, writer]])

def remove():
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
                
def display(list=songs):
    count = 1
    for song in list:
        print(f"{count}. {song[0]}, by {song[1]}.\n")
        count += 1

def search():
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
    if searchResults:
        display(searchResults)
    else:
        print("None")

def main():
    while True:
        os.system("cls")
        choice = input("What do you want to do?\n1. Search the song list\n 2. Add an item to the list\n3. Remove an item from the list\n4. Display the list\n5. Exit the program\n")
        if choice == 1:
            search()
        elif choice == 2:
            songs = add()
        elif choice == 3:
            songs = remove()
        elif choice == 4:
            display()
        elif choice == 5:
            break
        input("Done reading?: ")