import utils

def run():
  print(utils.welcome())
  words_spanish = utils.read()
  word_chosen = utils.choose_word(words_spanish)
  spaces = utils.show_number_letters(word_chosen)

  for i in spaces:
    print(i, end=" ")
  print()
  print()

  letter_gamer = utils.letter_gamer()

  if letter_gamer in word_chosen:
    print("OK")
  else:
    print("Bad")

  print(word_chosen)
  print(letter_gamer)
 
if __name__ == '__main__': #Es para ejecutar el archivo main.py desde la consola.
  run()