palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E","F","G"]

def k(k:int,p:float)->bool:
    """
    Kasutajad kirjuta ise nimi
    :parem k: Muutaja
    :rtype: bool
    """
    if k in inimesed and inimesed.istitle():# Начинаются ли слова в строке с заглавной буквы: (inimesed.istitle())
        p=float(input("Sisse teie palgad: "))
        pass
    else:
        print("Viga!")
    return k, p

#19 Ise funktsioon, uus töötane
t=[]#töötane
vanus=[]
pa=[]#palgad
v=1300

def uk(u:bool, vanus: int, p: int):
    """
    Uus töötane registrerimine
    :parem bool u: Muutaja
    :rtype: u
    """
    
    if vanus<18:
        print("Te ei soobi!")
    elif vanus>=18:
        u=int(input("Sisse teie nimi: "))
        t.append(u)
        p=int(input("Milline palg te tahte, suurem 1200 euro või väiksem(1-Suurem, 2-Väikem):"))
        if p==1:
            print("Me helistame tagasi teiele!")    
        elif p==2:
            print("Teie palg on 1300 eurp.Palju õnne!")
            pa.append(v)
    return u, vanus, p

def valik(v:int):
    """
    Vale töölt lahkuda
    :parm int: v: Muutaja
    :rtype:
    """
    if v==2:
        uk
    elif v==1:
        nimi=int(input("Sisse sinu nimi:"))
        if nimi in t:
            t.removed(nimi)
            print("Sinu nimi removed. Nägemist!")
        else:
            print("Te ei töötate siin!")


            

    

    





        
