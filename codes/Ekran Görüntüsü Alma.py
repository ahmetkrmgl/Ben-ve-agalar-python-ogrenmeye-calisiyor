import pyautogui
from time import sleep
adres=input("Kaydetmek istediğiniz dizin+dosyaya vermek istediğiniz ismi giriniz:")
print("3")
sleep(1)
print("2")
sleep(1)
print("1")
sleep(1)
pyautogui.screenshot(r"{}".format(adres))
