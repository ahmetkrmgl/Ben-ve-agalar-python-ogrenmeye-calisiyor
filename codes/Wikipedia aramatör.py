import wikipedia
import temizle
while(0<1):
    page = input("Ara:")
    sayfa = wikipedia.page(page)
    print(sayfa.title)
    input("")
    print(sayfa.url)
    input("")
    print(sayfa.content)
    print(" "*50)
    input("   Aramaya devam etmek için enter'a basın")
    temizle.temizle()
