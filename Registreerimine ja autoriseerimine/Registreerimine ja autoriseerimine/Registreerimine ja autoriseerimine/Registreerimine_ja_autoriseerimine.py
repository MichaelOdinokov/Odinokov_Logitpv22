from Omamodul import*
l=[]#nimi
p=[]#salsõna

while True:
    l=log(int(input("1- Sisse, 2-registreerimine, 3-muutuja salsõna, 4-nimi muutaja:")))
    if l==1:
        n=alogin(int(input("Sissesta oma nimi: "), salasona=input("Sissesta ma salsõna:")))#nimi
    elif l==2:
        n=registreerimine(bool(input("Sisse sinu uus nimi: ")))
    elif l==3:
        nimi=mp(int(input("Sisse sinu nimi:")))
    elif l==4:
        n=nimim(bool(input("Sisse sinu vana nimi:")))




        

    


        

        


    