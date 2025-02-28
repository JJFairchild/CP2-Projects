import time

def count(text):
    with open(text, "r") as file:
        word = ""
        words = 0
        for letter in file.read() + "\n":
            if letter in ["\n", " ", "", "\t", None]:
                if word not in ["\n", " ", "", "\t", None]:
                    words += 1
                word = ""
            else:
                word += letter
        return words