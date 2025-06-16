import time
import os
print('Введите количество секунд')
a = int(input())
while a > 0:
    sec = a % 60
    min = a // 60
    time.sleep(1)
    os.system('cls')
    print(f'Осталось: {min}:{sec}')
    a -= 1
os.system('cls')
print('Время вышло!')