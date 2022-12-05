
BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import random

flip = None
resultado = None

# ---------------------------- FLIP ------------------------------- # 

def flip_correct():
    global resultado
    canvas.itemconfig(card_front,image=image_cardback)
    canvas.itemconfig(ingles_text,text="Español",fill= "white")
    canvas.itemconfig(aleatorio,text=f"{resultado['ESPAÑOL']}",fill= "white")

def correct_answer():
    dictionary_data_.remove(resultado)
    pd = pandas.DataFrame(dictionary_data_)
    pd.to_csv('./data/words_to_learn.csv', index=False)
    random_word_english()



# ---------------------------- RANDOM WORDS GENERATOR ------------------------------- # 

try:
    excel_palabras = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    print('No existe un archivo para aprender')
    pd = pandas.DataFrame(columns = ['INGLES','ESPAÑOL'])
    pd.to_csv('./data/words_to_learn.csv')
    excel_palabras = pandas.read_csv("./data/Angela yu Flash Cards ingles-español - Hoja 1.csv")
    dictionary_data_ = excel_palabras.to_dict(orient="records")
else:
    dictionary_data_ = excel_palabras.to_dict(orient="records")


resultado = random.choice(dictionary_data_) 

def random_word_english():
    global resultado
    resultado = random.choice(dictionary_data_) 
    canvas.itemconfig(card_front,image=image_front)
    canvas.itemconfig(ingles_text,text="Ingles",fill= "black")
    canvas.itemconfig(aleatorio,text=f"{resultado['INGLES']}",fill= "black")
    window.after(3000,flip_correct)

# ---------------------------- UI INTERFACE ------------------------------- # 

window = Tk()
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

image_cardback = PhotoImage(file=f"./images/card_back.png")
image_front = PhotoImage(file=f"./images/card_front.png")
image_rigth = PhotoImage(file=f"./images/right.png")
image_wrong = PhotoImage(file=f"./images/wrong.png")

canvas = Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
card_front = canvas.create_image(400,263,image=image_front)
ingles_text = canvas.create_text(400,150,text="Ingles",font=("Ariel",40,"italic"))

aleatorio = canvas.create_text(400,263,text=f"{resultado['INGLES']}",font=("Ariel",60,"bold"))

canvas.grid(column=0,row=0,columnspan=2)


canvas_rigth = Button(image=image_rigth, highlightthickness=0,bg=BACKGROUND_COLOR,command=correct_answer)
canvas_rigth.grid(column=1,row=1)

canvas_wrong = Button(image=image_wrong, highlightthickness=0,bg=BACKGROUND_COLOR,command=random_word_english)
canvas_wrong.grid(column=0,row=1)

window.after(3000,flip_correct)
window.mainloop()