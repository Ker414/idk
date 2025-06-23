import keyboard
import time

#keyboard.press('')
#keyboard.release('')
#keyboard.press_and_release('')

time.sleep(3)

for i in range(40):
    for i in range(23):
        keyboard.press_and_release('p')
        keyboard.press_and_release('e')
        keyboard.press_and_release('n')
        keyboard.press_and_release('i')
        keyboard.press_and_release('s')
        keyboard.press_and_release('space')
    keyboard.press_and_release('enter')
