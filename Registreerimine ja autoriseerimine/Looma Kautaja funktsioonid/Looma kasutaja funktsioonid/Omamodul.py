#1
def arithmetic(arv1:float,tehe: str,arv2:float)->any:
    """E
    :param int a: Järjend 
    :rtype: str
    """

    if tehe=="+":
        vastus=arv1+arv2
    elif tehe=="-":
        vastus==arv1-arv2
    elif tehe=="*":
        vastus=arv1*arv2
    elif tehe=="/":
        vastus=arv1/arv2
    return 
#2
def   is_year_leap(a:int)->bool:
    """E
    :param int y: Järjend
    :rtype: str
    """
    if a%4==0:
        True 
    else:
        False
    return False or True
#3
def square(arv:float,a)->any:
    """E
    :param int 
    :rtype: str
    """
    
    P=arv**4
    S=arv**2
    d=arv
    return arv
#4
def season(k1,k:int)->any:
    """E
    :param int
    :rtype: str
    """
    if k==1 and k==2 and k==12:
        k1=="Talv"
    elif k==3 and k==4 and 5:
        k1="Kevad"
    elif k==6 and k==7 and k==8:
        k1="Suvel"
    elif k==9 and k==10 and k==11:
        k1="Sügis"
    return k1

#5
def bank(b: float, aa: int):
    """
    """
    for i in range(aa):
        b=b+b*0.1
    return b
 
#6
def is_prem(n: float):
    """
    """
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

#7
def date(day: int,month:int,year: int):
    """
    """
    if month in (1, 3, 5, 7, 8, 10, 12):
        return day>=1 and day<=31
    elif month in (4, 6, 9, 11):
        return day>=1 and day<=30
    elif month==2:
        if year%4==0 and (year%400==0 or year%100!=0):
            return day>=1 and day<=29
        else:
            return day>=1 and day<=28
    else:
        return False

#7.2
from datetime import*
def date_(d:int,m: int,y:int)->bool:
    """
    :param:
    ::rtype:
    """
    try:
        print(date(y,m,d))
        date(y,m,d)
        flag=True
    except:
        print("Viga")
        flag=False
    return flag








 
    