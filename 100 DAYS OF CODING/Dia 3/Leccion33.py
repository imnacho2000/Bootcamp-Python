anio = int(input("Ingrese un anio: "))
if(anio % 4 == 0):
    if(anio % 100 == 0):
        if(anio % 400 == 0):
            print("El anio " + str(anio) + " es bisiesto.")
        else:
            print("El anio" + str(anio) + " no es bisiesto")
    else:
        print("El anio " + str(anio) + "  es bisiesto.")
else:
    print("El anio " + str(anio) + "  no es bisiesto.")