secim=""
kullanıcıadı=input("Kullanıcı adı giriniz:")
while "{} maldır".format(kullanıcıadı) not in secim:
    print("{} maldır yazana kadar durmayacağım".format(kullanıcıadı))
    secim=input("Söyle!:")