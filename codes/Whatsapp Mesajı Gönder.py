import pywhatkit as whatsapp
mesaj=input("Mesajınızı Giriniz:")
numara=input("Göndermek İstediğiniz Numarayı(ülke kodu ile)Giriniz:")
zaman=input("Mesajı Göndermek İstediğiniz Zamanı(Saat{saat tek haneliyse sıfırsız şekilde}:Dakika)Giriniz:")
saat=zaman[0:2]
if ":" in saat:
    saat = saat[0]
dakika=zaman[2:len(zaman)]
if ":" in dakika:
    dakika = dakika[1:3]
whatsapp.sendwhatmsg(numara,mesaj,saat,dakika)
input("")
