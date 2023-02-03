import utils

def run():
  utils.welcome()
  words_spanish = utils.read()
  word_chosen = utils.choose_word(words_spanish)
  spaces = utils.show_number_letters(word_chosen)
  utils.print_spaces(spaces)
  print()
  print()

  letter_gamer = utils.letter_gamer()

  if letter_gamer in word_chosen:
    if word_chosen.count(letter_gamer) == 1:
      position = word_chosen.find(letter_gamer) #Encuentra 1ra posición de la letra ingresada.
      utils.insert_letter(spaces,position,letter_gamer)
      utils.print_spaces(spaces)
    elif word_chosen.count(letter_gamer) == 2:
      position = word_chosen.find(letter_gamer) #Encuentra última posición de la letra ingresada.
      utils.insert_letter(spaces,position,letter_gamer)
      position = word_chosen.rfind(letter_gamer)
      utils.insert_letter(spaces,position,letter_gamer)
      utils.print_spaces(spaces)
  else:
    print("NO")
  print()

  print(word_chosen)
  print(letter_gamer)
 
if __name__ == '__main__': #Es para ejecutar el archivo main.py desde la consola.
  run()