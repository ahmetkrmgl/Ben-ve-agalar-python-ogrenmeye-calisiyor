secim,liste="",[]
def hesapmakinesi(x,y):
    return x+y,x-y,x*y,x/y
while secim!="programdan çık":
    liste=hesapmakinesi(int(input("Bir sayı gir:")),int(input("Bir sayı daha gir:")))
    for x in liste:
        print(x)
    secim=input("Çıkmak için \"programdan çık yazınız\"/Devam etmek için \"enter'a\" basın:")