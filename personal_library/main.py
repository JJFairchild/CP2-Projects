#Stores all items in a set or tuple (done)
#Function to add a new item (done)
#Function to search the items
#Function to remove an item
#Function to display ALL items
#Function that runs the code (displays the menu options inside and calls the functions inside of a while True loop)

songs = (['A', 'A'], ['B', 'B'])

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
                del songlist lkzrhglkhsbv
        else:
            print("That song isn't on the list.")
            return songs
                
            


remove()