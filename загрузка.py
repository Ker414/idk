import time

for i in range (1001):
    print(f'загрузка: {i / 10}%')
    
    time.sleep(0.01)
print ('загрузка завершина')