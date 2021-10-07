import pyautogui
import time
contador = 0

pyautogui.alert('NÃO USAR O COMPUTADOR!')

while contador <= 50:
    pyautogui.moveTo(x=180, y=273)
    time.sleep(2)
    pyautogui.click()
    time.sleep(4)
    pyautogui.moveTo(x=1853, y=930)
    time.sleep(2)
    pyautogui.click()
    time.sleep(24)
    contador += 1
pyautogui.alert('FIM')
