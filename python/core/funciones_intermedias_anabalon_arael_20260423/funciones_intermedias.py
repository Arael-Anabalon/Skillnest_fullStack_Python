# Ranking de puntajes de un torneo de eSports
puntajes = [ [1000, 1500, 2000], [300, 700, 1400] ]
puntajes[1][0] = 600

# Lista de creadores de contenido en una plataforma de streaming
streamers = [
   {"nombre": "GameNinjaPro", "seguidores": 250000},
   {"nombre": "PixelWarrior", "seguidores": 180000}
]
streamers[0]["nombre"] = "EliteGamerX"

# Eventos en distintas ciudades del mundo
eventos = {
   "Estados Unidos": ["Los Ángeles", "Nueva York", "Las Vegas"],
   "España": ["Madrid", "Barcelona", "Valencia"]
}
eventos["Estados Unidos"][2] = "San Francisco"

# Coordenadas de la sede de un torneo internacional
ubicacion = [
   {"latitud": 34.052235, "longitud": -118.243683}
]
ubicacion[0]["latitud"] = 40.712776





# Funciones para recorrer y representar datos:
def iterar_diccionario(lista):
   for diccionario in lista:
         lineas = []
         for clave, valor in diccionario.items():
             lineas.append(f"{clave} - {valor}")
         print(lineas)

iterar_diccionario(streamers)

def obtener_valores(clave, lista):
    for diccionario in lista:
        if clave in diccionario:
            print(diccionario[clave])

obtener_valores("nombre", streamers)
obtener_valores("seguidores", streamers)





# Mostrar información de un diccionario con listas:
categorias = {
   "juegos_populares": [
      "Fortnite", 
      "Minecraft", 
      "Valorant", 
      "GTA V",
   ],
   "ciudades_eventos": [
      "Nueva York",
      "Madrid",
      "Tokio",
   ]
}

def mostrar_informacion(diccionario):
   for categoria, lista in diccionario.items():
      print(f"{len(lista)} {categoria.upper()}")
      for items in lista:
          print(items)
   
mostrar_informacion(categorias)




    



















