import time
from file_handling import count

def check_time(last_count, txt, edit_time):
    if count(txt) != last_count:
        return time.time()
    else:
        return edit_time