class Kullanici:
    def __init__(self,ad,soyad,yaş,boy,kilo,md):
        self.ad = ad #ad = girilen ad
        self.soyad = soyad
        self.yas = yaş
        self.boy = boy
        self.kilo = kilo
        self.md = md

class Isci(Kullanici):
    def __init__(self,ad,soyad,yaş,boy,kilo,md,maas,ig,vardiya,mesai):
        self.maas=maas
        self.ig=ig
        self.vardiya=vardiya
        self.mesai=mesai
        Kullanici.__init__(self,ad,soyad,yaş,boy,kilo,md)

kullanicigereksinimleri=["Ad:","Soyad:","Yaş:","Boy:","Kilo:","Medeni durum:"]
iscigereksinimleri=["Ad:","Soyad:","Yaş:","Boy:","Kilo:","Medeni durum:","Maaş:","İzin günü:","Vardiya:","Mesai:"]
sorgu=input("İşçi misiniz:")
sorgu=sorgu.lower()

if sorgu=="hayır":
    for x in kullanicigereksinimleri:
        giriş=input(x)
        sıra=kullanicigereksinimleri.index(x)
        kullanicigereksinimleri.remove(x)
        kullanicigereksinimleri.insert(sıra,giriş)
    kullanici=Kullanici(kullanicigereksinimleri[0],kullanicigereksinimleri[1],kullanicigereksinimleri[2],kullanicigereksinimleri[3],kullanicigereksinimleri[4],kullanicigereksinimleri[5])
    print("\n","Kullanıcı adı: ",kullanici.ad,"\n","Kullanıcı yaşı: ",kullanici.yas,"\n","Kullanıcı soyadı: ",kullanici.soyad,"\n","Kullanıcı boyu:",kullanici.boy,"\n","Kullanıcı medeni durumu: ",kullanici.md,"\n","Kullanıcı kilosu: ",kullanici.kilo,"\n")

elif sorgu=="evet":
    for x in iscigereksinimleri:
        giriş=input(x)
        sıra=iscigereksinimleri.index(x)
        iscigereksinimleri.remove(x)
        iscigereksinimleri.insert(sıra,giriş)
    isci=Isci(iscigereksinimleri[0],iscigereksinimleri[1],iscigereksinimleri[2],iscigereksinimleri[3],iscigereksinimleri[4],iscigereksinimleri[5],iscigereksinimleri[6],iscigereksinimleri[7],iscigereksinimleri[8],iscigereksinimleri[9])
    print("\n","İşçi adı: ",isci.ad,"\n","İşçi yaşı: ",isci.yas,"\n","İşçi soyadı: ",isci.soyad,"\n","İşçi boyu: ",isci.boy,"\n","İşçi medeni durumu: ",isci.md,"\n","İşçi kilosu: ",isci.kilo,"\n","İşçi maaşı:",isci.maas,"\n","İşçi izin günü: ",isci.ig,"\n","İşçi vardiyası: ",isci.vardiya,"\n","İşçi mesaisi: ",isci.mesai)

else:
    print("lütfen evet ya da hayır yazınız")
input()
