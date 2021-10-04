import pyautogui
import time
contador = 0

pyautogui.alert(
    'O Python ira assumir o controle do Computador! Por favor, não mexa!')

while contador <= 880:
    pyautogui.PAUSE = 0.1
    pyautogui.moveTo(697, 211)
    pyautogui.mouseDown()
    pyautogui.mouseUp
    time.sleep(0.1)
    pyautogui.press('enter')
    contador += 1
pyautogui.alert('Fim')


#  pyautogui.alert('')          -     Mostra mensagem na tela.
#  pyautogui.PAUSE = 0.0        -     Adiciona um delay no code
#  pyautogui.press('')          -     Pressiona uma tecla no teclado
#  pyautogui.write('')          -     Digita texto
#  pyautogui.hotkey('', '')     -     Pressiona teclas de atalho
#  pyautogui.position()         -     Mostra posição do mouse
#  pyautogui.moveTo(x, y)       -     Move o mouse até a posição
#  pyautogui.mouseDown()        -     Clica botão do mouse (por padrão botão esquerdo)
#  pyautogui.mouseUp ()         -     Soltar botão do mouse
