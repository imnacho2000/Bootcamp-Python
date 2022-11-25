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
REPS = 8
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global REPS
    window.after_cancel(timer)
    set_mainscreen()
    REPS = 8
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global REPS
    long_break = LONG_BREAK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    work_min = WORK_MIN * 60

    if REPS == 0:
        set_timer_break()
        count_down(long_break)
    elif REPS % 2 == 0:
        set_timer_work()
        count_down(work_min)
        REPS -= 1
    else:
        set_timer_break()
        count_down(short_break)
        REPS -= 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global timer
    minutos = floor(count / 60)
    segundos= count % 60
     
    if segundos == 0:
        if minutos < 10:
            minutos =f"0{minutos}"
        segundos = "00"
    elif segundos < 10: 
        if minutos < 10:
            minutos =f"0{minutos}"
        segundos = f"0{segundos}"
    elif minutos < 10:
        if segundos < 10: 
            segundos = f"0{segundos}"
        minutos =f"0{minutos}"

    canvas.itemconfig(timer_text, text=f"{minutos}:{segundos}")
    if count > 0:
       timer = window.after(1000, count_down,count - 1)
    else:
        check()
        start()
        
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100,pady=100, bg=YELLOW)


canvas = Canvas(width=200,height=223, bg=YELLOW, highlightthickness=0)
tomate_img = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomate_img)
canvas.grid(column=3,row=1)

label_timer = Label(text="Temporizador",font=(FONT_NAME,30,"bold"), fg=GREEN, background=YELLOW)
label_timer.grid(column=3,row=0)
timer_text = canvas.create_text(103, 134, text="00:00", font=(FONT_NAME, 35, "bold"),fill="white")

def set_timer_break():
    label_timer["text"] = "Descanso"
    label_timer["fg"] = PINK
    label_timer["bg"] = YELLOW

def set_timer_work():
    label_timer["text"] = "Trabajando"
    label_timer["fg"] = RED
    label_timer["bg"] = YELLOW


label_done = Label(text="",font=(FONT_NAME,10,"bold"),background=YELLOW,fg="green")
label_done.grid(column=3,row=5)

def set_mainscreen(): 
    label_timer["text"] = "Temporizador"
    label_timer["fg"] = GREEN
    canvas.itemconfig(timer_text, text="00:00")
    label_done["text"] = ""
 

def check():
    global REPS
    if REPS % 2 != 0:
        label_done["text"] = "✔"
    else:
        label_done["text"] = ""

label_start = Button(text="Comenzar",font=(FONT_NAME,10,"bold"),background="white", fg="black", command=start)
label_start.grid(column=2,row=4)

label_restet = Button(text="Resetear",font=(FONT_NAME,10,"bold"),background="white",fg="black", command=reset)
label_restet.grid(column=5,row=4)



window.mainloop()