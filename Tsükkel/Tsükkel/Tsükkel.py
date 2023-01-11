while True:
        a=input("Kas soovite lennata Pariisi?")
        if a.upper()=="EI": break
        while a.upper()=="JAH":
            try:
                k=int(input("Millises klassis economy või business? (E/B): "))
                if k.upper()=="E"or k.downer()=="E": 
                    print("Pileti Hind edasi ja tagasi 470 euro")
                if k.upper()=="B" or k.downer()=="B": 
                    print("Pileti Hind edasi ja tagasi 865 euro")
            except:
                print("Kirjuta E või B!!!")

print()

#1
while True:
    try:
        nimi=input("Palun sisesta oma nimi: ")
        n=int(input("Palun sisesta mitu korda soovid tervitust saada: "))
        if nimi=="SIIM":
            n=int(input("Palun sisesta mitu korda soovid tervitust saada: "))
        for i in range(1, n+1):
            print(f"Ole tervitatud, {nimi}, {i}. korda.")
    except:
        print("!!!")
