import time
from file_handling import count

def check_time(last_count):
    try: #Gets the time that the text was last edited
        with open("word_counter/save_time.txt", "r") as file:
            edit_time = float(file.read())
    except:
        edit_time = time.time()
    
    if last_count != count(): #If the wordcount has been updated, write the current time to the save_time file.
        with open("word_counter/save_time.txt", "w") as file:
            file.write(str(time.time()))
    
    print(f"The wordcount of the text was updated {int(time.time() - edit_time)} seconds ago.")