print("Merhaba,Hesap makinesine hoş geldiniz beaa")
print("""Toplama için 1 giriniz,
Çıkarma için 2 giriniz,
Çarpma için 3 giriniz,
Bölme için 4 giriniz""")
x=input("İşlem Seçiniz")
y=float(input("Sayı giriniz"))
z=float(input("Bir tane daha giriniz"))
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
    if y or z == 0:
        print("bir sayı 0'a bölünemez")
    else:
        print(y/z)
