from tkinter import *
from tkinter import messagebox
import random
import json




# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generar_contraseña():
    label_text_password_entry.delete(0,END)
    
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
    dictionary_data = { website: {
      "mail" : email,
      "password" : password
    }}
    if password == "" or email == "" or website == "":
        messagebox.showerror(title="Informacion", message="¡Asegurese que los campos esten completos!")
    else:
        try:
            f = open(f"C:\\Users\\ignacio.carrera\\Desktop\\contraseñas.json","r")
        except FileNotFoundError:
            print('No se encontro el archivo, creandolo y cargando informacion')
            f = open(f"C:\\Users\\ignacio.carrera\\Desktop\\contraseñas.json","w")
            json.dump(dictionary_data,f, indent=4)
        else:
            # leo datao vieja
            jason = json.load(f)
            # Actualizo la vieja con la nueva
            jason.update(dictionary_data)
            #Lo cargo
            f = open(f"C:\\Users\\ignacio.carrera\\Desktop\\contraseñas.json","w")
            json.dump(jason,f, indent=4)
        finally:
            label_text_webist_entry.delete(0,END)
            label_text_password_entry.delete(0,END)
            messagebox.showinfo(title="Exito",message="¡Informacion guardada con exito!")


# ---------------------------- SEARCH ------------------------------- #
def buscar_contraseña():
    web = label_text_webist_entry.get()
    if web == "":
        messagebox.showerror(title="Informacion", message="¡Asegurese que los campos esten completos!")
    else:
        contraseña = ""
        username = ""
        try:
            f = open(f"C:\\Users\\ignacio.carrera\\Desktop\\contraseñas.json","r")
        except FileNotFoundError:
            messagebox.showerror(title="Informacion", message="¡Archivo no encontrado!")
        else:
            jason = json.load(f)
            if web in jason: 
                contraseña = jason[web]['password']
                username = jason[web]['mail']
                messagebox.showinfo(title="Informacion",message=f"Website: {web} \nEmail/Username: {username} \nContraseña: {contraseña}")
            else:
                messagebox.showerror(title="Informacion", message="¡Web no encontrada!") 
# ---------------------------- UI SETUP ------------------------------- # 


window = Tk()
window.config(padx=20, pady=20, bg = "white")
window.title("Password Manager")

image_logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200,height=200, highlightthickness=0, bg="white")
canvas.create_image(100,100, image=image_logo)
canvas.grid(column=1,row=0)
window.iconphoto(False,image_logo)
 
 # Fuente # 
font = ("Arial",8,"bold")


# ---------------------------- WEBSITE ------------------------------- # 
label_text_webiste = Label(text="Website:", font=font, bg="white")
label_text_webiste.grid(column=0,row=1)

label_boton_buscar = Button(text="Buscar",fg="white",bg="black", command=buscar_contraseña)
label_boton_buscar.grid(column=2,row=1)

label_text_webist_entry = Entry(width=36)
label_text_webist_entry.grid(column=1,row=1)

# ---------------------------- EMAIL------------------------------- # 

label_text_email = Label(text="Email/Username:", font=font, bg="white")
label_text_email.grid(column=0,row=2)

label_text_email_entry = Entry(width=36)
label_text_email_entry.grid(column=1,row=2)
label_text_email_entry.insert(0,"ignaciocarrera2000@hotmail.com")

# ---------------------------- PASSWORD ------------------------------- # 

label_text_password = Label(text="Password:", font=font, bg="white")
label_text_password.grid(column=0,row=3)

label_text_password_entry = Entry(width=24)
label_text_password_entry.grid(column=1,row=3)


label_button_generate = Button(text="Generar Contraseña",fg="white",bg="black", command=generar_contraseña)
label_button_generate.grid(column=2,row=3,columnspan=2)



# ---------------------------- ADD ------------------------------- # 

label_button_generate = Button(text="Guardar", font=font, width=36,fg="white",bg="black", command=crear_contrasena)
label_button_generate.grid(column=1,row=4)

   







window.mainloop()
