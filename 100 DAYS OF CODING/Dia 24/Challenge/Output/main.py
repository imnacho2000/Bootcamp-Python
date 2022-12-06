

with open("../Input/Names/invited_names.txt", mode="r") as file_names:
   for name in file_names:
       with open("../input/Letters/starting_letter.txt", mode="r+") as file_replace:
            nombre = name.strip()
            archivo_guardar = file_replace.read().replace("[name]",nombre)
            with open(f"./ReadyToSend/invitacion_para_{nombre}",mode ="w") as f:
                f.write(archivo_guardar)

