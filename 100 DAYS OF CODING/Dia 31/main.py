
BACKGROUND_COLOR = "#B1DDC6"

from tkinter import*


window = Tk()
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

image_cardback = PhotoImage(file=f"./images/card_back.png")
image_front = PhotoImage(file=f"./images/card_front.png")
image_rigth = PhotoImage(file=f"./images/right.png")
image_wrong = PhotoImage(file=f"./images/wrong.png")

canvas = Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
canvas.create_image(400,263,image=image_front)
canvas.create_text(400,150,text="Hola",font=("Ariel",40,"italic"))
canvas.create_text(400,263,text="Hola",font=("Ariel",60,"bold"))
canvas.grid(column=0,row=0,columnspan=2)


canvas_rigth = Button(image=image_rigth, highlightthickness=0,bg=BACKGROUND_COLOR)
canvas_rigth.grid(column=1,row=1)

canvas_wrong = Button(image=image_wrong, highlightthickness=0,bg=BACKGROUND_COLOR)
canvas_wrong.grid(column=0,row=1)


window.mainloop()