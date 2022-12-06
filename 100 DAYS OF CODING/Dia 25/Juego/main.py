from turtle import Screen, Turtle
import pandas

screen = Screen()
screen.setup(width=725, height=491)
screen.title("Adivina el estado")
image = "juego/blank.gif"
screen.addshape(image)

score = 0

mapa = Turtle()
mapa.shape(image)

correcto = Turtle()
correcto.penup()
correcto.hideturtle()


estados = pandas.read_csv("juego/50_states.csv")


lista_estados = estados["state"].to_list()
lista_correctos = []
print(lista_estados)
respuesta = screen.textinput(
    title=f"Adivina el estado", prompt="Escriba un nombre de estado").title()

while len(lista_correctos) < 50:
    if respuesta == "Exit" or respuesta == "Cancel":
        lista_faltantes = [
            n for n in lista_estados if n not in lista_correctos]
        dict_estados = {
            "Estados faltantes": lista_faltantes
        }
        datos_score = pandas.DataFrame(dict_estados)
        datos_score.to_csv("Juego/scoreboard.csv")
        break
    if (respuesta in lista_estados and respuesta not in lista_correctos):
        lista_correctos.append(respuesta)
        estado = estados[estados["state"] == respuesta]
        x = float(estado.x)
        y = float(estado.y)
        correcto.goto(x=x, y=y)
        correcto.write(f"{respuesta}", align="center",
                       font=('arial', 10, 'normal'))
    if len(lista_correctos) == 50:
        screen.bye()
    else:
        respuesta = screen.textinput(
            title=f"{len(lista_correctos)}/50", prompt="Escriba otro nombre de estado").title()


screen.mainloop()
