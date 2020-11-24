import random
secim=0
while secim==0:
    secim=int(input("""İşlem seçiniz[İki tane rastgele sayı toplamı için-1/
    İki tane rastgele sayı farkı için-2/
    İki tane rastgele sayı çarpımı için-3/
    İki tane rastgele sayı bölümü için-4"""]))
    while secim==1:#Rastgele sayı toplamı
        min=int(input("x için minimum değeri giriniz:"))
        max=int(input("x için maximum değeri giriniz:"))
        x=random.randint(min,max)
        min=int(input("y için minimum değeri giriniz:"))
        max=int(input("y için maximum değeri giriniz:"))
        y=random.randint(min,max)
        print(x,"+",y,"=",x+y)
        secim=int(input("devam etmek için-1 çıkmak için-0"))
    while secim==2:
        min=int(input("x için minimum değeri giriniz:"))
        max=int(input("x için maximum değeri giriniz:"))
        x=random.randint(min,max)
        min=int(input("y için minimum değeri giriniz:"))
        max=int(input("y için maximum değeri giriniz:"))
        y=random.randint(min,max)
        print(x,"-",y,"=",x-y)
        secim=int(input("devam etmek için-2 çıkmak için-0"))
    while secim==3:
        min=int(input("x için minimum değeri giriniz:"))
        max=int(input("x için maximum değeri giriniz:"))
        x=random.randint(min,max)
        min=int(input("y için minimum değeri giriniz:"))
        max=int(input("y için maximum değeri giriniz:"))
        y=random.randint(min,max)
        print(x,"x",y,"=",x*y)
        secim=int(input("devam etmek için-3 çıkmak için-0"))
    while secim==4:
        min=int(input("x için minimum değeri giriniz:"))
        max=int(input("x için maximum değeri giriniz:"))
        x=random.randint(min,max)
        min=int(input("y için minimum değeri giriniz:"))
        max=int(input("y için maximum değeri giriniz:"))
        y=random.randint(min,max)
        print(x,"/",y,"=",x/y)
        secim=int(input("devam etmek için-4 çıkmak için-0"))
