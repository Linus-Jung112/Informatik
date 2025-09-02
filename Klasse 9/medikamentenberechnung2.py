monat = 0
konzentration = int(input("Bitte gebe die Konzentration deines Produktes an: "))
kritisch = int(input("Bitte gebe den Wert an bei dem dein Produkt kritisch wird: "))
rate = float(input("Bitte gebe die Rate an bei der dein Produkt schlecht wird: "))

while konzentration >= kritisch:
    monat += 1
    konzentration = konzentration * (1 - rate/100)
    print(monat, konzentration)
    
else:
    print(f"Das Medikament ist nach {monat} Monaten abgelaufen")