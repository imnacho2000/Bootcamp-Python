travel_log = [
    {
    "country" : "France",
    "cities_visited" : ["Paris", "Lille", "Dijon"],
    "total_visits" : 12
    },
    {
    "country" : "United states", 
    "cities_visited" : ["Los Angeles", "Miami", "Orlando", "Nueva York"], 
    "Visitas_totales" : 3, 
    "RestauranteFavorito" : "In-n-out"
    },
]

def aniadir(Pais,visitas,listaCiudad):
    dicionario = {
        "Country" : Pais, 
        "cities_visited" : listaCiudad,
        "total_visits" : visitas * 2,
        }
    # dicionario ["Country"] = Pais
    # dicionario ["cities_visited"] = listaCiudad
    # dicionario ["total_visits"] = visitas
    travel_log.append(dicionario)
    print(travel_log)
    
aniadir("Russia", 2, ["Moscow", "Saint Petersburg"])
aniadir("Puticlub", 4, ["Ella", "Peterg"])