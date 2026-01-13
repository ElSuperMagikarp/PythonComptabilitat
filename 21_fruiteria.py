# VARIABLES
fruites = {}

# METODES
def afegirFruita():
    print()
    nomFruita = input("Introdueix el nom de la fruita: ")
    
    if nomFruita in fruites:
        print("\nERROR: Aquesta fruita ja existeix")
    else:
        preuPerKilo = float(input("Quin preu té? (Per kilo): "))
        fruites[nomFruita] = preuPerKilo
        print("Fruita afegida!")

def calcularValor():
    print()
    print("Fruites: ")
    for fruita in fruites:
        print(fruita, end=" ")
    print()
    nomFruita = input("Introdueix el nom de la fruita: ")
    
    if nomFruita in fruites:
        kilos = float(input("Introdueix el nombre de kilos: "))
        preu = fruites[nomFruita] * kilos
        print("Costará "+str(preu)+"€", sep="")
    else:
        print("\nERROR: Aquesta fruita no existeix")

# MAIN
continuar = True
while (continuar):
    print()
    print("Que vols fer?")
    print("1- Afegir Fruita")
    print("2- Calcular Valor")
    print("3- Sortir del programa")

    selection = input("Selecciona una opció: ").strip()
    if selection == "1":
        afegirFruita()
    elif selection == "2":
        calcularValor()
    elif selection == "3":
        print("Adeu!")
        continuar = False
    else:
        print("\nERROR: Opció no valida")