"""
Escribir un algoritmo que permita utilizar tres tablas hash para guardar los datos de Pokémons,
que contemple las siguientes actividades: 

a)En la primera tabla hash la función hash debe ser sobre el tipo de Pokémon, en la segunda
tabla la función hash deberá utilizar el ultimo dígito del número del Pokémon como clave y
la tercera sera en base  a su nivel repartiéndolos en 10 posiciones dentro de la tabla; 
"""

def hash_type(pokemons):
    return pokemon["tipo"]

def hash_number(pokemons):
    return pokemon["numero"]%10

def hash_lvl(pokemons):
    return pokemon["nivel"]%10

table_type={}
table_number={}
table_lvl={}


pokemons=[
    {"nombre": "Bulbasaur", "tipo": "Plantas","subtipo":"veneno", "nivel": 5, "numero": 1},
    {"nombre": "Psyduck", "tipo": "Agua","subtipo":"", "nivel": 25, "numero": 54},
    {"nombre": "Nidorino" , "tipo": "Veneno","subtipo":"", "nivel": 32, "numero":33 },
    {"nombre": "Blastoise" , "tipo": "Agua","subtipo":"", "nivel": 5, "numero":9},
    {"nombre": "Charmander", "tipo": "Fuego","subtipo":"", "nivel": 4, "numero": 4},
    {"nombre": "Squirtle", "tipo": "Agua","subtipo":"", "nivel": 88, "numero": 7},
    {"nombre": "Pikachu", "tipo": "Eléctrico","subtipo":"", "nivel": 61, "numero": 25},
    {"nombre": "Geodude", "tipo": "Roca","subtipo":"Tierra", "nivel": 10, "numero": 74},
    {"nombre": "Glaceon" , "tipo": "Hielo","subtipo":"", "nivel": 5 , "numero":471},
    {"nombre": "Metagross" , "tipo": "Acero","subtipo":"Psíquico", "nivel": 55 , "numero":376}
]

def hash_subtipo(pokemons):
    return pokemon["subtipo"]

table_subtipo={}

#b)Debe utilizar tablas hash abiertas con listas como estructura secundaria;

for pokemon in pokemons:
    valur=hash_type(pokemon)
    if valur not in table_type:
        table_type[valur]=[]
    table_type[valur].append(pokemon)

    valur_2=hash_lvl(pokemon)
    if valur_2 not in table_lvl:
        table_lvl[valur_2]=[]
    table_lvl[valur_2].append(pokemon)

    valur_3=hash_number(pokemon)
    if valur_3 not in table_number:
        table_number[valur_3]=[]
    table_number[valur_3].append(pokemon)

    valur_4=hash_subtipo(pokemon)
    if valur_4 not in table_subtipo:
            table_subtipo[valur_4]=[]
    table_subtipo[valur_4].append(pokemon)

#c)Si el Pokémon es de más de un tipo deberá cargarlo en cada uno de las tabla que indiquen estos tipos;

def subtipo_pokemon(pokemons):
    for pokemon in pokemons:
        if pokemon["subtipo"] !="":
            print("Pokemons con dos tipos: ",pokemon["nombre"])

subtipo_pokemon(pokemons)

print()
#d)Deberá permitir cargar Pokémons de los cuales se dispone de su número, nombre, tipo/s, nivel.
def agregar_pokemon(numero, nombre, tipo, nivel):
    pokemon = {"numero": numero, "nombre": nombre, "tipo": tipo, "nivel": nivel}
    pokemons.append(pokemon)


numero = 10  
nombre = "Cyndaquil" 
tipo = ["Fuego"]  
nivel = 8


agregar_pokemon(numero, nombre, tipo, nivel)
print()
#e)Mostrar todos los Pokémons cuyos numeros terminan en 3, 7 y 9;
print(f"Pokemons finalizados en 3: {table_number[3]}")
print(f"Pokemons finalizados en 7: {table_number[7]}")
print(f"Pokemons finalizados en 9: {table_number[9]}")
print()

#f)Mostrar todos los Pokémons cuyos niveles son multiplos de 2, 5 y 10.

def lvlMultiplos(pokemos):
    for pokemon in pokemons:
        if (pokemon["nivel"] % 2)== 0:
            print(f"Pokemons Lvls Multiplos de 2: {pokemon}")
        if (pokemon["nivel"] % 5)== 0:
            print(f"Pokemons Lvls Multiplos de 5: {pokemon}")
        if (pokemon["nivel"] % 10)== 0:
            print(f"Pokemons Lvls Multiplos de 10: {pokemon}")

lvlMultiplos(pokemons)
print()

#g)Mostrar todos los Pokémons de los siguientes tipo: Acero, Fuego, Electrifico, Hielo.

print("Pokemons Tipo Acero: ",table_type["Acero"])
print("Pokemons Tipo Fuego: ",table_type["Fuego"])
print("Pokemons Tipo Electrico: ",table_type["Eléctrico"])
print("Pokemons Tipo Hielos: ",table_type["Hielo"])