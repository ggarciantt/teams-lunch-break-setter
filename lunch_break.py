from time import sleep
from datetime import datetime, timedelta
import mouse
import keyboard

# Coordenadas do ícone do usuário no Teams
width=3040
height=37

def moving_and_clicking(x, y):
    mouse.move(x, y, duration=0.5)
    mouse.click(mouse.LEFT)    

# Definir o status para ausente
moving_and_clicking(0, 0)
sleep(0.3)
keyboard.press_and_release('esc')
sleep(0.3)
moving_and_clicking(width, height)
sleep(0.3)
keyboard.press_and_release('tab')
sleep(0.3)
keyboard.press_and_release('up')
sleep(0.3)
keyboard.press_and_release('enter')
sleep(0.3)
keyboard.press_and_release('down')
sleep(0.3)
keyboard.press_and_release('down')
sleep(0.3)
keyboard.press_and_release('down')
sleep(0.3)
keyboard.press_and_release('down')
sleep(0.3)
keyboard.press_and_release('down')
sleep(0.3)
keyboard.press_and_release('down')
sleep(0.3)
keyboard.press_and_release('enter')
sleep(0.3)
keyboard.press_and_release('enter')
sleep(0.3)
keyboard.press_and_release('down')
sleep(0.3)
keyboard.press_and_release('down')
sleep(0.3)
keyboard.press_and_release('down')
sleep(0.3)
keyboard.press_and_release('enter')
sleep(0.3)
keyboard.press_and_release('tab')
sleep(0.3)
keyboard.press_and_release('enter')
sleep(0.3)
keyboard.press_and_release('1')
sleep(0.3)
keyboard.press_and_release('enter')
sleep(0.3)
keyboard.press_and_release('tab')
sleep(0.3)
keyboard.press_and_release('enter')
sleep(1)

# Escrever a mensagem
keyboard.press_and_release('esc')
sleep(0.3)
keyboard.press_and_release('enter')
sleep(0.3)
keyboard.press_and_release('down')
sleep(0.3)
keyboard.press_and_release('down')
sleep(0.3)
keyboard.press_and_release('enter')
sleep(0.3)
return_time = (datetime.now() + timedelta(hours=1)).strftime('%H:%M')
keyboard.write(f'Em intervalo de almoço. Retorno às {return_time}')
sleep(0.3)
keyboard.press_and_release('tab')
sleep(0.3)
keyboard.press_and_release('space')
sleep(0.3)
keyboard.press_and_release('tab')
sleep(0.3)
keyboard.press_and_release('tab')
sleep(0.3)
keyboard.press_and_release('enter')
sleep(0.3)
keyboard.press_and_release('1')
sleep(0.3)
keyboard.press_and_release('enter')
sleep(0.3)
keyboard.press_and_release('tab')
sleep(0.3)
keyboard.press_and_release('enter')
sleep(0.3)
keyboard.press_and_release('esc')
sleep(0.3)
moving_and_clicking(0, 0)
