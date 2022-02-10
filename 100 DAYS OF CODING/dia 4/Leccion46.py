row1 = ["","",""]
row2 = ["","",""]
row3 = ["","",""]
map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
n = input("Donde queres poner el tesoro? ")
column = int(n[0])
fila = int(n[1])
map[fila - 1][column - 1] = "X"
print(f"{row1}\n{row2}\n{row3}")
