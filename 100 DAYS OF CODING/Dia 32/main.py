import smtplib
import datetime as dt
import random

email = "ignacio.carrera2000@gmail.com"
password = "sodzqjbqmuwskpxm"


lectura_archivo_txt = open("./frases/frases.txt", mode="r", encoding="utf-8")
lista_frases = lectura_archivo_txt.readlines()

dia_semana = dt.datetime.now().day
print(dia_semana)
