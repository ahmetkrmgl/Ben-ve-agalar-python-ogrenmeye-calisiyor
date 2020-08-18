import random
import os
def temizle():
    if os.name=="nt":
        os.system("cls")
    else:
        os.system("clear")
x,secim,insanevlatlari=True,"",[]
while secim != "bitti":
    secim=input("Bir isim giriniz:")
    temizle()
    insanevlatlari.append(secim.title())
    if secim=="sil":
        insanevlatlari.pop()
        insanevlatlari.pop()
    if x==True:
        print("Isimler bittiginde \"bitti\" yazınız")
        print("Son yazıgınız ismi silmek icin \"sil\" yazın")
        x=False
insanevlatlari.pop()
temizle()
print("""Rus ruleti oynaniyor...
--------------------------""")
y=random.randint(0,len(insanevlatlari)-1)
print("{} öldü".format(insanevlatlari[y].capitalize()))
insanevlatlari.pop(y)
print("Yasayanlar",insanevlatlari)
input("")