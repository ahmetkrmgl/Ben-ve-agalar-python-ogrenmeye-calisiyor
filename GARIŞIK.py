mrogramcıpatınaga=1
while mrogramcıpatınaga==1:
    print("""Dikdörtgen Alanı ve Çevresi Bulmak İçin 1'e
Vize ve Final Notu Ortalaması Hesaplamak İçin 2'Ye
Programı Kapatmak İçin 3'e Basınız""")
    secim=int(input("HAĞNGİSİ:"))
    if secim==2:
        vize=int(input("Vize Notunuzu Giriniz:"))
        final=int(input("Final Notunuzu Giriniz:"))
        ortalama=(float(vize)*0.3)+(float(final)*0.7)
        print("Ortalama:{}".format(ortalama))
    elif secim==1:
        programcıbatınbey=0
        while programcıbatınbey==0:
            kısa=input('Kısa Kenar:')
            uzun=input('Uzun Kenar:')
            alan=int(kısa)*int(uzun)
            çevre=2*(int(kısa)+int(uzun))
            print("Alan:{}".format(alan))
            print("Çevre:{}".format(çevre))
            break
    elif secim==3:
        mrogramcıpatınaga=0
        break
        
        
        
        
                 
