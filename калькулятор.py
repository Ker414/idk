def calculate (num1, num2, znak):

#проверка действия
    if znak == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif znak == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    elif znak == '/':
        print(f'{num1} / {num2} = {num1 / num2}')
    elif znak == '*':
        print(f'{num1} * {num2} = {num1 * num2}')
    elif znak == '^':
        print(f'{num1} ^ {num2} = {num1 ** num2}')
    else:
        print('*Неверный знак*')
#повтор
    print('---------------------------------------------------')
    calculate (float(input('а = ')), float(input('b = ')), input('действие (+-*/^) : '))    

#запуск
print ('a,b - числа')
calculate (float(input('а = ')), float(input('b = ')), input('действие (+-*/^) : '))