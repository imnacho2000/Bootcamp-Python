import functions

# f = input("Ingrese su nombre: ")
# s = input("Ingrese su apellido: ")
# print(f"Eres: {functions.format_name(f,s)}")

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = functions.days_in_month(year, month)
print(days)