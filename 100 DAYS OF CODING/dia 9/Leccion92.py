student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {
}

for n in student_scores:
    valor = student_scores[n]
    if(valor <= 70):
        student_grades[n] = "Repite"
    elif((valor >=71 ) and (valor <=80)):
        student_grades[n] = "Aceptable"
    elif((valor >= 81) and (valor <= 90 )):
        student_grades[n] = "Excede lo aceptable"
    else:
        student_grades[n] = "Sobresaliente"
print(student_grades)
