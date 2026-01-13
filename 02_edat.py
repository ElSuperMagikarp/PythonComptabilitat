edatPersona1 = int(input("Quina és la edat de la 1ra persona? "))
edatPersona2 = int(input("Quina és la edat de la 2na persona? "))

if edatPersona1 > edatPersona2:
    print("La persona 1 és la més gran")
elif edatPersona2 > edatPersona1:
    print("La persona 2 és la més gran")
else:
    print("Les dos persones tenen la mateixa edat")