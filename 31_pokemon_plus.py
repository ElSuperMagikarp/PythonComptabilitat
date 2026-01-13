# CLASSES
class Pokemon():
    def __init__(self, nom: str, tipo1: str, tipo2: str | None):
        # atributs
        self.nom = nom
        self.tipo1 = tipo1
        self.tipo2 = tipo2

# VARIABLES
pokemons = []

# METODES
def afegirPokemon():
    nom = input("\nIntrodueix el nom del Pokémon: ")
    tipo1 = input("Introdueix el tipus principal del Pokémon: ")
    tipo2 = None
    if(input("\nVols introduir un tipus secundari? (N/Y): ").lower().strip() == "y"):
        tipo2 = input("Introdueix el tipus secundari del Pokémon: ")
        
    newPokemon = Pokemon(nom, tipo1, tipo2)
    pokemons.append(newPokemon)
    print("Pokémon afegit \n")

def veurePokemons():
    if len(pokemons) > 0:
        print("\nLLISTA DE POKÉMONS:")
        for pokemon in pokemons:
            print("- "+pokemon.nom, end="")
            print(" | Tipo "+pokemon.tipo1, end="")
            if (pokemon.tipo2 != None):
                print(" & "+pokemon.tipo2, end="")
            print()
        input("\nPrem qualsevol tecla quan hagis acabat")
    else:
        print("\n!No hi han Pokémons!\n")

def actualitzarPokemon():
    targetPokemonName = input("\nIntrodueix el nom del Pokémon que vols canviar: ")

    targetPokemon = None
    for pokemon in pokemons:
        if pokemon.nom == targetPokemonName:
            targetPokemon = pokemon
    
    if targetPokemon != None:
        nom = input("\nIntrodueix el nou nom del Pokémon: ")
        tipo1 = input("Introdueix el nou tipus principal del Pokémon: ")
        tipo2 = None
        if(targetPokemon.tipo2 != None):
            tipo2 = input("Introdueix el nou tipus secundari del Pokémon: ")
            
        newPokemon = Pokemon(nom, tipo1, tipo2)

        pokemons[pokemons.index(targetPokemon)] = newPokemon
        print("Pokémon canviat!")
    else:
        print("\nERROR: Aquest Pokémon no existeix")

def borrarPokemon():
    targetPokemonName = input("\nIntrodueix el nou nom del Pokémon que vols esborrar: ")

    targetPokemon = None
    for pokemon in pokemons:
        if pokemon.nom == targetPokemonName:
            targetPokemon = pokemon
    
    if targetPokemon != None:
        pokemons.remove(targetPokemon)
        print("Pokémon esborrat!")
    else:
        print("\nERROR: Aquest Pokémon no existeix")

# MAIN
continuar = True
while (continuar):
    print("Que vols fer?")
    print("1- Afegir Pokémon")
    print("2- Veure Pokémons")
    print("3- Update Pokémon")
    print("4- Borrar Pokémon")
    print("5- Sortir del programa")

    selection = input("Selecciona una opció: ").strip()
    if selection == "1":
        afegirPokemon()
    elif selection == "2":
        veurePokemons()
    elif selection == "3":
        actualitzarPokemon()
    elif selection == "4":
        borrarPokemon()
    elif selection == "5":
        print("Adeu!")
        continuar = False
    else:
        print("\nERROR: Opció no valida")