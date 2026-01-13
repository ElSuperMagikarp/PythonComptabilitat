quantitat = float(input("Quantitat a invertir? "))
interes = float(input("Interès percentual anual? "))
anys = int(input("Anys? "))

interesMult = 1 + (interes / 100)

for i in range(1,anys+1):
    capital = quantitat * (interesMult ** i)
    capital = round(capital, 2)
    print("Capital després de",i,"anys:",capital)