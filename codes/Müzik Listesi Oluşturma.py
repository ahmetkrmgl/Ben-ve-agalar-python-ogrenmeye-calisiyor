liste=[""]
music=""
liste[0]=input("Bir müzik giriniz:")
while music !="yazmayı durdur":
    music=input("Bir müzik giriniz:")
    liste.append(music)
liste.pop()
for x in range(len(liste)):
    print(liste[x].title())