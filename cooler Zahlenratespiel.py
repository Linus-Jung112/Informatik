import random 

geheimzahl = random.randint (1, 100)
tipp = 0
counter = 0

while (tipp != geheimzahl):
    counter += 1
    tipp = int(input("Gebe eine Zahl zwischen 1 und 10050 ein: "))

    if tipp <= geheimzahl:
        print("Falscher Tipp! Denke höher. Dulli!")
    elif tipp >= geheimzahl:
        print("Falscher Tipp! Denke tiefer. Dulli!")


print("GEWONNEN!!!!")
print(f"Du hast {counter} Versuche gebraucht: ")
