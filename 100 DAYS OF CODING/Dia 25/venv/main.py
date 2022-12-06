# import csv
# with open("weather_data.csv", mode="r") as weather:
#     data = weather.readlines()
# print(data)

# with open("weather_data.csv", mode="r") as weather:
#     data = csv.reader(weather)
#     tempereaturas = []
#     for temp in data:
#         if temp[1] != "temp":
#             tempereaturas.append(int(temp[1]))
#     print(tempereaturas)

# dato = pandas.read_csv("weather_data.csv")

# print(dato.temp.max())
# lista_temp = dato["temp"].to_list()
# print(f"El promedio de las temperaturas es: {round(sum(lista_temp)/len(lista_temp))} grados.")

# print(dato[dato.temp == dato.temp.max()])
# monday = dato[dato.day == "Monday"]
# monday.temp = (dato.temp * 9/5) + 32
# print(monday.temp)


# Crear data frame

# data_dict = {
#     "estudiantes" : ["Ignacio","Miqueas","Dante"],
#     "scores" : [4,3,3]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(data)




import pandas
datos = pandas.read_csv("2018.csv")

#Recorda el LEN que es para sacar la longitud
data_dict = {
    "color" : ["gray","black","cinnamon"],
    "count" : [len(datos[datos["Primary Fur Color"] == "Gray"]),len(datos[datos["Primary Fur Color"] == "Black"]),len(datos[datos["Primary Fur Color"] == "Cinnamon"])]
}

date = pandas.DataFrame(data_dict)
date.to_csv("reto.csv")
print(date)