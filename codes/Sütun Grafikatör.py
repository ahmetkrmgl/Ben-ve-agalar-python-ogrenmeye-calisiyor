from matplotlib import pyplot as plt
isimler,degerler,renk,baslik,isim,deger,girdi=[],[],"","","","",""
while girdi!="bitti":
    girdi=input("Bir isim girin:")
    if girdi=="bitti":
        break
    isimler.append(girdi)
    girdi=int(input("Girdiğiniz isime ait sayı değerini girin:"))
    if girdi=="bitti":
        break
    degerler.append(girdi)
renk=input("Renk seçimi yapınız(ingilizce):")
baslik=input("Grafik için başlık giriniz:")
isim=input("Girmiş olduğunuz isimlere bir grup adı verin(örn.yarışmacılar):")
deger=input("Girmiş olduğunuzsayı değerlerine bir grup adı verin(örn.puanlar):")
plt.bar(isimler,degerler,color = renk)
plt.title(baslik)
plt.xlabel(isim)
plt.ylabel(deger)
plt.show()
input("")
