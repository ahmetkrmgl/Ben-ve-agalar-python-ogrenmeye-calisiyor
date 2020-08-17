import random
f=open("kelimeler.txt","r")
kelimeler=f.readlines()
f.close()
anamenüseçim=0
def oyunuoyna():
    seçim = "e"
    puan = 0
    tahmindeneme = []
    while seçim=="e":
        kelime=kelimeler[random.randint(0,len(kelimeler)-1)]
        kelimeliste=[]
        uzunluk=len(kelime)-1
        for i in range(uzunluk):
            kelimeliste.append(kelime[i])
        tahmin=[]
        hak = 15
        for i in range(uzunluk):
            tahmin.append("_ ")
        print("Kelimemiz",uzunluk,"harfli")
        while tahmin != kelimeliste:
            harf=input("Bir Harf Giriniz:")
            for i in range(uzunluk):
                if harf==kelime[i]:
                    tahmin.pop(i)
                    tahmin.insert(i,harf)
            print("--------Tahmin Etmek İçin \"tahmin\" yazın--------")
            print(tahmin)
            if harf=="tahmin":
                tahmingirişi=input("Tahmininizi Giriniz:")
                tahmingirişiliste=[]
                for i in range(len(tahmingirişi)):
                    tahmingirişiliste.append(tahmingirişi[i])
                if tahmingirişiliste==kelimeliste:
                    print("tahmininiz doğru.......")
                    for i in range(uzunluk):
                        tahmin.pop(i)
                        tahmin.insert(i,tahmingirişiliste[i])
                    puan=puan+uzunluk*10
                else:
                    print("tahmininiz yanlış......")
                    puan=puan-uzunluk*5
            if tahmin==kelimeliste:
                print("Tebrikler Bildiniz :) :)")
                print("Kelimemiz",kelime)
                seçim=input("Tekrar Oynamak İster Misiniz [e/h]:")
            if hak==0:
                print("Malesef Tahmin Hakkınız Bitti....")
                print("Kelimemiz:",kelime)
                seçim=input("Tekrar Oynamak İster Misiniz [e/h]:")
                break
            print(hak,"Hakkınız Kaldı")
            hak=hak-1
    print("puanınız:")
    print(puan)
    print("çıkış yaptınız....")
    quit()
def anamenü():
    print("_"*50)
    print(" "*48,)
    print("[1] Oyunu Oyna"," "*34)
    print(" "*50)
    print("[2] Kütüphaneye kelime ekle",)
    print(" "*50)
    print("[3] ÇIKIŞ")
    print("_"*50)
    anamenüseçim=(input("="))
    if anamenüseçim!="1" and anamenüseçim!="2" and anamenüseçim!="3":
        print("Yanlış Değer Girdiniz...")
        anamenü()
    return anamenüseçim
def kelimeekle():
    kelimeekleme="a"
    while kelimeekleme!="1":
        kelimeekleseçim=0
        kelimeekleme=input("Kelime Gir:")
        if kelimeekleme=="1":
            break
        f=open("Kelimeler.txt","a")
        f.write("\n"+kelimeekleme)
        f.close()
        print("Kelime kütüphaneye eklendi......")
        print("_" * 50)
        print("Ana Menü'e gitmek için[1]")
    anamenü()
anamenüseçim=anamenü()
if anamenüseçim=="1":
    oyunuoyna()
elif anamenüseçim=="2":
    kelimeekle()
elif anamenüseçim=="3":
    quit()

