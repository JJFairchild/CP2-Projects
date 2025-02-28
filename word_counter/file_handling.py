def count():
    with open("word_counter/words.txt", "r") as file:
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

print(count())

if __name__ == "main":
    print(count())