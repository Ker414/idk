import threading
import time
import os
import random

map = '--------------------------------------------------------'
attention_line = ['  ','  ','  ','  ',]
jump = False

# Очистка терминала
def clear_terminal():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/Mac
        os.system('clear')

# Движение карты и поражение
def independent_task():
    while True:
        # Добавление препятствий
        if len(attention_line) <= 22:
            box_pattern = ['  ', '  ','[]']
            random.shuffle(box_pattern)
            box_pattern.append('  ')
            box_pattern.append('  ')
            for s in box_pattern:
                attention_line.append(s)
        
        # 1 шаг карты
        attention_line.pop(0)
        time.sleep(0.6)
        
        
        # Условия поражения
        if jump is False and attention_line[0] == '[]':
            print("Вы проиграли")
            os._exit(0)

# Создаем и запускаем поток игры
thread = threading.Thread(target=independent_task)
thread.start()

# Отрисовка карты + прыжка
def game_picture():
    score = 0
    while independent_task:
        box_line = ''
        
        for i in attention_line:
            box_line = box_line + i
        if jump is False:
            print()
            print('O',box_line)
        elif jump is True:
            print('O')
            print(' ',box_line)
        print(map)
        
        print('''
[Enter] - прыгать
-------------''')
        
        time.sleep(0.2)
        score += 0.25
        clear_terminal()
        print(f'Очки: {score}')

# Создаем и запускаем поток отрисовки
thread = threading.Thread(target=game_picture)
thread.start()

# Прыжок
while True:
    if jump is False:
        jump_ = input()
        jump = True
        print('прыжок')
        time.sleep(0.6)
        jump = False
        print('падение')
        time.sleep(0.2)