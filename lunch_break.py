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
keyboard.press_and_release('esc')
sleep(0.1)
moving_and_clicking(width, 37)
moving_and_clicking(width, height + 163)
moving_and_clicking(width, height + 413)
sleep(0.1)
keyboard.press_and_release('enter')
sleep(0.1)
keyboard.press_and_release('down')
sleep(0.1)
keyboard.press_and_release('down')
sleep(0.1)
keyboard.press_and_release('down')
sleep(0.1)
keyboard.press_and_release('enter')
sleep(0.1)
keyboard.press_and_release('tab')
sleep(0.1)
keyboard.press_and_release('enter')
sleep(0.1)
keyboard.press_and_release('1')
sleep(0.1)
keyboard.press_and_release('enter')
sleep(0.1)
keyboard.press_and_release('tab')
sleep(0.1)
keyboard.press_and_release('enter')
sleep(1)

# Escrever a mensagem
keyboard.press_and_release('down')
sleep(0.1)
keyboard.press_and_release('down')
sleep(0.1)
keyboard.press_and_release('enter')
sleep(0.1)
return_time = (datetime.now() + timedelta(hours=1)).strftime('%H:%M')
sleep(0.1)
keyboard.write(f'Em intervalo de almoço. Retorno às {return_time}')
sleep(0.1)
keyboard.press_and_release('tab')
sleep(0.1)
keyboard.press_and_release('tab')
sleep(0.1)
keyboard.press_and_release('tab')
sleep(0.1)
keyboard.press_and_release('enter')
sleep(0.1)
keyboard.press_and_release('1')
sleep(0.1)
keyboard.press_and_release('enter')
sleep(0.1)
keyboard.press_and_release('tab')
sleep(0.1)
keyboard.press_and_release('enter')
sleep(0.1)
keyboard.press_and_release('esc')
sleep(0.1)
moving_and_clicking(0, 0)
