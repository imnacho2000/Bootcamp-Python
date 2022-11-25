from tkinter import *
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generar_contraseña():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_choice = [random.choice(letters) for a in range(random.randint(8, 10))]
    symbols_choice = [random.choice(symbols) for a in range(random.randint(2, 4))]
    numbers_choice = [random.choice(numbers) for a in range(random.randint(2, 4))]

    password_list = letters_choice + symbols_choice + numbers_choice


    password = "".join(password_list)
    
    print(password)
    label_text_password_entry.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def crear_contrasena():
    website = label_text_webist_entry.get()
    email = label_text_email_entry.get()
    password = label_text_password_entry.get()

    if password == "" or email == "" or website == "":
        messagebox.showerror(title="Informacion", message="¡Asegurese que los campos esten completos!")
    else:
        is_ok = messagebox.askyesno(title="Atencion",message=f"Estos son los datos ingresados: \n Web: {website} \n Email: {email}  \n Passsword: {password}  \n ¿Seguro desea guardarla? ")
        if is_ok:
            f = open(f"C:\\Users\\ignacio.carrera\\Desktop\\contraseñas.txt","a+")
            f.write(f'Website: {website} | Email: {email} | Password: {password} \n')
            f.close()
            label_text_webist_entry.delete(0,END)
            label_text_password_entry.delete(0,END)
        else:
            label_text_password_entry.delete(0,END)
        messagebox.showinfo(title="Exito",message="¡Informacion guardada con exito!")
# ---------------------------- UI SETUP ------------------------------- # 
window = Tk()
window.config(padx=20, pady=20, bg = "white")
window.title("Password Manager")

image_logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200,height=200, highlightthickness=0, bg="white")
canvas.create_image(100,100, image=image_logo)
canvas.grid(column=1,row=0)
 
 # Fuente # 
font = ("Arial",8,"bold")


# ---------------------------- WEBSITE ------------------------------- # 
label_text_webiste = Label(text="Website:", font=font, bg="white")
label_text_webiste.grid(column=0,row=1)

label_text_webist_entry = Entry(width=36)
label_text_webist_entry.grid(column=1,row=1,columnspan=2)

# ---------------------------- EMAIL------------------------------- # 

label_text_email = Label(text="Email/Username:", font=font, bg="white")
label_text_email.grid(column=0,row=2)

label_text_email_entry = Entry(width=36)
label_text_email_entry.grid(column=1,row=2,columnspan=2)
label_text_email_entry.insert(0,"ignaciocarrera2000@hotmail.com")

# ---------------------------- PASSWORD ------------------------------- # 

label_text_password = Label(text="Password:", font=font, bg="white")
label_text_password.grid(column=0,row=3)

label_text_password_entry = Entry(width=24)
label_text_password_entry.grid(column=1,row=3)


label_button_generate = Button(text="Generar Contraseña",fg="white",bg="black", command=generar_contraseña)
label_button_generate.grid(column=2,row=3)



# ---------------------------- ADD ------------------------------- # 

label_button_generate = Button(text="Add", font=font, width=36,fg="white",bg="black", command=crear_contrasena)
label_button_generate.grid(column=1,row=4,columnspan=2)

   







window.mainloop()
