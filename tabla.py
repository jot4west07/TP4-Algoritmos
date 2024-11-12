# Funciones de hash para cada tabla
def hash_type(pokemon):
    return pokemon["tipo"]

def hash_number(pokemon):
    return pokemon["numero"] % 10 # La razón por la que se usa % 10 es para obtener el último dígito del número del pokemon

def hash_lvl(pokemon):
    return pokemon["nivel"] % 10

# Si la condición pokemon["subtipo"] != "" es True (es decir, el Pokemon tiene un subtipo), entonces devuelve el subtipo del Pokemon (pokemon["subtipo"]).
# Si la condición es False (es decir, el Pokemon no tiene subtipo, o el valor de subtipo es una cadena vacía ""), entonces devuelve None.
def hash_subtipo(pokemon):
    return pokemon["subtipo"] if pokemon["subtipo"] != "" else None

# Tablas hash para almacenar los Pokemons
table_type = {}
table_number = {}
table_lvl = {}
table_subtipo = {}

# Lista de Pokemons
pokemons = [
    {"nombre": "Bulbasaur", "tipo": "Plantas", "subtipo": "veneno", "nivel": 5, "numero": 1},
    {"nombre": "Psyduck", "tipo": "Agua", "subtipo": "", "nivel": 25, "numero": 54},
    {"nombre": "Nidorino", "tipo": "Veneno", "subtipo": "", "nivel": 32, "numero": 33},
    {"nombre": "Blastoise", "tipo": "Agua", "subtipo": "", "nivel": 5, "numero": 9},
    {"nombre": "Charmander", "tipo": "Fuego", "subtipo": "", "nivel": 4, "numero": 4},
    {"nombre": "Squirtle", "tipo": "Agua", "subtipo": "", "nivel": 88, "numero": 7},
    {"nombre": "Pikachu", "tipo": "Eléctrico", "subtipo": "", "nivel": 61, "numero": 25},
    {"nombre": "Geodude", "tipo": "Roca", "subtipo": "Tierra", "nivel": 10, "numero": 74},
    {"nombre": "Glaceon", "tipo": "Hielo", "subtipo": "", "nivel": 5, "numero": 471},
    {"nombre": "Metagross", "tipo": "Acero", "subtipo": "Psíquico", "nivel": 55, "numero": 376}
]

# Insertar Pokémones en las tablas hash
for pokemon in pokemons:
    # Hash por tipo
    valur = hash_type(pokemon) # valur asume el tipo del pokemon
    if valur not in table_type:
        table_type[valur] = [] # asigna una lista vacía a la clave valur dentro del diccionario table_type
    table_type[valur].append(pokemon) # agregar a table_type con clave [valur]
    
    # Hash por último dígito
    valur_2 = hash_number(pokemon)
    if valur_2 not in table_number: # si valur_2 no esta en table_number
        table_number[valur_2] = [] # asigna una lista vacía a la clave valur_2 dentro del diccionario table_number
    table_number[valur_2].append(pokemon) # agregar a table_number con clave [valur_2]
    
    # Hash por nivel
    valur_3 = hash_lvl(pokemon)
    if valur_3 not in table_lvl: # si valur_3 no esta en table_lvl
        table_lvl[valur_3] = [] # asigna una lista vacía a la clave valur_3 dentro del diccionario table_lvl
    table_lvl[valur_3].append(pokemon) # agregar a table_lvl con clave [valur_3]
    
    # Hash por subtipo (si tiene)
    valur_4 = hash_subtipo(pokemon)
    if valur_4: # Si el pokemon no tiene subtipo (es decir, el campo subtipo es ""), entonces valur_4 será None
        if valur_4 not in table_subtipo:
            table_subtipo[valur_4] = [] # crea una nueva clave en el diccionario y asigna una lista vacía a esa clave
        table_subtipo[valur_4].append(pokemon) # agregar a table_subtipo con clave [valur_4]

# c) Si el Pokémon tiene más de un tipo, mostrarlo
print("Se asume que si el pokemon tiene tipo y subtipo, ya tiene mas de un tipo")
def subtipo_pokemon(pokemons):
    for pokemon in pokemons:
        if pokemon["subtipo"] != "": # si es distinto a vacio mostrarlo 
            print(f"Pokémon con dos tipos: {pokemon['nombre']}")

subtipo_pokemon(pokemons)
print()

# d) Función para agregar nuevos Pokemones
def agregar_pokemon(numero, nombre, tipo, nivel, subtipo=""):
    pokemon = {"numero": numero, "nombre": nombre, "tipo": tipo, "nivel": nivel, "subtipo": subtipo}
    pokemons.append(pokemon)

# Agregar un nuevo Pokémon
numero = 10  
nombre = "Cyndaquil" 
tipo = ["Fuego"]  
nivel = 8

agregar_pokemon(numero, nombre, tipo, nivel)
print()

# e) Mostrar todos los Pokémones cuyos números terminan en 3, 7 y 9
def mostrar_pokemon_por_ultimo_digito():
    for digito in [3, 7, 9]:
        if digito in table_number:
            print(f"Pokémons finalizados en {digito}:")
            for pokemon in table_number[digito]:
                print(f"  - {pokemon['nombre']}")
        else:
            print(f"No hay Pokémones que terminan en {digito}")
    print()

mostrar_pokemon_por_ultimo_digito()

# f) Mostrar todos los Pokémones cuyos niveles son múltiplos de 2, 5 y 10
def lvlMultiplos(pokemons):
    for pokemon in pokemons:
        if pokemon["nivel"] % 2 == 0:
            print(f"Pokémon nivel múltiplo de 2: {pokemon['nombre']}")
        if pokemon["nivel"] % 5 == 0:
            print(f"Pokémon nivel múltiplo de 5: {pokemon['nombre']}")
        if pokemon["nivel"] % 10 == 0:
            print(f"Pokémon nivel múltiplo de 10: {pokemon['nombre']}")
    print()

lvlMultiplos(pokemons)

# g) Mostrar todos los Pokémones de los siguientes tipos: Acero, Fuego, Eléctrico, Hielo
def mostrar_pokemon_por_tipo(tipos):
    for tipo in tipos: # tipos sera una lista con los tipos de pokemons
        if tipo in table_type: # si tipo esta en la tabla de tipos
            print(f"Pokémons tipo {tipo}:")
            for pokemon in table_type[tipo]:
                print(f"  - {pokemon['nombre']}")
        else:
            print(f"No hay Pokémones del tipo {tipo}")
    print()

mostrar_pokemon_por_tipo(["Acero", "Fuego", "Eléctrico", "Hielo"])
