import random
from tkinter import W 
palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]

def k(k:list):
    """
    Kasutajad kirjuta ise nimi
    :parem k: Muutaja
    :rtype: bool
    """
    
    if k not in inimesed:# Начинаются ли слова в строке с заглавной буквы: (inimesed.istitle())
        inimesed.append(k)
        pp=int(input("Sisse teie palgad: "))
        print("Teie palg on",pp)
        palgad.append(pp)
        pass
    else:
        print("Viga!")
    return k

#19 Ise funktsioon, uus töötane
def valik(v:int):
    """
    Vale töölt lahkuda
    :parm int: v: Muutaja
    :rtype:
    """
    if v==2:
        va=int(input("Teie vanus: "))
        if va<18:
            print("Te ei soobi!")
        elif va>=18:
            u=input("Sisse teie nimi: ")
            inimesed.append(u)
            pp=int(input("Sisse teie palgad: "))
            palgad.append(pp)
            print("Teie palg on",pp)
    elif v==1:
        nimi=input("Sisse sinu nimi:")
        if nimi in inimesed:
            inimesed.removed(nimi)
            print("Sinu nimi removed.")
            pp=int(input("Sisse teie palgad: "))
            palgad.append(pp)
            print("Teie palg removed.")
            print("Nägemist!")
        else:
            print("Te ei töötate siin!")
    return v

#Premium võta
def premium(w:int):
    if w==1:
        for i in range(1):
            w=random.choice(inimesed)
            print("Победитель:", w)
    else:
        print("Kirjuta 1!")


#def delete
#def create



            

    

    





        
