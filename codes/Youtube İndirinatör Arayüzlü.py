from tkinter import *
from pytube import YouTube
def indir():
    myVar.set("İndiriliyor...")
    root.update()
    YouTube(link.get()).streams.first().download()
    myVar.set("İndirildi!")
root = Tk()
root.geometry("500x150")
root.title("Youtube Video İndirme Uygulaması")
Label(root, text="",font="Consolas 15 bold").pack()
myVar = StringVar()
myVar.set("Linki Aşağıya Giriniz")
Entry(root, textvariable=myVar, width=18).pack(pady=10)
link = StringVar()
link.set("")
Entry(root, textvariable=link, width=70).pack(pady=10)
Button(root, text="Videoyu İndir", command=indir).pack()
root.mainloop()
