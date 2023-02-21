palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E","F","G"]

def k(k:bool,pp:int)->bool:
    """
    Kasutajad kirjuta ise nimi
    :parem k: Muutaja
    :rtype: bool
    """
    k=bool(input("Sisse sinu nimi:"))
    k.append
    if k in inimesed and inimesed.istitle():# Начинаются ли слова в строке с заглавной буквы: (inimesed.istitle())
        pp=int(input("Sisse teie palgad: "))
        print(pp)
        pass
    else:
        print("Viga!")
    return k, pp

#19 Ise funktsioon, uus töötane

def uk(u:int, t: list):
    """
    Uus töötane registrerimine
    :parem bool u: Muutaja
    :rtype: u
    """
    va=int(input("Teie vanus: "))
    if va<18:
        print("Te ei soobi!")
    elif va>=18:
        u=bool(input("Sisse teie nimi: "))
        t.append(u)
        p=int(input("Milline palg te tahte, suurem 1200 euro või väiksem(1-Suurem, 2-Väikem):"))
        if p==1:
            print("Me helistame tagasi teiele!")    
        elif p==2:
            print("Teie palg on 1300 eurp.Palju õnne!")
            pa.append(v)
    return u, p

def valik(v:int):
    """
    Vale töölt lahkuda
    :parm int: v: Muutaja
    :rtype:
    """
    if v==2:
        uk
    elif v==1:
        nimi=bool(input("Sisse sinu nimi:"))
        if nimi in t:
            t.removed(nimi)
            print("Sinu nimi removed. Nägemist!")
        else:
            print("Te ei töötate siin!")
    return v

#def delete
#def create



            

    

    





        
