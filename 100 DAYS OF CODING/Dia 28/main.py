from tkinter import *
from math import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    canvas.itemconfig(timer_text, text=25)
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    count_down(5 * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    minutos = floor(count / 60)
    segundos= count % 60
    if segundos == 0:
        canvas.itemconfig(timer_text, text=f"{minutos}:00")
    canvas.itemconfig(timer_text, text=f"{minutos}:{segundos}")
    if count > 0:
        window.after(1000, count_down,count - 1)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100,pady=100, bg=YELLOW)


canvas = Canvas(width=200,height=223, bg=YELLOW, highlightthickness=0)
tomate_img = PhotoImage(file="tomato.png")

label_timer = Label(text="Timer",font=(FONT_NAME,30,"bold"), fg=GREEN, background=YELLOW)
label_timer.grid(column=3,row=0)
canvas.create_image(103, 112, image=tomate_img)
timer_text = canvas.create_text(103, 134, text="00:00", font=(FONT_NAME, 35, "bold"),fill="white")
canvas.grid(column=3,row=1)


label_start = Button(text="Comenzar",font=(FONT_NAME,10,"bold"),background="white", fg="black", command=start)
label_start.grid(column=2,row=4)

label_restet = Button(text="Resetear",font=(FONT_NAME,10,"bold"),background="white",fg="black", command=reset)
label_restet.grid(column=5,row=4)

label_done = Label(text="✔",font=(FONT_NAME,10,"bold"),background=YELLOW,fg="green")
label_done.grid(column=3,row=5)

window.mainloop()