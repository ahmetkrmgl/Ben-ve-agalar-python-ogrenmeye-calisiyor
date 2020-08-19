import os
secim=input("Dosyayı sıfırlamak için evet yazın(istemiyorsanız entera basın):")
if secim=="evet":
    os.remove("müziklistesi.txt")
liste=open("müziklistesi.txt","w")
music=""
liste.write("{} \n".format(input("Bir müzik giriniz:")))
while music !="yazmayı durdur":
    music=input("Bir müzik giriniz:")
    if music!="yazmayı durdur":
        liste.write("{} \n".format(music))
liste.close()
