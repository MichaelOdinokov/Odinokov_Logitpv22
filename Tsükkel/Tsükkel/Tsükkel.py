



#0
while True:
    try:
        a=input("Kas soovite lennata Pariisi?") # a=Kasutaja
        if a.upper()=="JAH" or a.upper()=="EI": break
    except:("Kirjuta Jah või Ei!!!!")
if a.upper()=="JAH":
    while True:
            try:
                k=int(input("Millises klassis economy või business? (E/B): "))# k=Kasutaja:
                if k.upper()=="E":
                                print("Pileti Hind edasi ja tagasi 470 euro")
                if k.upper()=="B": 
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
            n=int(input("Palun sisesta mitu korda soovid tervitust saada: ")) # n=korda
        for i in range(1, n+1): # i=katsete arv
            print(f"Ole tervitatud, {nimi}, {i}. korda.")
    except:
        print("!!!")
