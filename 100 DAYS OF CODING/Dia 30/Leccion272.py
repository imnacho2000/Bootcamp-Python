fruits = ["Apple", "Pear", "Orange"]

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError as error:
        print(f"Error: {error}, el indice {index} esta fuera de rango")
    else:
        print(fruit + " pie")  


make_pie(4)