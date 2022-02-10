import random
largo = int(input("Cuantas letras queres que tenga tu contrasenia?: \n "))
simb = int(input("Cuantos simbolos?: \n"))
nums = int(input("Cuantos numeros?: \n"))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


contra = []

for n in range(0,largo):
    contra.append(random.choice(letters))
for n in range(0,nums):
    contra.append(random.choice(numbers))
for n in range(0,simb):
    contra.append(random.choice(symbols))

random.shuffle(contra)
contras=""
for n in contra:
    contras+=n
print(contras)