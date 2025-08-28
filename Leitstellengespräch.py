
def leitstellengespraech():
    wo = ""
    was = "Autounfall mit 2 Verletzten"   
    wie = "Auffahrunfall"
    wer = "Heinz, 70, MICHIII, 18"

    wo = input("Wo ist der Notfallort? ")

    print(f"In {wo} Geschah ein {was} Durch {wie} Mit {wer}")

#leitstellengespraech()

def leitstelle():
    wo = input("Wo ist der Notfallort? ")
    was = input("Was ist passiert? ")
    wie = input("Wie ist der Notfall passiert? ")
    wer = input("Wer ruft an? ")

    print("Dort ist der Unfall: " + wo)
    print("Das ist passiert: " + was)
    print("So ist es passiert: " + wie)
    print("Der hat angerufen: " + wer)
    
leitstelle()