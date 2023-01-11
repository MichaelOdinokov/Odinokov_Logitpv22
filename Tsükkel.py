
while True:
    try:
        a=input("Kas soovite lennata Pariisi?")
        if a.upper()=="JAH":
            b=input("Millises klassis economy või business? (E/B): ")
        elif a.upper()=="EI": break
    except:
        print("Kirjuta Jah või Ei!!!")
        if b=="E": 
            print("pileti Hind edasi ja tagasi 470 euro")
        if b=="B": 
            print("pileti Hind edasi ja tagasi 865 euro")
                                                       

print()


while True:
    try:
        nimi=input("Palun sisesta oma nimi: ")
        n=int(input("Palun sisesta mitu korda soovid tervitust saada: "))
        if nimi=="SIIM":
            n=int(input("Palun sisesta mitu korda soovid tervitust saada: "))
        for i in range(1, n+1):
            print(f"Ole tervitatud, {nimi}, {i}. korda.")
    except:
        print("!!")
