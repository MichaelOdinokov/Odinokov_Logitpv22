from math import*
from random import*

#7
while True:
    try:
        mn=float(input("Mis on sinu sugu?"))
    except:
        print("Kirjuta mees voi naine!!")
        if mn.upper()=="MEES":
            k=float(input("Mis on sinu kasv?"))
        elif k>1.75:
            print("Teil on pikka kasv.")
        elif k<1.75:
            print("Teil on lühike kasv.")
        elif k==1.75:
            print("Teil on keskmine kasv.")
        if mn.upper()=="NAINE":
            k=float(input("Mis on sinu kasv."))
        elif k>1.65:
            print("Teil on pikka kasv.")
        elif k<1.65:
            print("Teil on lühike kasv.")
        elif k==1.65:
            print("Teil on keskmine kasv.")


#6
while True:
    try:
        k=float(input("Mis on sinu kasv."))
        if k>1.75:
            print("Teil on pikka kasv.")
        if k<1.75:
            print("Teil on lühike kasv.")
        if k==1.75:
            print("Teil on keskmine kasv.")
        if k.isalpha(): break
    except:
        print("Kirjuta numbrid!!!")


#5
while True:
    try:
        t=float(input("Mis on temperatuur ?"))
        if t.isalpha(): break
        if t>18:
            print("soovitav toasoojus talvel 18°")
        if t<18:
            print("soovitav toasoojus talvel 18°")
    except:
        



#3
while True:
    try:
        p=float(input("Mis seina pikkus on? "))
        if p>0: break
    except:
        print("On vaja numbreid kirjutada, mis on suurem kui 0")
while True:
    try:
        l=float(input("Laius: "))
        if l>0: break
    except:
        print("On vaja numbreid kirjutada, mis on laius kui 0")
while True:
    r=input("Kas sa tahab remontid teha? ")
    if r.upper()=="JAH" or r.upper=="EI": break
if r.upper()=="JAH":
    try:
        hind=float(input("Kui palju maksab m^2? "))
    except TypeError:
            print("Viga!!")
    hind=l*p*hind
    print(f"Remonti hind on {hind}")


#2
while True:
    a=input("Mis sinu nimi on? ") #a=nimi
    b=input("Mis sinu nimi on? ") #b=nimi
    if a.isalpha(): break
print(f"{a} on pinginaabrid {b}.")




# 21/12/22
#1
while True:
    a=input("Mis sinu nimi on: ") # a=nimi
    if a.isalpha(): break

if a.upper()=="JUKU":
    while True:
        try:
            vanus=int(input("Kui vana sa oled? "))
            break
        except:
            print("On vaja arvude tüüp kasutada")
    if 0<vanus<6: 
        print("Tasuta")
    elif 6<=vanus<=14:
        print("Lastepilet")
    elif 15<=vanus<=65: 
        print("Täispilet")
    elif 65<=vanus<=100:
        print("Sooduspilet")
    else:
        print("Vanus ei soobi!")
else:
    print("Ma otsin Juku!")


           

