import string
l=[]
p=[]

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



def registreerimine(a: int)->bool:
    """
    Uus kasutajad loojab uus kont
    :parem: int a: muutuja
    :rtype: p, nimi
    """
    nimi=bool(input("Sisse sinu uus nimi: "))
    a=int(input("1-autoserimine, 2-ise registreerimine"))
    if a==1:
        salasona=Salasona(12)
        l.append(nimi)
        p.append(salasona)
    elif a==2:
        p=float(input("Sisse sinu parool:"))
        p.append(p)
    return p, nimi




def Salasona(k: int)->bool:
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

def mp(p:float,nimi: bool):
    """Muutuja parool ja nimi
    :poarem float p, bool nimi; muutuja
    :rtypr: p, nimi
    """
    nimi=bool(input("Sisse sinu uus nimi: "))
    a=int(input("1-autoserimine, 2-ise registreerimine"))
    if a==1:
        salasona=Salasona(12)
        l.replace(nimi)
        p.replace(salasona)
    elif a==2:
        p=float(input("Sisse sinu parool:"))
        p.replace(p)
    return p,nimi




















