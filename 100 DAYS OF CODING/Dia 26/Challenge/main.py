student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

nato = pandas.read_csv("Nato.csv")
dict_letters = {rows.letter:rows.code for(index,rows) in nato.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

#Yo lo hice de esta forma en caso de que el usuario ingresara el nombre completo
# respuesta = input("Ingrese su nombre: ").upper()
# lista = respuesta
# lista_respuesta = [n for n in lista if n != " "]
# lista_final = [dict_letters[n] for n in lista_respuesta if n in dict_letters]
# print(f"Aqui esta su nombre en formato Nato:\n{lista_final}")

# respuesta = input("Ingrese su nombre: ").upper()
# lista_final = [dict_letters[n] for n in respuesta if n in dict_letters]
# print(lista_final)