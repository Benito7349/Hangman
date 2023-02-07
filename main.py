import utils

def run():
  utils.welcome()
  words_spanish = utils.read()
  word_chosen = utils.choose_word(words_spanish)
  spaces = utils.show_number_letters(word_chosen)
  utils.print_spaces(spaces)
  print()
  print()

  intentos = 1
  msj = "¡¡Tu estas ahorcado!!"
  msjs_final = ["¡GANASTE!","¡PERDISTE! :(","¡JUEGO TERMINADO!"]
  multiplicator = [len(msjs_final[0]),len(msjs_final[1]),len(msjs_final[2])]
  while intentos < 8:
    letter_gamer = utils.letter_gamer()
    final = ""
    if letter_gamer in word_chosen:
      if word_chosen.count(letter_gamer) == 1:
        position = word_chosen.find(letter_gamer) #Encuentra 1ra posición de la letra ingresada.
        utils.insert_letter(spaces,position,letter_gamer)
        utils.print_spaces(spaces)
        word_in_construction = utils.word_in_construction(spaces)
        if word_in_construction == word_chosen:
          final = "SI"
          break
        print()
      elif word_chosen.count(letter_gamer) == 2:
        position = word_chosen.find(letter_gamer) 
        utils.insert_letter(spaces,position,letter_gamer)
        position = word_chosen.rfind(letter_gamer) #Encuentra última posición de la letra ingresada.
        utils.insert_letter(spaces,position,letter_gamer)
        utils.print_spaces(spaces)
        word_in_construction = utils.word_in_construction(spaces)
        if word_in_construction == word_chosen:
          final = "SI"
          break
        print()
      elif word_chosen.count(letter_gamer) == 3:
        position = word_chosen.find(letter_gamer)
        utils.insert_letter(spaces,position,letter_gamer)
        word_chosen_cut = word_chosen.replace(letter_gamer,'',1)#Encuentra segunda posición
        position = word_chosen_cut.find(letter_gamer) + 1       #de la letra ingresada.
        utils.insert_letter(spaces,position,letter_gamer)
        position = word_chosen.rfind(letter_gamer) #Encuentra última posición de la letra ingresada.
        utils.insert_letter(spaces,position,letter_gamer)
        utils.print_spaces(spaces)
        word_in_construction = utils.word_in_construction(spaces)
        if word_in_construction == word_chosen:
          final = "SI"
          break
        print()
    else:
      print(msj[0:intentos * 3])
      utils.print_spaces(spaces)
      intentos += 1
      print()
      
  print()
  if final == "SI":
    utils.farewell(msjs_final[0],multiplicator[0])
  else:
    utils.farewell(msjs_final[1],multiplicator[1])
    print()
    print(f"La palabra era: {word_chosen}")
  print()
  utils.farewell(msjs_final[2],multiplicator[2])
 
if __name__ == '__main__': #Es para ejecutar el archivo main.py desde la consola.
  run()