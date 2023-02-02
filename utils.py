from random import randint

def read():
    words_spanish = []
    with open("spanish.txt", "r") as file:
        for line in file:
            words_spanish.append(line)
        return words_spanish

        