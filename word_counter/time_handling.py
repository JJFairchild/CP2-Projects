import time
from file_handling import count

def check_time(last_count, txt, edit_time): #Checks if the file has been edited.
    if count(txt) != last_count: #If the count isn't the same as it was before, then return the current time. Otherwise, return the time of the last modification.
        return time.time()
    else:
        return edit_time