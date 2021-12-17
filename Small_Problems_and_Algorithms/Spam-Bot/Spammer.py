import pyautogui, time
time.sleep(5)

f=open("Beescript.txt",'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("ENTER")

