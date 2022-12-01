
BACKGROUND_COLOR = "#B1DDC6"

from tkinter import*


window = Tk()
window.config(pady=50,padx=50,bg=BACKGROUND_COLOR)

image_cardback = PhotoImage(file=f"./images/card_back.png")
image_front = PhotoImage(file=f"./images/card_front.png")
image_rigth = PhotoImage(file=f"./images/right.png")
image_wrong = PhotoImage(file=f"./images/wrong.png")

canvas = Canvas(width=800,height=526,highlightthickness=0)
canvas.create_image(200,325,image=image_cardback)
canvas.grid(column=0,row=0)


window.mainloop()