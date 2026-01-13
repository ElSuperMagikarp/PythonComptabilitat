continuar = True
while (continuar):
    amplada = int(input("Amplada: "))
    alcada = int(input("Alçada: "))
    caracter = input("Caràcter: ")

    for i in range(1,alcada+1):
        for i in range(1,amplada+1):
            print(caracter, end=" ")
        print()
    
    continuarStr = input("Vols seguir fent rectangles? (Y/N): ")
    if (continuarStr == "Y" or continuarStr == "y"):
        continuar = True
    else:
        continuar = False