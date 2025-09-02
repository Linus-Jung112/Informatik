monat = 0
konzentration = 80

while konzentration >= 70:
    monat += 1
    konzentration = konzentration * 0.9975
    #print(monat, konzentration)
    
else:
    print(f"Das Medikament ist nach {monat} Monaten abgelaufen")