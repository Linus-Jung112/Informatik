import random 

geheimzahl = random.randint (1, 100)
tipp = 0
counter = 0

while counter <= 1000:
    counter += 1
    tipp = int(input("Gebe eine Zahl zwischen 1 und 10 ein: "))
    
    if (tipp == geheimzahl):
        print("GEWONNEN!!!!")
        print(f"Du hast {counter} Versuche gebraucht: ")
        break 
    else:
        print("Loser!! Falscher Tipp")
