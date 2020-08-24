hağngisi,x="devağm",0
kahvehanemasası=[1,2,3,4,5,6,7,8,9]
import os
def hijyen():
    if os.name=="nt":
        os.system("cls")
    else:
        os.system("clear")
def garadahdayayaz():
    global kahvehanemasası
    hijyen()
    print("\n",kahvehanemasası[0]," ",kahvehanemasası[1]," ",kahvehanemasası[2],"\n",
kahvehanemasası[3]," ",kahvehanemasası[4]," ",kahvehanemasası[5],"\n",
kahvehanemasası[6]," ",kahvehanemasası[7]," ",kahvehanemasası[8],"\n")
def xsaglamkoydu():
    global x
    global hağngisi
    x=1
    garadahdayayaz()
    kahvehanemasası.clear()
    print("""X Oturttuuu!
Varmısınız Bi El Daha HE??""")
    hağngisi=input("TickTackToeyi Kapamak İstiyorsanız kapanamkoyunu/Devam Etmek için ise devağm yazabilirsiniz:")
def osaglamkoydu():
    global x
    global hağngisi
    x=1
    garadahdayayaz()
    kahvehanemasası.clear()
    print("""O Oturttuuu!
Varmısınız Bi El Daha HE??""")
    hağngisi=input("TickTackToeyi Kapamak İstiyorsanız kapanamkoyunu/Devam Etmek için ise devağm yazabilirsiniz:")
def kontrolet():
    global kahvehanemasası
    if kahvehanemasası[0]==kahvehanemasası[3]==kahvehanemasası[6]=="X":
        xsaglamkoydu()
    elif kahvehanemasası[1]==kahvehanemasası[4]==kahvehanemasası[7]=="X":
        xsaglamkoydu()
    elif kahvehanemasası[2]==kahvehanemasası[5]==kahvehanemasası[8]=="X":
        xsaglamkoydu()
    elif kahvehanemasası[0]==kahvehanemasası[1]==kahvehanemasası[2]=="X":
        xsaglamkoydu()
    elif kahvehanemasası[3]==kahvehanemasası[4]==kahvehanemasası[5]=="X":
        xsaglamkoydu()
    elif kahvehanemasası[6]==kahvehanemasası[7]==kahvehanemasası[8]=="X":
        xsaglamkoydu()
    elif kahvehanemasası[0]==kahvehanemasası[4]==kahvehanemasası[8]=="X":
        xsaglamkoydu()
    elif kahvehanemasası[2]==kahvehanemasası[4]==kahvehanemasası[6]=="X":
        xsaglamkoydu()
    elif kahvehanemasası[0]==kahvehanemasası[3]==kahvehanemasası[6]=="O":
        osaglamkoydu()
    elif kahvehanemasası[1]==kahvehanemasası[4]==kahvehanemasası[7]=="O":
        osaglamkoydu()
    elif kahvehanemasası[2]==kahvehanemasası[5]==kahvehanemasası[8]=="O":
        osaglamkoydu()
    elif kahvehanemasası[0]==kahvehanemasası[1]==kahvehanemasası[2]=="O":
        osaglamkoydu()
    elif kahvehanemasası[3]==kahvehanemasası[4]==kahvehanemasası[5]=="O":
        osaglamkoydu()
    elif kahvehanemasası[6]==kahvehanemasası[7]==kahvehanemasası[8]=="O":
        osaglamkoydu()
    elif kahvehanemasası[0]==kahvehanemasası[4]==kahvehanemasası[8]=="O":
        osaglamkoydu()
    elif kahvehanemasası[2]==kahvehanemasası[4]==kahvehanemasası[6]=="O":
        osaglamkoydu()
def tavlatavla():
        global kahvehanemasası
        if x==1:
            return
        garadahdayayaz()
        hangisix=int(input("X Nireye Binecen Böhöhöh:"))
        kahvehanemasası.pop(hangisix-1)
        kahvehanemasası.insert(hangisix-1,"X")
        kontrolet()
        if x==1:
            return
        garadahdayayaz()
        hangisio=int(input("O Nireye Binecen Böhöhöh:"))
        kahvehanemasası.pop(hangisio-1)
        kahvehanemasası.insert(hangisio-1,"O")
        kontrolet()
while hağngisi !="kapanamkoyunu":
    if hağngisi=="devağm":
        for i in range(len(kahvehanemasası)):
            kahvehanemasası.remove(i+1)
        for i in range(9):
            kahvehanemasası.append(i+1)
        hijyen()
        x=0
        hağngisi=" "
    elif hağngisi==" ":
        tavlatavla()
