from matplotlib import pyplot as plt
girdi,isimler,degerler,explode,list="",[],[],(),[]
while girdi!="bitti":
    girdi=input("Bir isim giriniz:")
    if girdi=="bitti":
        break
    isimler.append(girdi)
    girdi=input("Girdiğiniz isme ait değeri giriniz:")
    if girdi=="bitti":
        break
    degerler.append(girdi)
for i in range(len(isimler)):
    list.append(0)
explode=tuple(list)
fig, ax1=plt.subplots()
ax1.pie(degerler,explode=explode,labels=isimler,autopct='%1.1f%%',shadow="True",startangle=90)
ax1.axis('equal')
plt.show()
input("")
