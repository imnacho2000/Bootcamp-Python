import random
import pandas
# list = ["141 y 45","141 y 46"]
# dict_tocompress = {"calles":list} 
# print(dict_tocompress)

names = ["Alex","Juliet","Cath","Miqueas"]
student_scores = {
    "student":names,
    "score":[80,50,70,65]
}

student_data_frame = pandas.DataFrame(student_scores)
#iterrows nos permite recorrer las filas de las columnas 
for (index,row) in student_data_frame.iterrows():
    print(row.score)
# passed_students = {students:scores for(students,scores) in student_scores.items() if scores > 80}
# print(passed_students)