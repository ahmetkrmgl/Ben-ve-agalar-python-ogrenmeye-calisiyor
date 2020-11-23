liste.append() #sona ekle
liste.insert(index,değişken) #değişkeni bildirilen sıraya ekler
liste.clear() #tamamen sil
liste.count(değişken) #değişken kaç tane var
liste.index(değişken) #kaçıncı liste sırada
liste.pop(index) #o sıradaki değişkeni siliyor
liste.reverse() #listeyi terse çevirir
liste2 = liste #kısayol
liste3 = liste2.copy() #kopya
liste.extend(liste3) #birleştir
liste.sort() #elemanları sıralar /alfabetik ya da rakamsal
setim = {1,2,3}
liste.add(değişken)#ekleme
liste.update(değişken/liste)#ekleme
liste.discard(değişken)#varsa sil
del setim
setA | setB #union birleşim
setA.union(setB) #""
setA & setB #intersection kesişim
setA.intersection(setB)
setA - setB #difference fark
setA.difference(setB)
setA ^ setB #symmetric difference kesişim hariç
setA.symmetric_difference(setB)
tuple = ("büyücü","okçu","savaşçı")
tuple = ("büyücü") #string
tuple = ("büyücü",) #tuple
tuple[-2] #sondan ikinci
dict = {"elma":"apple","arda":"mal"}
dict[elma] #apple
dict[olmayan kelime] #ekleme
del dict[kelime]
string.split(işaret,sayı) #kelimelere ayırma
("ahmet#batın#arda#arif")
