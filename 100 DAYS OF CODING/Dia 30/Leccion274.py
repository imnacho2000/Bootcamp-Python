# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
print(data)

#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def start():
  try:
    word = input("Enter a word: ").upper()
    output_list = [phonetic_dict[letter] for letter in word]
    print(output_list)
  except Exception:
      print("Debe ingresar letras y no un caracter diferente!")
      start()
  else:
      seleccion = input("Desea continuar? Y o N: ").upper()
      if seleccion == "Y":
          start()

start()
