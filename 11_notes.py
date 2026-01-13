notes = []
nom = input("Com et dius? ")
for i in range(1, 6):
    inputstr = "Introdueix la nota de la RA%s: " % (i)
    notes.append(float(input(inputstr)))

print("Hola %s!" % (nom))
sumaNotes = 0
for i in range(0, len(notes)):
    print("Nota RA",i+1,":",notes[i])
    sumaNotes = sumaNotes+notes[i]

mitjana = sumaNotes / len(notes)
print("Mitjana:", mitjana)

