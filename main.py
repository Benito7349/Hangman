from random import randint
import utils

def run():
    list_words_spanish = list(utils.read())
    number = randint(0,2047)
    word_chosen = list_words_spanish[number]
    #print(list_words_spanish)
    print(word_chosen)
    print(len(word_chosen))
 
if __name__ == '__main__': #Es para ejecutar el archivo main.py desde la consola.
  run()