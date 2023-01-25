spisok=[]
numbers=[1,2,3,4,5]
abc=['Abc','a','c']
slovo="Programmeerimine"
slovo_list=list(slovo)
print(slovo)
print(slovo_list)
while True:
    print("1- lisa sõna lists")
    print("2 - kleebi järendid")
    print("4 - udalit element")
    print("5 - Удаляет i-ый элемент и возвращает его.")
    print("6 - Возвращает положение первого элемента от start до end со значением a ") 
    print("7 - Копия списка ")
    valik=int(input())
    if valik==1:
        a=input("Sisse bukvu")
        slovo_list.append(a)
        print(f"dobavil {a} uus järendid", slovo_list)
    elif valik==5:
        slovo_list.pop(a)
    elif valik==6:
        slovo_list.index(a, [start [, end]])
    elif valik==2:
        slovo_list.extend(abc)
        print(slovo_list)
    elif valik==3:
        a=input("sissesta bukvu, milline soovib lisa")
        i=input(input("Sissesta number kohal, et soovin lisa bukvu"))
        slovo_list.insert(i-1,a)#0,1,2...
        print(slovo_list)
    elif valik==4:
        a=input("Sisseta bukvu, et sa soovid udalit")
        n=slovo_list.count(a)
        if n>0:
            for in range(n):
                slovo_list.remove(a)
        else:
            print("Iskomoi bukvi net")
    print(slovo_list)

    


