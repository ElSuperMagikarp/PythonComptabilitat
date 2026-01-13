# VARIABLES
pokemons = []

# METODES
def afegirPokemon():
    newPokemon = input("\nQuin pokémon vols afegir? ")
    pokemons.append(newPokemon)
    print("Pokémon afegit \n")

def veurePokemons():
    if len(pokemons) > 0:
        print("\nLLISTA DE POKÉMONS:")
        for pokemon in pokemons:
            print("-"+pokemon)
        input("\nPrem qualsevol tecla quan hagis acabat")
    else:
        print("\n!No hi han Pokémons!\n")

def actualitzarPokemon():
    targetPokemon = input("\nQuin pokémon vols canviar? ")
    
    if targetPokemon in pokemons:
        newPokemon = input("Introdueix el nou Pokémon: ")
        pokemons[pokemons.index(targetPokemon)] = newPokemon
        print("Pokémon canviat!")
    else:
        print("\nERROR: Aquest Pokémon no existeix")

def borrarPokemon():
    deletedPokemon = input("\nQuin pokémon vols esborrar? ")
    
    if deletedPokemon in pokemons:
        pokemons.remove(deletedPokemon)
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