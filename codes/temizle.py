import os
def temizle():
    if os.name=="nt":
        os.system("cls")
    else:
        os.system("clear")
