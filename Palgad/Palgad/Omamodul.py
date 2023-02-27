import random

def Vordsed_palgad(inimesed: list, palgad: list):#
    """
    """
    dublikatid=[x for x in palgad if palgad.count(x)>1]
    dublikatid=list(set(dublikatid))# lisa Järendisse: [1200, 2500, 750, 750, 1200]->[1200,750]
    for palk in dublikatid:
        n=palgad.count(palk)#1200, n=2; 750, n=2
        k=-1#
        print(f"{palk} saavad kätte järgmised inimesed:")
        for j in range(n):
            k=palgad.index(palk, k+1)# k=p.index(palk, k+1)- pervi index ctobi pereschla na sledujushi index to stavim satrtovi index
            nimi=inimesed[k]
            print(nimi)
    return palgad, inimesed

def Sorteerimine(inimesed: list, palgad: list):
    """Palgad kahneb või kadvab
    param: list inimesed, list palgad: Järjend
    :rtype: list, list
    """
    v=int(input("palk 1-kahaneb, 2-kadvab?"))
    if v==1:
        n=len(palgad)
        for j in range (0, n-1):
            for k in range (j+1,n):
                if palgad[j]<palgad[k]:
                    abi=palgad[j]# if abi 0 palgad[j]
                    palgad[j]=palgad[k]# if palgad[j]=palgad[k]
                    palgad[k]=abi# if palgad[k]=abi
                    abi=inimesed[j]# if  abi=inimesed[j]
                    inimesed[j]=inimesed[k]# if inimesed[j]=inimesed[k]
                    inimesed[k]=abi# if inimesed[k]=abi
    elif v==2:
            n=len(palgad)
            for j in range (0, n-1):
                for k in range (j+1,n):
                    if palgad[j]>palgad[k]:
                        abi=palgad[j]
                        palgad[j]=palgad[k]
                        palgad[k]=abi
                        abi=inimesed[j]
                        inimesed[j]=inimesed[k]
                        inimesed[k]=abi
    return inimesed, palgad

                
def Kustutamine(inimesed: list, palgad: list):
    """
    :param list i: Inimeste järjend, lisy p: Palgade järjend
    :rtype: list, list
    """
    nimi=input("Sisesta nimi:")
    if nimi in inimesed:
        n=inimesed.count(nimi)# list.count shitaet cloichestvo zarplat
        for j in range(n):
            ind=inimesed.index(nimi)
            inimesed.pop(ind)
            palgad.pop(ind)
    return inimesed, palgad

def k(k:str, palgad: list, inimesed: list):
    """
    Kasutajad kirjuta ise nimi
    :parem k: str, palgad: list, inimesed: list
    :rtype: palgad, inimesed
    """    
    if k not in inimesed:# Начинаются ли слова в строке с заглавной буквы: (inimesed.istitle())
            inimesed.append(k)
            pp=int(input("Sisse teie palgad: "))
            print("Teie palg on",pp)
            palgad.append(pp)
    else:
        print("Lisa sinu nimi!")
    return inimesed, palgad

#19 Ise funktsioon, uus töötane
def valik(v:int, inimesed: list, palgad: list):
    """
    Vale töölt lahkuda
    :parm int: v: Muutaja
    :rtype: inimesed, palgad
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
            inimesed.remove(nimi)
            print("Sinu nimi removed.")
            pp=int(input("Sisse teie palgad: "))
            palgad.remove(pp)
            print("Teie palg removed.")
            print("Nägemist!")
        else:
            print("Te ei töötate siin!")
    return inimesed, palgad

#Premium võta
"""
"""
def premium(w:int, inimesed: list):
    if w==1:
        for i in range(1):
            w=random.choice(inimesed)
            print("Победитель:", w)
    else:
        print("Kirjuta 1!")