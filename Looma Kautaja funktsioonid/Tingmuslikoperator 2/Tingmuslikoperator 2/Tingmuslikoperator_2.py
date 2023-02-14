while True:
    try:
        print("Arvuta peast! ...4*100-55")
        o_vastus=4*100-55
    except:
        print("Viga!")
        vastus=int(input("Lahenda ülesanne ..."))
        k=1
while True:
   if vastus!=o_vastus:
    print("Viga! Sisesta Õige vastus on ...", )
    vastus=int(input("Sisesta vastus ..."))
    k+=1
    print("Õige vastus! Katsed oli ...",k )


print("Arvuta peast! ...4*100-55")
o_vastus=4*100-55
vastus=int(input("Lahenda ülesanne ..."))
k=1
while vastus!=o_vastus:
    print("Viga! Sisesta Õige vastus on ...", )
vastus=int(input("Sisesta vastus ..."))
k+=1
print("Õige vastus! Katsed oli ...",k )

print()

for i in range(10):
    print(i, end=",")
    print()
for i in range(2, 12):
    print(i, end=";")
    print()
for i in range(2, 12, 3):
    print(i, end="")
    print()
for i in range(12, 2 , -2):
    print(i, end="")
