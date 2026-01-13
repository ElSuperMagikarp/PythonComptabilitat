import datetime

try:
    nom = input("Quin és el teu nom? ")
    cognom = input("Quin és el teu primer cognom? ")
    lloc = input("On vas neixer? ")
    dataStr = input("Quan vas neixer? (Format YYYY-MM-DD): ")
    data = datetime.datetime.strptime(dataStr, "%Y-%m-%d")
    if   (data.month == 12 and data.day >= 22) or (data.month == 1 and data.day <= 19):
        signe = "Capricornio"
    elif (data.month == 1 and data.day >= 20) or (data.month == 2 and data.day <= 18):
        signe = "Aquario"
    elif (data.month == 2 and data.day >= 19) or (data.month == 3 and data.day <= 20):
        signe = "Piscis"
    elif (data.month == 3 and data.day >= 21) or (data.month == 4 and data.day <= 19):
        signe = "Aries"
    elif (data.month == 4 and data.day >= 20) or (data.month == 5 and data.day <= 20):
        signe = "Tauro"
    elif (data.month == 5 and data.day >= 21) or (data.month == 6 and data.day <= 20):
        signe = "Geminis"
    elif (data.month == 6 and data.day >= 21) or (data.month == 7 and data.day <= 22):
        signe = "Cancer"
    elif (data.month == 7 and data.day >= 23) or (data.month == 8 and data.day <= 22):
        signe = "Leo"
    elif (data.month == 8 and data.day >= 23) or (data.month == 9 and data.day <= 22):
        signe = "Virgo"
    elif (data.month == 9 and data.day >= 23) or (data.month == 10 and data.day <= 22):
        signe = "Libra"
    elif (data.month == 10 and data.day >= 23) or (data.month == 11 and data.day <= 21):
        signe = "Escorpio"
    elif (data.month == 11 and data.day >= 22) or (data.month == 12 and data.day <= 21):
        signe = "Sagitario"
    else:
        signe = None

    print("Sr./Sra. ",nom," ",cognom,", nascut a ",lloc," l'any ",data.year,", té a ",signe," com a signe solar del zodíac.", sep="")
except ValueError:
    print("Format de data invalid. Siusplau utilitza YYYY-MM-DD.")