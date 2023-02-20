import string
l=[]#nimi
p=[]#salsõna


def log(l:int)->bool:
    """
    Valik siise või registreerimine
    :parem int l: muutuja 
    :rtype: bool
    """
    l=int(input("1- Sisse, 2-registreerimine:"))
    if l==1:
        alogin
    elif l==2:
        registreerimine
    return l

def alogin(l: list, p: list):#sisessta
    """
    Kasutaja sisse
    :parem list l , list p: Järjend
    :rtype: nimi, salasona
    """
    nimi=input("Sissesta oma nimi: ")
    salasona=input("Sisesta ma salsõna:")
    if nimi in l:
        ind=l.index(nimi)
        if salasona==p[ind]:
            print("Tere Tulemast")
        else:
            print("Vale sõna!")
    else:
        print("Ei ole kiris!")
    return nimi,salasona



def registreerimine(a: int)->bool:#Looma
    """
    Uus kasutajad loojab uus kont
    :parem: int a: muutuja
    :rtype: p, nimi
    """
    nimi=bool(input("Sisse sinu uus nimi: "))
    if nimi not in l==[]:
        l.append(nimi)
        print("Sinu uus nimi", nimi)
        a=int(input("1-autoserimine, 2-ise registreerimine"))
    if a==1:
        salasona=Salasona(12)
        if salasona not in p==[]:
            p.append(salasona) 
            print("Tere tulemast!")
    elif a==2:
        p=float(input("Sisse sinu p:"))
        if p not in p==[]:
            p.append(p)
            print("Tere tulemast!")
        else:
            print("See nimi oli!")
    return p, nimi




def Salasona(k: int)->bool:# appi autoseerimine
    """
    Määrme salasõna..
    :parem int k:Järjend salasõna numbridest
    :rtype: bool
    """
    saladus=""
    for i in range(k):
        t=(string.ascii_letters) #Aa...Zz
        num=([1,2,3,4,5,6,7,8,9,0])
        sym=(["*","-",".","!","_"])
        t_num=[t,str(num),sym]
        saladus+=(t_num)
    return saladus

def mp(p:float,nimi: bool, l: list):# salsõna muutuja
    """Muutuja parool
    :parem float p, bool nimi: Järjend
    :rtypr: p, nimi
    """
    nimi=int(input("Sisse sinu nimi:"))
    if nimi not in l==[]:
        print("Järendisse ei ole see nimi! Kordate.")
    else:
        nimi=int(input("Oled sa kindel, salaõna muutuja? 1-Jah, 2-Ei"))
    if nimi==1:
        a=int(input("1-autoserimine, 2-ise registreerimine"))
        if a==1:
            p.remove(salasona)
            print("Vana salsõna removed")
            salasona=Salasona(12)
            print(f"Sinu uus salsõna {salasona}")
        elif a==2:
            p.remove(p)
            print("Vana salsõna removed!")
            p=float(input("Sisse sinu uus parool:"))
            p.append(p)
            print("Sinu uus salsõna", p)
    elif nimi==2:
        print("Parool vaja")
    return p,nimi,a



def nimim(nimi:int, l: list)->bool:#nimi muutuja
    """Muutaja nimi
    :parem int nimi:Järjend
    :rtype: bool
    """
    nimi=bool(input("Sisse sinu vana nimi:"))
    if nimi not in l==[]:
        print("Vale nimi!")
    elif nimi in l==[]:
        nimi=int(input("Oled sa kindel, nimi muutaja? 1-Jah, 2-Ei"))
    if nimi==1:
        l.remove(nimi)
        print("Nimi removed")
        nimi=bool(input("Mutajate nimi: "))
        l.append(nimi)
        print("Looma uus nimi", nimi)
    elif nimi==2:
        print("Vaja!")
        
    return nimi

def nimi(nimi:int, l: list)->bool:
    """
    Looma nimi
    :parem int nimi: Järjend
    :rtype: bool
    """
    nimi=bool(input("Sisse sinu uus nimi: "))
    if nimi not in l==[]:
        l.append(nimi)
    print(f"Sinu uus nimi {nimi}")
    return nimi



    




















