import random
import os

class Tkm():
    def temizle(self):
        if os.name=="nt":
            os.system("cls")
        else:
            os.system("clear")

    def anasayfa(self):
        secim=input("Taş kağıt makas oynayalım mı?: ")
        return secim

    def girdial(self):
        girdi=input("Taş...kağıt...makas?:")
        print("\n")
        return girdi

    def secimyap(self):
        sayi=random.randint(1,3)
        if sayi==1:
            bilgisayar="taş"
        elif sayi==2:
            bilgisayar="kağıt"
        elif sayi==3:
            bilgisayar="makas"
        return bilgisayar

    def karsilastir(self,girdi,bilgisayar,oyuncupuan,bilgisayarpuan):
        print(bilgisayar.capitalize(),"\n")
        if girdi==bilgisayar:
            print("Hmm...aynı yaptık, bir daha","\n")
            print(oyuncupuan,"-",bilgisayarpuan,"\n")
            return 0
        elif girdi=="taş" and bilgisayar=="makas":
            print("Makasımı kırdın demek...:()","\n")
            oyuncupuan+=1
            print(oyuncupuan,"-",bilgisayarpuan,"\n")
            return 1
        elif girdi=="taş" and bilgisayar=="kağıt":
            print("Haha! Kağıt taşı sarar...ne işe yarar bilmiyorum ama puan benim işte sonuçta :D","\n")
            bilgisayarpuan+=1
            print(oyuncupuan,"-",bilgisayarpuan,"\n")
            return 2
        elif girdi=="makas" and bilgisayar=="taş":
            print("Yazık oldu makasına :(","\n")
            bilgisayarpuan+=1
            print(oyuncupuan,"-",bilgisayarpuan,"\n")
            return 2
        elif girdi=="makas" and bilgisayar=="kağıt":
            print("Makas kağıdı keser ha :( olsun gene de bu kağıtları kullanırım ben bir yerde...","\n")
            oyuncupuan+=1
            print(oyuncupuan,"-",bilgisayarpuan,"\n")
            return 1
        elif girdi=="kağıt" and bilgisayar=="taş":
            print("Ha ha çok komik, tamam şimdi taşımı bırakma vakti...","\n")
            oyuncupuan+=1
            print(oyuncupuan,"-",bilgisayarpuan,"\n")
            return 1
        elif girdi=="kağıt" and bilgisayar=="makas":
            print("Heh, gel bakalım buraya...kağıııt kaçma! Hem tamam bak tam ortadan bölerim A5 olur, sınıf atlarsın","\n")
            bilgisayarpuan+=1
            print(oyuncupuan,"-",bilgisayarpuan,"\n")
            return 2
secim="evet"
oyun=Tkm()
while "olur" in secim or "tamam" in secim or "evet" in secim or "tabii" in secim or "neden olmasın" in secim or "elbette" in secim:
    oyuncupuan,bilgisayarpuan,oyuncu,bilgisayar=0,0,"",""
    secim=oyun.anasayfa().lower()
    if secim=="hayır" or secim=="asla" or secim=="olmaz":
        print("peki madem...")
        break
    while oyuncupuan<3 or bilgisayarpuan<3:
        oyuncu=oyun.girdial().lower()
        oyun.temizle()
        bilgisayar=oyun.secimyap()
        x=oyun.karsilastir(oyuncu,bilgisayar,oyuncupuan,bilgisayarpuan)
        if x==1:
            oyuncupuan+=1
        elif x==2:
            bilgisayarpuan+=1
        if oyuncupuan==3:
            print("Tebrikler sen kazandın...tabii algoritmayı yendim diye havalanmayasın ha!","\n"," Tekrar tekrar yenersen belki :/","\n")
            break
        elif bilgisayarpuan==3:
            print("Haha! N'aber yenilen pehlivan, doydun mu bakalım güreşe?","\n")
            break
print("kazandınız")
