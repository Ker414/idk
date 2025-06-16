import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def todo_list():
    tasks = []

    while True:
        chose = int(input('''Выберете действие
1. посмотреть задачи
2. добавить задачу
3. убрать задачу
4. выход
ваш выбор: '''))

        if chose == 1:
            num = 1
            print('-=-=-=-=-=-=-=-=-=-=-=-=')
            for i in tasks:
                print(num,'.', i)
                num += 1
            print('-=-=-=-=-=-=-=-=-=-=-=-=')
            input('Enter')
            clear_console()
        
        if chose == 2:
            tasks.append(input('введите задачу: '))
            clear_console()
        
        if chose == 3:
            tasks.pop(int(input())-1)
            clear_console()
        if chose == 4:
            exit()

        

todo_list()