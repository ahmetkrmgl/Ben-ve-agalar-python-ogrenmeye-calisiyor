import temizle
secim=0
def otur():
    print("""  0
 /|7
  77
    """)
def kay():
    print("""  0
 /|>
 //
    """)
def sag():
    print("""  0
 /|7
  |7
    """)
def sol():
    print("""  0
 <|7
 /|
        """)
while secim!=5:
    secim=int(input("Oturmak için 1/Yaslanmak için 2/Kaymak için 3/Durmak için 4/Çıkmak için 5 giriniz:"))
    if secim==1:
        temizle.temizle()
        otur()
    elif secim==2:
        temizle.temizle()
        sol()
    elif secim==3:
        temizle.temizle()
        kay()
    elif secim==4:
        temizle.temizle()
        sag()
