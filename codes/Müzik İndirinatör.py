from pafy import pafy
url=input("Linki Giriniz:")
video=pafy.new(url)

bestaudio = video.getbestaudio()
bestaudio.download()
