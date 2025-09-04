# 6. [enkel python] schrijf een programma die 2getalen vraagt: </br>
#    . print de som van deze twee getallen</br>
#    . print de zin: "de som van de getallen x en y is x+y" (vervang natuurlijk x en y)

getal1 = int(input("geef een nummer: "))
getal2 = int(input("geef nog een nummer: "))

som = getal1+getal2
print(som)

print(f"de som van de getallen {getal1} en {getal2} is {som}")
