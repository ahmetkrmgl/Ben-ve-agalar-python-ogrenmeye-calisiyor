import random
import temizle
secim=0
while secim==0:
    secim=int(input("""İşlem seçiniz;
İki tane rastgele sayı toplamı için-1
İki tane rastgele sayı farkı için-2
İki tane rastgele sayı çarpımı için-3
İki tane rastgele sayı bölümü için-4:
"""))
    temizle.temizle()
    while secim==1:
        temizle.temizle()
        min=int(input("x için minimum değeri giriniz:"))
        max=int(input("x için maximum değeri giriniz:"))
        x=random.randint(min,max)
        min=int(input("y için minimum değeri giriniz:"))
        max=int(input("y için maximum değeri giriniz:"))
        y=random.randint(min,max)
        print(x,"+",y,"=",x+y)
        secim=int(input("Aynı işleme devam etmek için için-1 çıkmak için-0 : "))
        temizle.temizle()
    while secim==2:
        temizle.temizle()
        min=int(input("x için minimum değeri giriniz:"))
        max=int(input("x için maximum değeri giriniz:"))
        x=random.randint(min,max)
        min=int(input("y için minimum değeri giriniz:"))
        max=int(input("y için maximum değeri giriniz:"))
        y=random.randint(min,max)
        print(x,"-",y,"=",x-y)
        secim=int(input("Aynı işleme devam etmek için için-2 çıkmak için-0 : "))
        temizle.temizle()
    while secim==3:
        temizle.temizle()
        min=int(input("x için minimum değeri giriniz:"))
        max=int(input("x için maximum değeri giriniz:"))
        x=random.randint(min,max)
        min=int(input("y için minimum değeri giriniz:"))
        max=int(input("y için maximum değeri giriniz:"))
        y=random.randint(min,max)
        print(x,"x",y,"=",x*y)
        secim=int(input("Aynı işleme devam etmek için için-3 çıkmak için-0 : "))
        temizle.temizle()
    while secim==4:
        temizle.temizle()
        min=int(input("x için minimum değeri giriniz:"))
        max=int(input("x için maximum değeri giriniz:"))
        x=random.randint(min,max)
        min=int(input("y için minimum değeri giriniz:"))
        max=int(input("y için maximum değeri giriniz:"))
        y=random.randint(min,max)
        print(x,"/",y,"=",x/y)
        secim=int(input("Aynı işleme devam etmek için için-4 çıkmak için-0 : "))
        temizle.temizle()
input()
