l=[]
p=[]

def login(l: list, p:list):
    """
    """
    return l, p

def valik(j: int):
    """
    """

def newuser(u: int):
    """
    """
    u=bool(input("Looma nimi: "))
    u=input("Введи букву => ")
    print("Вы ввели заглавную букву ",u)

    pp=input("Введи цифру => ")
    if (p.isdigit(pp)):
        print("Вы ввели цифру ", pp)
        l.appen(u) and p.append(pp)
        if l==[] and p==[]:
            print("Tere tulemast uus kasutaja!")
    return u,p

def alogin(l: list, p: list):
    """
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











