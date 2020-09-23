from pytube import YouTube
link = input("Linki Giriniz:")
print("İndiriliyor...")
YouTube(link).streams.first().download()
print("Video indirildi")
input("")
