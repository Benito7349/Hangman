import unidecode 

def read():
    words_spanish = []
    with open("spanish.txt", "r") as file:
        for line in file:
            word = line.strip() # Elimina Newline caracter "\n".
            word = unidecode.unidecode(word) # Elimina acento de las palabras.
            words_spanish.append(word)
    return words_spanish
