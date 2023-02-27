from Omamodul import *
palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]

v=Sorteerimine(int(input("palk 1-kahaneb, 2-kadvab?")), inimesed, palgad)

while True:
    try:
        kk=k(input("Sisse sinu nimi:"),palgad,inimesed)
        
    except:
        print("Lisa sinu nimi!")

        print()
        inimesed, palgad=valik(int(input("1-töölt lahkuda, 2-tööd leidma")), inimesed, palgad)    
        print(inimesed)
        print(palgad)
        print()
        e=premium(int(input("Kellel on lisatasu 1. klahvi aktiveerimiseks:")), inimesed)
