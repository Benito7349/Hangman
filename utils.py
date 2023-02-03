import unidecode 
from random import randint

def welcome(): # Función que imprime mensaje de bienvenida.
    print("#" * 34)
    print("¡BIENVENIDO AL JUEGO DEL AHORCADO!")
    print("#" * 34)

def read(): # Función para leer .txt de palabras en Español y devolverlas en una lista.
    words_spanish = []
    with open("spanish.txt", "r") as file:
        for line in file:
            word = line.strip() # Elimina Newline caracter "\n".
            word = unidecode.unidecode(word) # Elimina acento de las palabras.
            words_spanish.append(word)
    return words_spanish

def choose_word(words_spanish): # Función para escoger la palabra para jugar.
    list_words_spanish = words_spanish
    number = randint(0,2047)
    word_chosen = list_words_spanish[number]
    return word_chosen

def show_number_letters(word_chosen): # Función que define los espacios de las letras a descubrir.
    number_letters = len(word_chosen)
    spaces = ["_" for i in range(number_letters)]
    return spaces

def print_spaces(spaces): # Imprime lista de espacios vacios y modificados.
    for i in spaces:
        print(i, end=" ")

def letter_gamer(): # Función para ingresar la letra a jugar.
    letter = input("Ingrese una letra: ")
    return letter

def insert_letter(spaces,position, letter_gamer):
    spaces.insert(position,letter_gamer) #Inserta la letra en los espacios.
    spaces.pop(position + 1) #Elimina el espacio reemplazado por la letra.
    return spaces