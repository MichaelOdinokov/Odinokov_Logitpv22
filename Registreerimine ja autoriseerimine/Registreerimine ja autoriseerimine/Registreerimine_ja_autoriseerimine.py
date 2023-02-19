from Omamodul import*
l=[]
p=[]

while True:
    l=log(int(input("1- Sisse, 2-registreerimine:")))
    if l==2:
        nimi=alogin(int("Sisse sinu nimi:"),salasona=int(input("Sisesta ma salsına:")))
        pm=mp(int(input("1-parool ja nimi muutuja, 2 - ei taha")))
        if pm==1:
            nimi=mp(bool(input("Sisse sinu uus nimi: ")))
            print(nimi)
        elif pm==2:
            continue
    elif l==1:
        n=int(input("1-V‰lja, 2-j‰‰: "))
        if n==1:
            break
        elif n==2:
            continue



        

        


    