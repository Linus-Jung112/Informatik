def bmitesterschule():

    gewicht = int(input ("Gib dein Gewicht ein (kg):  "))
    groesse = int(input ("Gib deine Groesse ein (cm):  "))

    bmi = 10000 * gewicht / (groesse *  groesse)

    print("Dein BMI betraegt:  ", bmi)

bmitesterschule()