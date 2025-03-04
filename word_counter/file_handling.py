import time

def count(text): #Counts the number of words in the document.
    with open(text, "r") as file:
        word = ""
        words = 0
        for letter in file.read() + "\n": #Looks through the document until it has what looks like a word, then adds 1 to the word count.
            if letter in ["\n", " ", "", "\t", None]:
                if word not in ["\n", " ", "", "\t", None]:
                    words += 1
                word = ""
            else:
                word += letter
        return words