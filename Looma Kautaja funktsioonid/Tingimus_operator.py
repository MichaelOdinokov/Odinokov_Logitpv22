from math import*
from random import*

#12
sugu=input("Palun sisestage oma sugu (M / F):")

if sugu=="M":
  vanus=int(input("Palun sisestage oma vanus:"))
  if vanus>=16 and vanus<=18:
    print("Sa sobid meeskonda!")
  else:
    print("Vabandust, te ei sobi meeskonda.")
else:
  print("Vabandust, te ei sobi meeskonda.")

#10
while True:
    try:
        a=input("Sisestage esimene arv:")
        A=int(a)
        b=input("Sisestage teine arv:")
        B=int(b)
        op=input("Sisestage soovitud tehe (+-*/):")
    except:
        print("Viga!!!")
    if op == "+":
        r=A+B
    elif op=="-":
        r=A-B
    elif op=="*":
        r=A*B
    elif op == "/":
        r=A/B
        print(f"{r}")



#9
s=input("Sisestage ruudu külje pikkus: ")
A=s
s=input("Sisestage ruudu teise külje pikkus: ")
B=s
if A==B:
  print("See on ruut.")
else:
  print("See ei ole ruut.")



#7
while True:
    try:
        mn=float(input("Mis on sinu sugu?"))
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
    except:
        print("Viga!!")

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
        


#4
print("Alghind 700")
a=700
h=700*30/100
print(f"Soodushind on {h}")

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


           

