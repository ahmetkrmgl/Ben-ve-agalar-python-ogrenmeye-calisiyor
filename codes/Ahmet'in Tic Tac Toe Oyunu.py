secim,x="devam et",0
oyuntahtası=[1,2,3,4,5,6,7,8,9]
import temizle
def ekranayaz():
    global oyuntahtası
    temizle.temizle()
    print("\n",oyuntahtası[0]," ",oyuntahtası[1]," ",oyuntahtası[2],"\n",
oyuntahtası[3]," ",oyuntahtası[4]," ",oyuntahtası[5],"\n",
oyuntahtası[6]," ",oyuntahtası[7]," ",oyuntahtası[8],"\n")
def xkazandi():
    global x
    global secim
    x=1
    ekranayaz()
    oyuntahtası.clear()
    print("""X kazandı!
Ama bence bir rövanş lazım!""")
    secim=input("Oyunu kapatmak istiyorsanız durdur/Devam etmek için devam et yazabilirsiniz:")
def okazandi():
    global x
    global secim
    x=1
    ekranayaz()
    oyuntahtası.clear()
    print("""O kazandı!
Ama bence bir rövanş lazım!""")
    secim=input("Oyunu kapatmak istiyorsanız durdur/Devam etmek için devam et yazabilirsiniz:")
def kontrolet():
    global oyuntahtası
    if oyuntahtası[0]==oyuntahtası[3]==oyuntahtası[6]=="X":
        xkazandi()#birinci sıra dikey
    elif oyuntahtası[1]==oyuntahtası[4]==oyuntahtası[7]=="X":
        xkazandi()#ikinci sıra dikey
    elif oyuntahtası[2]==oyuntahtası[5]==oyuntahtası[8]=="X":
        xkazandi()#üçüncü sıra dikey
    elif oyuntahtası[0]==oyuntahtası[1]==oyuntahtası[2]=="X":
        xkazandi()#birinci sıra yatay
    elif oyuntahtası[3]==oyuntahtası[4]==oyuntahtası[5]=="X":
        xkazandi()#ikinci sıra yatay
    elif oyuntahtası[6]==oyuntahtası[7]==oyuntahtası[8]=="X":
        xkazandi()#üçüncü sıra yatay
    elif oyuntahtası[0]==oyuntahtası[4]==oyuntahtası[8]=="X":
        xkazandi()#soldan sağa çapraz
    elif oyuntahtası[2]==oyuntahtası[4]==oyuntahtası[6]=="X":
        xkazandi()#sağdan sola çapraz
    elif oyuntahtası[0]==oyuntahtası[3]==oyuntahtası[6]=="O":
        okazandi()#birinci sıra dikey
    elif oyuntahtası[1]==oyuntahtası[4]==oyuntahtası[7]=="O":
        okazandi()#ikinci sıra dikey
    elif oyuntahtası[2]==oyuntahtası[5]==oyuntahtası[8]=="O":
        okazandi()#üçüncü sıra dikey
    elif oyuntahtası[0]==oyuntahtası[1]==oyuntahtası[2]=="O":
        okazandi()#birinci sıra yatay
    elif oyuntahtası[3]==oyuntahtası[4]==oyuntahtası[5]=="O":
        okazandi()#ikinci sıra yatay
    elif oyuntahtası[6]==oyuntahtası[7]==oyuntahtası[8]=="O":
        okazandi()#üçüncü sıra yatay
    elif oyuntahtası[0]==oyuntahtası[4]==oyuntahtası[8]=="O":
        okazandi()#soldan sağa çapraz
    elif oyuntahtası[2]==oyuntahtası[4]==oyuntahtası[6]=="O":
        okazandi()#sağdan sola çapraz
def oyun():
        global oyuntahtası
        if x==1:
            return
        ekranayaz()
        hangisix=int(input("X koymak istediğiniz yeri giriniz:"))
        oyuntahtası.pop(hangisix-1)
        oyuntahtası.insert(hangisix-1,"X")
        kontrolet()
        if x==1:
            return
        ekranayaz()
        hangisio=int(input("O koymak istediğiniz yeri giriniz:"))
        oyuntahtası.pop(hangisio-1)
        oyuntahtası.insert(hangisio-1,"O")
        kontrolet()
while secim !="durdur":
    if secim=="devam et":
        for i in range(len(oyuntahtası)):
            oyuntahtası.remove(i+1)
        for i in range(9):
            oyuntahtası.append(i+1)
        temizle.temizle()
        x=0
        secim=" "
    elif secim==" ":
        oyun()
