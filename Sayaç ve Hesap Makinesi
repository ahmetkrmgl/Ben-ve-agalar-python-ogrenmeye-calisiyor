programkontrol=1
while programkontrol==1:
    print("""Sayaç için 1
Hesap makinesi için 2
Programı kapatmak için 3""")
    secim=int(input("Seçim giriniz:"))
    if secim==1:
        alttaban=int(input("Alttaban giriniz:"))
        üsttaban=int(input("Üsttaban giriniz:"))
        kaçarkaçar=int(input("Kaçar Kaçar Sayim Abi:"))
        while alttaban<üsttaban:
            print(alttaban)
            alttaban+=kaçarkaçar
    elif secim==2:
        hesapmakinesikontrol=0
        while hesapmakinesikontrol==0:
            print("""Merhaba,Hesap makinesine hoş geldiniz beaa
------------------------------------------""")
            print("""Toplama için 1
Çıkarma için 2
Çarpma  için 3
Bölme   için 4
Çıkış için 5""")
            x=input("İşlem Seçiniz:")
            if x=='5':
                hesapmakinesikontrol=1
                continue
            y=float(input("Sayı giriniz:"))
            z=float(input("Bir tane daha giriniz:"))
            if x=='1':
                print(y+z)
            elif x=='2':
                if y>z:
                    print(y-z)
                else:
                    print(z-y)
            elif x=='3':
                print(y*z)
            elif x=='4':
                if z == 0:
                    print("Bir sayı 0'a bölünemez!")
                else:
                    print(y/z)
    elif secim==3:
        programkontrol=0
        break
