from tkinter import *

window = Tk()
window.title("Conversor de Millas a Km")
window.minsize(width=200,height=117)


#Etiquetas
tupla_fuente = ("Arial",12)
label_es_igual_a = Label(text="es igual a", font=tupla_fuente)
label_es_igual_a.grid(column=0,row=1)

label_km = Label(text="Km", font=tupla_fuente)
label_km.grid(column=4,row=1)

#Botones
def boton_clickeado():
    millas = float(entrada_millas.get())
    label_resultado['text']=str(millas * 1.609)

boton = Button(text="Calcular", command=boton_clickeado)
boton.grid(column=3,row=2)


label_resultado = Label(text="0", font=tupla_fuente)
label_resultado.grid(column=3,row=1)

#Entradas
entrada_millas = Entry(width=10)
entrada_millas.grid(column=3,row=0)


#Para que la pantalla no se salga!
window.mainloop()